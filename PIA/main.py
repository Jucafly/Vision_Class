#PIA
#Equipo 11
#Ashley Sierra Uribe - 1818031
#Juan Carlos Valdez Flores - 1942636
#----------Librerias---------------#
import cv2
from matplotlib.pyplot import contour
import numpy as np

#--------------Fase 1--------------#
#Seleccion de Imagenes
img = cv2.imread("Assets\Img1small.jpg")
#img = cv2.imread("Assets\ImgTest.jpg")
#imgshow = cv2.imread("Assets\Img1small.jpg")
cv2.imshow("Original",img)
#cv2.imshow("show",imgshow)
#img = cv2.VideoCapture(0)
cv2.waitKey(0)
cv2.destroyAllWindows()

#-------(Pre-Procesamiento)--------#

amarilloBajo = np.array([20,70,120])
amarilloAlto = np.array([30,255,255])

verdeBajo = np.array([69,35,12])
verdeAlto = np.array([90,255,225])

imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
maskAmarillo = cv2.inRange(imgHSV,amarilloBajo,amarilloAlto)
maskVerde = cv2.inRange(imgHSV,verdeBajo,verdeAlto)


#Convertimos a Blanco y negro
#Se covierte para un mejor analisis de la imagen
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
cv2.imshow("Blanco y Negro",imgGray)
cv2.waitKey(0)

#Binarizacion 
#Se aplica la binarizacion para correcion de or
ret,imgtresh = cv2.threshold(imgGray,46,255,0)
cv2.imshow("Mask", imgtresh)
cv2.waitKey(0)

#--------------Fase 2-----------#
#Canny
#Aplicacion Filtro Canny para detectar bordes
imgcanny = cv2.Canny(imgtresh,10,150)
imgcanny = cv2.dilate(imgcanny,None,iterations=1)
cv2.imshow("Canny", imgcanny)
cv2.waitKey(0)


#--------------Fase 3-----------#
#Buscamos los Contornos y los dibujamos
#Funcion para buscar los Contornos
contour, hierarchy = cv2.findContours(imgcanny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.imshow("Original",img)
cv2.imshow("Blanco y Negro",imgGray)
cv2.imshow("Mask", imgtresh)
cv2.imshow("Canny", imgcanny)
cv2.waitKey(0)
cv2.destroyAllWindows()

for c in contour:
    epsilon = 0.02*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)
    print("El numero de lados es: ")
    print(len(approx))
    x,y,w,h = cv2.boundingRect(approx)

    if len(approx)==4:
        cv2.putText(img,"Rectangulo", (x+40,y+40),1,1,(255,106,0),1)
        cv2.putText(maskAmarillo,"Amarillo", (x+40,y+40),1,1,(255,106,0),1)

    if len(approx)>=8:
        cv2.putText(img,"Circulo", (x-5,y-5),1,1,(168,204,10),1)
        cv2.putText(maskVerde,"Verde", (x-30,y-30),1,1,(168,204,10),1)
        

    cv2.drawContours(img,[c],-1,(0,0,255),3)
    cv2.imshow("Original",img)
    cv2.imshow("Amarillo", maskAmarillo)
    cv2.imshow("Verde", maskVerde)
    cv2.waitKey(0)


