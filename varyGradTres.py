from util import *

if __name__ == '__main__':
    datapath = 'data'
    savepath = 'gradT_out'
    histpath = 'hist'
    boundarypath = 'gradT_boundary'
    
    filename = "1_gray.bmp"
    imagepath = os.path.join(datapath, filename)
    image = cv2.imread(imagepath, 0)
    
    for t in range(10, 200, 10):
        
        
        
        thresholds, threshold, boundary = getThreshold(image, t)
        print('threshold for {}: {}, t: {}'.format(filename, threshold, t))
        cv2.imwrite(os.path.join(boundarypath, filename.split('.')[0] + '_{}'.format(t) + '.bmp'), boundary)
            
        # plot the histogram
        # n, bins, patches = plt.hist(thresholds, bins=256, facecolor='blue', alpha=0.75)
        # plt.savefig(os.path.join(histpath, filename.split('.')[0] + '_{}_{}'.format(t, int(threshold)) + '.png'))
        # plt.cla()
            
        # segment the image with the threshold, which is the mean of all the gray value as threshold.
        _, img_treated = cv2.threshold(image, int(threshold), 255, cv2.THRESH_BINARY)
        cv2.imwrite(os.path.join(savepath, filename.split('.')[0] + '_{}_{}'.format(t, int(threshold)) +'.bmp'), img_treated)
        