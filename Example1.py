#Importamos las Librerias
import cv2
##Cargas la imagen
img1 = cv2.imread("Assets\Img1.jpeg")
img2 = cv2.imread("Assets\Img2.jpeg")
#Muestras la imagen
cv2.imshow('image',img1)
#Espera a presionar una tecla
cv2.waitKey(0)
#Cierra todas las ventanas
cv2.destroyAllWindows()
#Imagen es un arreglo de 2 dimensiones 

cv2.imshow('image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
