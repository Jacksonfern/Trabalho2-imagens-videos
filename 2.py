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

def diff_histograma_local(hf, hg):
    diff = 0
    for p in range(25):
        dr = 0
        dg = 0
        db = 0
        for i in range(255):
            db += np.abs((hf[p][i][0]-hg[p][i][0]))
            dg += np.abs((hf[p][i][1]-hg[p][i][1]))
            dr += np.abs((hf[p][i][2]-hg[p][i][2]))
        # print(db, dg, dr)
        diff += (db+dg+dr)/3.0
    return diff

vd = cv2.VideoCapture('1.mp4')
w=60 #Tamanho da janela
limiar = (1<<22)

ret,frame = vd.read()
hf = histograma_local(frame)
q=0
while True:
    for i in range(2*w+1):
        ret,frame = vd.read()
        q+=1
        if not ret:
            break
    if not ret:
        break
    ret,frame=vd.read()
    q+=1
    hg = histograma_local(frame)
    diff = diff_histograma_local(hf, hg)
    if diff>limiar:
        print("Mudanca de cena no quadro %d"%q)
    hf = hg