import cv2
import numpy as np

def histograma_global(frame):
    hist=np.zeros((256,3), dtype=int)

    for i in range(len(frame)):
        for j in range(len(frame[0])):
            for k in range(3):
                hist[frame[i][j][k]][k]+=1

    return hist

def diff(hf, hg):
    dr = 0
    dg = 0
    db = 0
    for i in range(255):
        db += np.abs((hf[i][0]-hg[i][0]))
        dg += np.abs((hf[i][1]-hg[i][1]))
        dr += np.abs((hf[i][2]-hg[i][2]))
    # print(db, dg, dr)
    return (db+dg+dr)/3.0

vd = cv2.VideoCapture('1.mp4')

w=60 #Tamanho da janela
limiar=(1<<20)

ret,frame=vd.read()
hf = histograma_global(frame)
q=0
while True:
    for i in range(2*w+1):
        ret,frame=vd.read()
        q+=1
        if not ret:
            break
    if not ret:
        break
    
    ret,frame=vd.read()
    q+=1
    hg = histograma_global(frame)
    d = diff(hf, hg)
    if d>limiar:
        print("Cena detectada no quadro %d" %q)
    hf = hg
