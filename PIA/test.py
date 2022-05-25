import cv2
from matplotlib.pyplot import contour
import numpy as np



amarilloBajo = np.array([20,70,120])
amarilloAlto = np.array([30,255,255])

verdeBajo = np.array([69,35,12])
verdeAlto = np.array([90,255,225])

img = cv2.imread("Assets\Img1small.jpg")
#img = cv2.imread("Assets\ImgTest.jpg")
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

maskAmarillo = cv2.inRange(imgHSV,amarilloBajo,amarilloAlto)
maskVerde = cv2.inRange(imgHSV,verdeBajo,verdeAlto)

cv2.imshow("Amarillo", maskAmarillo)
cv2.imshow("Verde", maskVerde)
cv2.imshow("orignial", img)
cv2.waitKey(0)
