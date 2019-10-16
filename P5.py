### P5
import numpy as np;
def gs(X):
    Q, R = np.linalg.qr(X)
    return Q
def svd(A):
    r = min(np.size(A,0),np.size(A,1))
    m = max(np.size(A,0),np.size(A,1))
    ATA=(A.T)@A;
    if (r==np.size(A,0)):
        V=np.zeros((r,m));
        U=np.zeros((m,r));
    else:
        V=np.zeros((m,r));
        U=np.zeros((r,m));
    vps = np.array(np.linalg.eig(ATA)[0]);
    VPs = np.array(np.linalg.eig(ATA)[1]);
    R=gs(-VPs)
    i=0;
    while(i<r):
        c=0;
        while(c<r):
            if(-np.sort(-vps)[i] == vps[c]):
                 np.array(V)[i] = -np.array(R)[c]
                 np.array(R)[c] = np.array(R)[i]
            c+=1
        U[i]=A@V[i]*(1/np.sqrt(-np.sort(-vps)[i]))
        i+=1
    i=0;
    sigma = np.diag(np.diag(np.sqrt(-np.sort(np.array(-vps)))))
    return(np.array(U),np.array(sigma),np.array(V))
