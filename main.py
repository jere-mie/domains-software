# imports section
import numpy as np
import pandas as pd
from scipy.integrate import quad
from scipy.special import spherical_jn as jn
import time

# compute F matrix section
def integrand(x,l):
  return jn(l,x) * x**2

def integrated(q,r1,r2,l):
  return (q**-3)*(quad(integrand,q*r1,q*r2, args=(l))[0])

# open F matrix


# compute Omega and Theta matrix section

########################
# main section
########################

# getting F matrix
f = open('data2.txt', 'r')
start = time.time()
F = f.read()
f.close()
# print(a[0:100])
F = F.split(' ')
F = F[0:len(F)-1]
for i in range(len(F)):
    F[i] = float(F[i])
    if i%100000==0:
        print(i)
print(len(F))
F = np.array(F).reshape(20,500,1900)
print(len(F))

from omega import Omat, Tmat
print(len(Omat))
print(len(Tmat))

# matrix multiplication step

Wp = []
for i in range(len(F)):
    Wp.append(F[i].dot(Omat))
Wp = np.array(Wp)
print(len(Wp))
print(len(Wp[0]))
print(len(Wp[0][0]))
Wp = np.swapaxes(Wp,0,1)
print()
print(len(Wp))
print(len(Wp[0]))
print(len(Wp[0][0]))
print(Wp.shape)
for i in range(len(Wp)):
    for j in range(len(Wp[0])):
        for k in range(len(Wp[0][0])):
            Wp[i][j][k] = np.abs(Wp[i][j][k]**2)