### P7
import P6;
import os;

def analizar(path, extension):
    os.chdir(path)
    E=0;
    i=0;
    for filename in os.listdir(path):
        print(filename)
        if filename.endswith(extension):
            m, error = P6.comprimir(filename,0)
            i+=1;
            E+=error;
    return np.abs(E)