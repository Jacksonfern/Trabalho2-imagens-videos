import cv2
import numpy as np

#particao da imagem em centro, cima e baixo
def histograma_particionado(frame):
    hist = np.zeros((3,256,3), dtype=int)
    cut = 0.1 #particiona 10% da imagem
    xa = cut*frame.shape[0]
    xb = (1-cut)*frame.shape[0]
    ya = cut*frame.shape[1]
    yb = (1-cut)*frame.shape[1]
    # print(xa, xb, ya, yb)

    for i in range(frame.shape[0]):
        for j in range(frame.shape[1]):
            if i>=xa and i<xb and j>=ya and j<yb:
                p=0
            elif i<frame.shape[0]/2:
                p=1
            else:
                p=2
            for k in range(3):
                hist[p][frame[i][j][k]][k]+=1
    return hist

def diff_histograma_particionado(hf, hg):
    diff = 0
    for p in range(3):
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
limiar = 1000000

ret,frame = vd.read()
hf = histograma_particionado(frame)
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
    hg = histograma_particionado(frame)
    diff = diff_histograma_particionado(hf, hg)
    print(diff)
    if diff>limiar:
        print("Mudanca de cena no quadro %d"%q)
    hf = hg
