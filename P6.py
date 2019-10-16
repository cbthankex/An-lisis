### P6
import P5;
import numpy as np;
import matplotlib as plt;
from skimage import io;

def comprimir(imagen, tolerancia):
    m = io.imread(str(imagen))/255.0
    h,w,c=m.shape
    mg = np.zeros((h,w))
    m_red=np.copy(m)[:,:,0]
    m_green=np.copy(m)[:,:,1]
    m_blue=np.copy(m)[:,:,2]
    for i in range(h):
        for j in range(w):
            mg[i,j] = (m_red[i,j]+m_green[i,j]+m_blue[i,j])/3
    msvd= P5.svd(mg);
    error= tolerancia - max(msvd[1])
    return(msvd, error)