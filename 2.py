import numpy as np
import cv2

def histograma_local(frame):
    hist = np.zeros((25,256,3), dtype=int) #Histograma grid 5x5
    tam_gridX = frame.shape[0]//5 #Dimensao vertical particionada
    tam_gridY = frame.shape[1]//5 #Dimensao horizontal particionada

    for i in range(frame.shape[0]):
        for j in range(frame.shape[1]):
            x = (i//tam_gridX)
            y = (j//tam_gridY)
            grid = 5*x+y
            for k in range(3):
                hist[grid][frame[i][j][k]][k]+=1

    return hist

vd = cv2.VideoCapture('1.mp4')
for i in range(100):
    ret, frame = vd.read()
hist_local = histograma_local(frame)