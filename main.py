# EE356 Project 1
# Author: Huang Siyuan (519030910095)
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# Laplace operator, gradient operator.
laplace = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
gx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
gy = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

def getThreshold(image, t):
    l, w = image.shape
    #image = cv2.GaussianBlur(image,(5,5),0)
    
    # enlarge the image by one pixel on every edge, and the expended area is filled with the grey value of the adjacent original pixel.
    enlarged_image = np.zeros((l+2, w+2), dtype=int)
    enlarged_image[1:1+l,1:1+w] = image
    enlarged_image[0,1:1+w] = image[0,:]
    enlarged_image[-1,1:1+w] = image[0,:]
    enlarged_image[:, 0] = enlarged_image[:, 1]
    enlarged_image[:, -1] = enlarged_image[:, -2]
    #print(enlarged_image)
    
    # Save the result
    laplacian = np.zeros((l,w), dtype=int)
    gradient = np.zeros((l,w), dtype=float)
    
    for i in range(l):
        for j in range(w):
            laplacian[i,j] = (enlarged_image[i:i+3, j:j+3] * laplace).sum()
            gradientx = (enlarged_image[i:i+3, j:j+3] * gx).sum()
            gradienty = (enlarged_image[i:i+3, j:j+3] * gy).sum()
            gradient[i,j] = (np.sqrt(np.power(gradientx, 2) + np.power(gradienty, 2)))
    
    
    thresholds = list() # list of the gray values of all boundary points
    sum = 0 # sum of the gray values
    boundary = np.zeros((l, w), dtype=np.uint8) # result image of edge detection
    for i in range(l):
        for j in range(w):
            # traverse all the pixels，examine (i, j), and whether the boundary intersects the edges between (i,j+1) and itself, (i+1,j) and itself.
            # the vertice itself is on the boundry.
            if laplacian[i, j] == 0 and gradient[i, j] >= t:
                sum += image[i,j]
                boundary[i, j] = image[i, j]
                thresholds.append(image[i, j])
                
            # the boundary goes through the two vertices.
            if i < l - 1 and laplacian[i, j] * laplacian[i+1, j] < 0 and gradient[i, j] + gradient[i+1, j] >= 2 * t:
                gray_level = (int(image[i, j]) + int(image[i+1, j])) // 2
                boundary[i, j] = image[i, j]
                boundary[i+1, j] = image[i+1, j]
                sum += gray_level
                thresholds.append(gray_level)
                
            if j < w - 1 and laplacian[i, j] * laplacian[i, j+1] < 0 and gradient[i, j] + gradient[i, j+1] >= 2 * t:
                gray_level = (int(image[i, j]) + int(image[i, j+1])) // 2
                boundary[i, j] = image[i, j]
                boundary[i, j+1] = image[i, j+1]
                sum += gray_level
                thresholds.append(gray_level)
                
    
    threshold = sum / (len(thresholds)) # calculate the mean of all the gray value.
    print("num boundary points: ", len(thresholds))
    return thresholds, threshold, boundary

def calHist(threshold):
    hist = np.zeros(256, dtype=float)
    for i in threshold:
        hist[i] += 1
    hist /= len(threshold)
    return hist
    
    
if __name__=='__main__':
    datapath = 'data'
    savepath = 'out'
    histpath = 'hist'
    boundarypath = 'boundary'
    t_dic = {'1_gray.bmp': 90, '6.jpg': 90, '8_gray.bmp': 90, "13.bmp": 90, "14.bmp": 90, "22.bmp": 90, "23.bmp": 35, "40.jpg": 90} # dic of different gradient thresholds for test images.
    
    for filepath, dirnames, filenames in os.walk(datapath):
        for filename in filenames:
            imagepath = os.path.join(filepath, filename)
            image = cv2.imread(imagepath, 0)
            t = t_dic[filename]
            thresholds, threshold, boundary = getThreshold(image, t)
            print('threshold for {}: {}, t: {}'.format(filename, threshold, t))
            
            # plot the histogram
            n, bins, patches = plt.hist(thresholds, bins=256, facecolor='blue', alpha=0.75)
            plt.savefig(os.path.join(histpath, filename.split('.')[0] + '_{}_{}'.format(t, int(threshold)) + '.png'))
            plt.cla()
            
            # segment the image with the threshold, which is the mean of all the gray value as threshold.
            # NOTE: More discussion on Multilevel threshold selection, Bi-level threshold selection and the corresponding results are shown in the report.
            _, img_treated = cv2.threshold(image, int(threshold), 255, cv2.THRESH_BINARY)
            cv2.imwrite(os.path.join(savepath, filename.split('.')[0] + '_{}_{}'.format(t, int(threshold)) +'.bmp'), img_treated)
            cv2.imwrite(os.path.join(boundarypath, filename.split('.')[0] + '_{}_{}'.format(t, int(threshold)) + '.bmp'), boundary)
    
    # 114514
    # img1 = cv2.imread(test, 0)
    # lap = cv2.Laplacian(img1, cv2.CV_16S, ksize=3)
    # dst = cv2.convertScaleAbs(lap)
    # print(dst)
    # cv2.imshow("laplace", dst)
    # cv2.waitKey(0)