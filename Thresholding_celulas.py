
import cv2
import numpy as np
from matplotlib import pyplot as plt

def Celulas_Buenas1(img):
    height, width = img.shape
    res = cv2.imread('CelulasRatones1.png', cv2.IMREAD_GRAYSCALE)
    for i in range(height):
        for j in range(width):
            if(img[i][j]>=193 and img[i][j]<=195 ):
                res[i][j]=255
            else:
                res[i][j]=0
    cv2.imshow('Celulas Buenas Imagen 1',res)

def Celulas_Malas1(img):
    height, width = img.shape
    res = cv2.imread('CelulasRatones1.png', cv2.IMREAD_GRAYSCALE)
    for i in range(height):
        for j in range(width):
            if(img[i][j]<=190 ):
                res[i][j]=255
            else:
                res[i][j]=0
    cv2.imshow('Celulas Malas Imagen 1',res)

def Celulas_Buenas2(img):
    height, width = img.shape
    res = cv2.imread('CelulasRatones2.png', cv2.IMREAD_GRAYSCALE)
    for i in range(height):
        for j in range(width):
            if(img[i][j]>=193 and img[i][j]<=195 ):
                res[i][j]=255
            else:
                res[i][j]=0
    cv2.imshow('Celulas Buenas Imagen 2',res)

def Celulas_Malas2(img):
    height, width = img.shape
    res = cv2.imread('CelulasRatones2.png', cv2.IMREAD_GRAYSCALE)
    for i in range(height):
        for j in range(width):
            if(img[i][j]<=186 ):
                res[i][j]=255
            else:
                res[i][j]=0
    cv2.imshow('Celulas Malas Imagen 2',res)

def Imagen1(img):
    cv2.imshow('Celulas 1', img)
    Celulas_Malas1(img)
    Celulas_Buenas1(img)

def Imagen2(img):
    cv2.imshow('Celulas 2', img)
    Celulas_Malas2(img)
    Celulas_Buenas2(img)

img = cv2.imread('CelulasRatones1.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('CelulasRatones2.png', cv2.IMREAD_GRAYSCALE)


hist = cv2.calcHist([img], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
        

#Imagen1(img)
#plt.plot(hist, color='gray' )

Imagen2(img2)
plt.plot(hist2, color='red' )

plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

cv2.destroyAllWindows()