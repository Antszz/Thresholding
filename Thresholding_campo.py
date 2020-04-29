import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Coseschas_trigo.png')
img2 = cv2.imread('Coseschas_trigo.png', cv2.IMREAD_GRAYSCALE)
res = cv2.imread('Coseschas_trigo.png')
res2 = cv2.imread('Coseschas_trigo.png')
cv2.imshow('xD', img)
cv2.imshow('xD', img2)
histB = cv2.calcHist([img], [0], None, [256], [0, 256])
histG = cv2.calcHist([img], [1], None, [256], [0, 256])
histR = cv2.calcHist([img], [2], None, [256], [0, 256])
histN = cv2.calcHist([img2], [0], None, [256], [0, 256])

height, width, chanels = img.shape
c=0
for i in range(height):
    for j in range(width):
        if(img[i][j][0]>200 or img[i][j][1]>220 or img[i][j][2]<200):        
            res[i][j]=0

for i in range(height):
    for j in range(width):
        if(img2[i][j]<182 or img2[i][j]>188):
            res2[i][j]=0
        
cv2.imshow('1',res)
cv2.imshow('2',res2)
#plt.plot(histB, color='blue' )
#plt.plot(histG, color='green' )
#plt.plot(histR, color='red' )
plt.plot(histN, color='black' )
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

cv2.destroyAllWindows()