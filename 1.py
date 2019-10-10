import cv2
import numpy as np

def histograma_global(frame):
    hist=np.zeros((3,256), dtype=int)

    for i in range(len(frame)):
        for j in range(len(frame[0])):
            for k in range(3):
                hist[k][frame[i][j][k]]+=1

    return hist

def diff(hf, hg):
    dr = 0
    dg = 0
    db = 0
    for i in range(255):
        db += np.abs((hf[0][i]-hg[0][i]))
        dg += np.abs((hf[1][i]-hg[1][i]))
        dr += np.abs((hf[2][i]-hg[2][i]))
    # print(db, dg, dr)
    return (db+dg+dr)/3.0

vd = cv2.VideoCapture('1.mp4')

w=60 #Tamanho da janela
limiar=(1<<20)

ret,frame=vd.read()
hist0 = histograma_global(frame)
q=1
while True:
    for i in range(2*w+1):
        ret,frame=vd.read()
        if not ret:
            break
    if not ret:
        break
    q+=2*w+1
    
    ret,frame=vd.read()
    hist1 = histograma_global(frame)
    d = diff(hist0, hist1)
    if d>limiar:
        print("Cena detectada no quadro %d" %q)
    hist0 = np.array(hist1)
