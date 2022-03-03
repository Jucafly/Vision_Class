import cv2 as cv
import numpy as np
from matplotlib import cm, pyplot as plt

##Cargamos Imagenes
##-----------------Imagen 1----------------##
##Imagen 1 RGB
img1RGB = cv.imread("Assets\Img1small.jpg",1)
##Imagen Escala de Grises
img1ByN = cv.imread("Assets\Img1small.jpg",0)

##-----------------Imagen 2----------------##
##Imagen 2 RGB
img2RGB = cv.imread("Assets\LenaTest.png")
##Imagen Escala de Grises
img2ByN = cv.imread("Assets\LenaTest.png",0)

##cv.imshow('Imagen 1 RGB',img1RGB)
##cv.imshow('Imagen 1 ByN',img1ByN)


histRGB = cv.calcHist([img1RGB],[1],None,[256],[0,265])
histByN = cv.calcHist([img1ByN],[0],None,[256],[0,265])


##Se Crea la tabla
##-----------------Tabla 1----------------##
fig, ax=plt.subplots(2,2)

ax[0,0].imshow(img1RGB)
ax[0,0].set_title('Imagen 1 RGB')
ax[0,0].axis('off')

ax[1,0].imshow(img1ByN,cmap='gray')
ax[1,0].set_title('Imagen 1 ByN')
ax[1,0].axis('off')

ax[0,1].hist(img1RGB.ravel(),256,[0,256])
ax[0,1].set_title('Histograma 1 RGB')


ax[1,1].hist(img1ByN.ravel(),256,[0,256])
ax[1,1].set_title('Histograma 1 ByN')


##-----------------Tabla 2----------------##

fig, ay=plt.subplots(2,2)

ay[0,0].imshow(img2RGB)
ay[0,0].set_title('Imagen 2 RGB')
ay[0,0].axis('off')

ay[1,0].imshow(img2ByN,cmap='gray')
ay[1,0].set_title('Imagen 2 ByN')
ay[1,0].axis('off')

ay[0,1].hist(img2RGB.ravel(),256,[0,256])
ay[0,1].set_title('Histograma 2 RGB')


ay[1,1].hist(img2ByN.ravel(),256,[0,256])
ay[1,1].set_title('Histograma 2 ByN')




cv.waitKey(0)
cv.destroyAllWindows()



