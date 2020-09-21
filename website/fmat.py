import numpy as np
import time
from os import path

# the sole purpose of this file is for importing the F matrix

basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "..", "data2.txt"))
f = open(filepath, "r")
# f = open('../data2.txt', 'r')
start = time.time()
F = f.read()
f.close()
# print(a[0:100])
F = F.split(' ')
F = F[0:len(F)-1]
for i in range(len(F)):
    F[i] = float(F[i])
print(len(F))
F = np.array(F).reshape(20,500,1900)