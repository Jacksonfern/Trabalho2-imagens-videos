import cv2
import numpy as np

def histograma_central(frame):
    hist = np.zeros((3,256), dtype=int)
    cut = 0.1 #Ignora 10% da extremidade
    xa = cut*frame.shape[0]
    xb = (1-cut)*frame.shape[0]
    ya = cut*frame.shape[1]
    yb = (1-cut)*frame.shape[1]
    # print(xa, xb, ya, yb)

    for i in range(frame.shape[0]):
        if i>=xa and i<xb:
            for j in range(frame.shape[1]):
                if j>=ya and j<yb:
                    for k in range(3):
                        hist[k][frame[i][j][k]]+=1

    return hist

vd = cv2.VideoCapture('2.mp4')
ret, frame = vd.read()
print(frame.shape)
hist = histograma_central(frame)
