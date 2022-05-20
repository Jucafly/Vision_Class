##Actividad Fundamental 4
##Imports
import sys
import cv2 as cv


def main(argv):
    ##Variales
    profundidad = cv.CV_16S
    matrizkernel1 = 3
    matrizkernel2 = 5
    nombreImagen1 = 'Imagen 1 Kernel 1'
    nombreImagen2 = 'Imagen 1 Kernel'

    ##Cargando Imagen
    src1 = cv.imread("Assets\Img4small.jpeg", cv.IMREAD_COLOR) 
    src2 = cv.imread("Assets\Img4small.jpeg", cv.IMREAD_COLOR) 

    ## Revisamo si la iagen funciona bien 
    if src1 is None:
        print ('Error al cargar la imagen, Reviasr variable src1')
        return -1
    
    if src2 is None:
        print ('Error al cargar la imagen, Reviasr variable src2')
        return -1

    ## Se limpia la imagen con el Blur
    src1 = cv.GaussianBlur(src1, (3, 3), 0)
    src2 = cv.GaussianBlur(src2, (3, 3), 0)
    
    ## Convertimos a Escala de Grises
    srcEscalaGrises1 = cv.cvtColor(src1, cv.COLOR_BGR2GRAY)
    srcEscalaGrises2 = cv.cvtColor(src2, cv.COLOR_BGR2GRAY)

    ## Aplicamos filtro de Laplace
    srclaplace1 = cv.Laplacian(srcEscalaGrises1, profundidad, ksize=matrizkernel1)
    srclaplace2 = cv.Laplacian(srcEscalaGrises2, profundidad, ksize=matrizkernel2)
  
    ## Convertimos unidad de 8bits
    srcfinal1 = cv.convertScaleAbs(srclaplace1)
    srcfinal2 = cv.convertScaleAbs(srclaplace2)
    
    ##Mostramops la imagen
    cv.imshow(nombreImagen1, srcfinal1)
    cv.imshow(nombreImagen2, srcfinal2)
    cv.waitKey(0)
   
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])