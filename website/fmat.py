import numpy as np
import time
# the sole purpose of this file is for importing the F matrix

f = open('data2.txt', 'r')
start = time.time()
F = f.read()
f.close()
# print(a[0:100])
F = F.split(' ')
F = F[0:len(F)-1]
for i in range(len(F)):
    F[i] = float(F[i])
F = np.array(F).reshape(20,500,1900)