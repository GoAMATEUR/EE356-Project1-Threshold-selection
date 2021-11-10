import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

laplace = np.array([[1,1,1], [1,-8,1], [1,1,1]])
gx = np.array([[-1,0,1], [-1,0,1], [-1,0,1]])
gy = np.array([[-1,-1,-1], [0,0,0], [1,1,1]])

def getBoundaryMatrix(image, t):
    l, w = image.shape
    image_blur = cv2.GaussianBlur(image,(5,5),0)
    
    enlarged_image = np.zeros((l+2, w+2), dtype=int)
    enlarged_image[1:1+l,1:1+w] = image_blur
    #print(enlarged_image)
    
    laplacian = np.zeros((l,w), dtype=int)
    boundaryMatrix = np.zeros((l,w), dtype=np.uint8)
    gradient = np.zeros((l,w), dtype=float)
    count = 0
    
    for i in range(l):
        for j in range(w):
            laplacian[i,j] = abs((enlarged_image[i:i+3, j:j+3] * laplace).sum())
            
            gradientx = (enlarged_image[i:i+3, j:j+3] * gx).sum()
            gradienty = (enlarged_image[i:i+3, j:j+3] * gy).sum()
            gradient[i,j] = (np.sqrt(np.power(gradientx, 2) + np.power(gradienty, 2)))
            
            if laplacian[i,j] == 0 and gradient[i,j] >= t:
                boundaryMatrix[i,j] = image[i,j]
                count += 1
    # print('num of boundry point:', count)
    # n, bins, patches = plt.hist(boundaryMatrix.flatten(), bins=100)
    # plt.show()
    # cv2.imshow('la', laplacian.astype(np.uint8))
    # cv2.waitKey(0)
    return boundaryMatrix, count

def calThreshold(boundaryMatrix):
    pass

if __name__=='__main__':
    datapath = 'data'
    savepath = 'out'
    t = 118 # threshold for EQ. 1
    #118
    
    for filepath, dirnames, filenames in os.walk(datapath):
        for filename in filenames:
            imagepath = os.path.join(filepath, filename)
            image = cv2.imread(imagepath, 0)
            boundaryMatrix, count = getBoundaryMatrix(image, t)
            threshold = boundaryMatrix.astype(int).sum() / count
            print('threshold for {}: {}'.format(filename, threshold))
            # cv2.imshow('boundary points', boundaryMatrix)
            # cv2.waitKey(0)
            _, img_treated = cv2.threshold(image, int(threshold), 255, cv2.THRESH_BINARY)
            cv2.imwrite(os.path.join(savepath, filename), img_treated)
            # cv2.imshow('output', img_treated)
            # cv2.waitKey(0)
    
    # for i in range(114,115, 1):
    #     print(i)
        # boundaryMatrix, count = getBoundaryMatrix(image, t)
        
        # threshold = boundaryMatrix.astype(int).sum() / count
        # print('threshold: ', threshold)    
    
    
    # img1 = cv2.imread(test, 0)
    # lap = cv2.Laplacian(img1, cv2.CV_16S, ksize=3)
    # dst = cv2.convertScaleAbs(lap)
    # print(dst)
    # cv2.imshow("laplace", dst)
    # cv2.waitKey(0)
    
    # mat1 = np.array([[  0,   0,   0],[  0, 164, 164,],[  0, 160, 162]])
    # print((mat1* laplace).sum())
