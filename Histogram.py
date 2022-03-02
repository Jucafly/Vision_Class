import cv2 as cv
import cv2
import numpy as np
from matplotlib import cm, pyplot as plt


#Lectura de Imagenes
img1 = cv.imread("Assets\Img1small.jpg")

b,g,r=cv.split(img1)

#Creamos la Tabla
fig, ax=plt.subplots(2,2)

##-------------Imagen Uno---------------##
#  [1,0]
#  [0,0] Imagen RGB Full
ax[0,0].imshow(img1)
ax[0,0].set_title('RGB Image')
ax[0,0].axis('off')

#  [0,1]
#  [0,0] Histograma RGB full
hist = cv2.calcHist([img1],[0],None,[256],[0,256])
ax[0,1].plot(hist)
ax[0,1].set_title('Histograma RGB')

##-------------Imagen Dos---------------##
#  [0,0]
#  [1,0] Imagen RGB Full
ax[1,0].imshow(b)
ax[1,0].set_title('B Image')
ax[1,0].axis('off')

#  [0,0]
#  [0,1] Histograma RGB full
bhist = cv2.calcHist([b],[0],None,[256],[0,256])
ax[1,1].plot(b)
ax[1,1].set_title('Histograma RGB')




cv2.waitKey(0)
cv2.destroyAllWindows()
