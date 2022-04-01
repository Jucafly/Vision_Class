##Librerias
import cv2
import numpy
##1942636
##Juan Carlos Valdez Flores
##Lectura de imagen
img = cv2.imread('Assets/img2Small.jpeg',cv2.IMREAD_GRAYSCALE)
img_width = img.shape[1]
img_heigh = img.shape[0]
##Matriz de ceroz
img_filter = numpy.zeros((img_heigh,img_width),numpy.uint)
##Kernel
kernel = [
            [1,1,1],
            [1,1,1],
            [1,1,1]
            ]
for w in range (img_width):
    for h in range (img_heigh):
        if w == 0 or h==0 or w==img_width-1 or h==img_heigh-1:
            img_filter[h][w]=0
        else:
            img_filter[h][w]=(img[h-1][w-1]*kernel[0][0]+img[h][w-1]*kernel[1][0]+img[h+1][w-1]*kernel[2][0]+img[h-1][w]
            *kernel[0][1]+img[h][w]*kernel[1][1]+img[h+1][w]*kernel[2][1]+img[h+1][w+1]*kernel[0][2]+img[h][w+1]*kernel[1][2]+img[h+1][w+1]*kernel[2][2])/9
##Show
cv2.imshow('Imagen 1', img)
cv2.imshow('Imagen Filtrada',img_filter[0])
cv2.waitKey(0)
cv2.destroyAllWindows()