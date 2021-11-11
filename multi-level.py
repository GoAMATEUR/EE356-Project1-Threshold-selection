# Multi-threshold selection
# Author: Huang Siyuan (519030910095)
from util import *

if __name__ == "__main__":
    
    datapath = 'data'
    savepath = 'out'
    histpath = 'hist'
    boundarypath = 'boundary'
    t_dic = {"22.bmp": 130, "23.bmp": 40} # dic of different gradient thresholds for test images.
    
    cluster_segments = {"22.bmp": [0, 110, 256], "23.bmp": [0,44,81,256]} # input the gray levels that segment clusters in boundary gray level histogram, deduced from saved histograms.
    
    for filename in list(t_dic.keys()):
        t = t_dic[filename]
        image = cv2.imread(os.path.join(datapath, filename), 0)
    
        thresholds, _, boundary = getThreshold(image, t)
        hist = calHist(thresholds)
        cv2.imwrite(os.path.join(boundarypath, filename.split('.')[0] + '_{}'.format(t) + '.bmp'), boundary)
        
        # plot the histogram
        n, bins, patches = plt.hist(thresholds, bins=256, facecolor='blue', alpha=0.75)
        plt.savefig(os.path.join(histpath, filename.split('.')[0] + '_{}'.format(t) + '.png'))
        #plt.show()
        plt.cla()
        
        
        cluster_segment = cluster_segments[filename]
        multi_thresholds = [] # calculated thresholds
        # calculate the mean of each cluster.
        for i in range(len(cluster_segment) - 1):
            sum = 0
            count = 0
            for gray in range(cluster_segment[i], cluster_segment[i+1]):
                count += hist[gray]
                sum += hist[gray] * gray
            multi_thresholds.append(int(sum/count))
        print(multi_thresholds)
                
        
        for i in range(len(multi_thresholds)):
            
            if i < len(multi_thresholds) - 1:
                image_treated = binaryImage(image, multi_thresholds[i], multi_thresholds[i+1])
                cv2.imwrite(os.path.join(savepath, filename.split('.')[0] + '_{}_{}'.format(t, i) +'.bmp'), image_treated)
                
            else:
                image_treated = binaryImage(image, multi_thresholds[0])
                cv2.imwrite(os.path.join(savepath, filename.split('.')[0] + '_{}_{}'.format(t, i) +'.bmp'), image_treated)
                image_treated = binaryImage(image, multi_thresholds[-1])
                cv2.imwrite(os.path.join(savepath, filename.split('.')[0] + '_{}_{}'.format(t, i+1) +'.bmp'), image_treated)