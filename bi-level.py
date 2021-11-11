from util import *

def getMainPeak(hist):
    return np.argmax(np.array(hist))

if __name__ == "__main__":
    datapath = 'data'
    savepath = 'out'
    histpath = 'hist'
    boundarypath = 'boundary'
    
    t_dic = {'1_gray.bmp': 80, "13.bmp": 110} # dic of different gradient thresholds for test images.
    
    for filename in list(t_dic.keys()):
        t = t_dic[filename]
        image = cv2.imread(os.path.join(datapath, filename), 0)
    
        thresholds, threshold, boundary = getThreshold(image, t)
        
        hist = calHist(thresholds)
        print("mean threshold: ", threshold)
        cv2.imwrite(os.path.join(boundarypath, filename.split('.')[0] + '_{}'.format(t) + '.bmp'), boundary)
        
        # plot the histogram
        n, bins, patches = plt.hist(thresholds, bins=256, facecolor='blue', alpha=0.75)
        plt.savefig(os.path.join(histpath, filename.split('.')[0] + '_{}'.format(t) + '.png'))
        #plt.show()
        plt.cla()
        
        main_threshold = getMainPeak(hist)
        print("main peak: " , main_threshold)
        image_treated = binaryImage(image, main_threshold)
        cv2.imwrite(os.path.join(savepath, filename.split('.')[0] + '_{}_{}'.format(t, main_threshold) +'.bmp'), image_treated)