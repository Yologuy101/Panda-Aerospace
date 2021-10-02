
import cv2
from matplotlib import pyplot as plt

#reading the image, can be changed to any file on your system.
img = cv2.imread("filename", cv2.IMREAD_GRAYSCALE)

#this uses canny edge detection.
edges = cv2.Canny(img,100,300)

#show the processed image
plt.imshow(edges, 'gray')
plt.show()
