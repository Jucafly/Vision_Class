#Actividad Fundamental 6
#Ashley Sierra Uribe
#Juan Carlos Valdez Flores

#Librerias
import cv2
from cv2 import threshold
import numpy as np

#Leemos Imagen
img = cv2.imread('Assets\Img1small.jpg')

#Transformamos a 8bits
img8bits = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Definimos el treshold que la imagen va a tomar
threshold = 60

#Se define la mascara con los valores de treshold
masrk = np.uint8((img8bits<threshold)*255)

#Se muestra la imagen
cv2.imshow("Original",img)
cv2.imshow("Sin Binarizar",img8bits)
cv2.imshow("Binarizada",masrk)
cv2.waitKey(0)
