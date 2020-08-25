# imports
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.integrate import quad
from scipy.special import spherical_jn as jn

# some functions
def integrand(x,l):
  return jn(l,x) * x**2

def integrated(q,r1,r2,l):
  return (q**-3)*(quad(integrand,q*r1,q*r2, args=(l))[0])


# getting constants
ad = np.longdouble(0.32)
rm = np.longdouble(500)
o = np.longdouble(0.25)
ps = np.longdouble(0.0636305)

# getting vectors
q = list(range(5,500))
for i in range(len(q)):
    q[i] = np.longdouble(q[i]/1000)

r = list(range(100,2000))

# dim Z
z = []
with open('z.txt', 'r') as f:
    for i in f:
        z.append(float(i))

d = []
with open('d.txt', 'r') as f:
    for i in f:
        d.append(float(i))

m = []
with open('m.txt', 'r') as f:
    for i in f:
        m.append(float(i))

# dim S
s = []
with open('s.txt', 'r') as f:
    for i in f:
        s.append(float(i))

t = []
with open('t.txt', 'r') as f:
    for i in f:
        t.append(float(i))

# generating F0

# generating D, M, O, T

# generating H0 and K0

# generating Ihom

# generating ihom and fhom

# plotting ihom and fhom