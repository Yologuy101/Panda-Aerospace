
#this program uses LAB (Light, green - red, blue -yellow) color space to detect green vegetation
import cv2
import numpy as np

thresh = 40
#reading the image, can be changed to any file on your system.
img = cv2.imread("Image\Example 1 zoomed #2.png")
imgLAB = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

#LAB processing 
color = [0, 0,5]
lab = cv2.cvtColor( np.uint8([[color]] ), cv2.COLOR_BGR2LAB)[0][0]
minLAB = np.array([lab[0] - thresh, lab[1] - thresh, lab[2] - thresh])
maxLAB = np.array([lab[0] + thresh, lab[1] + thresh, lab[2] + thresh])
maskLAB = cv2.inRange(imgLAB, minLAB, maxLAB)
resultLAB = cv2.bitwise_and(imgLAB, imgLAB, mask = maskLAB)

#show the processed image
cv2.imshow("Output LAB", resultLAB)
cv2.waitKey()

#the next line can be uncommented and be used to store the processed image
#cv2.imwrite("filename", resultLAB)

