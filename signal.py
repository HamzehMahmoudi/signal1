import matplotlib.pyplot as plt
import cv2
import numpy as np
img = cv2.imread('cameraman.png',0) # tabdil ax be array
#plt.hist(img.ravel(),256,[0,256])  
#plt.show()
img2= cv2.equalizeHist(img)     # hamgen kardane array
cv2.imwrite('cameraman2.png',img2)  #tabdil array hamgen shode be tasvir va zakhire ba esme cameraman2.png
img3 = np.hstack((img,img2))   #kenar ham gozashtan array(baraye moghayese sade tar)
cv2.imwrite('IOComparison.png',img3) # zakhire dar file iocomparison
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clh= clahe.apply(img)
cv2.imwrite('cameraman3.jpg',clh)