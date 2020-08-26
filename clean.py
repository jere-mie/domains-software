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
q = [10**-1] + list(range(5,510))
for i in range(len(q)):
    q[i] = np.longdouble(q[i]/1000)

# q = []
# with open('q.txt', 'r') as f:
#     for i in f:
#         q.append(float(i))

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
F0 = np.zeros(len(q)*len(r)).reshape(len(q),len(r))
for i in range(len(q)):
    for j in range(len(r)):
        F0[i][j] = np.longdouble(integrated(q[i], r[j], r[j]+1, 0))

# generating D, M, O, T
Dmat = np.full((len(r),len(s)), ps)
Mmat = np.full((len(r),len(s)), ps)

# Dmat stuff
for i in range(len(s)):
    for j in range(len(r)):
        if r[j] == t[i]+z[0]+1:
            for elem in d:
                Dmat[j][i] = elem
                j+=1

# Mmat stuff
for i in range(len(s)):
    for j in range(len(r)):
        if r[j] == t[i]+z[0]+1:
            for elem in m:
                Mmat[j][i] = elem
                j+=1
Omat = Dmat-Mmat
Tmat = Mmat - ps

# generating H0 and K0
H0 = F0.dot(Tmat)
K0 = F0.dot(Omat)

# generating Ihom
Ihom = np.zeros(len(H0)*len(H0[0])).reshape(len(H0),len(H0[0]))
s = np.array(s)

sqrpi = np.longdouble(np.sqrt(np.pi))
sqrpiby2 = np.longdouble(sqrpi/2)

for i in range(len(H0)):
  for j in range(len(H0[0])):
    p1 = np.longdouble(sqrpiby2*H0[i][j])
    p2 = 2*ad*sqrpi
    p2*=K0[i][j]
    psum = p1+p2
    Ihom[i][j] = np.longdouble(np.power(psum,2))

# generating ihom and fhom
ihom = Ihom.dot(s)

fhom = np.zeros(len(ihom))
for i in range(len(Ihom)):
  fhom[i] = np.longdouble(0)
  for j in range(len(Ihom[i])):
    fhom[i]+=(s[j]*np.sqrt(Ihom[i][j]))    

# plotting ihom and fhom
plt.figure(0)
plt.plot(q, fhom)
plt.savefig('fhom.png')

plt.figure(1)
plt.plot(q,ihom)
plt.yscale('log')
plt.xscale('log')
plt.savefig('ihom.png')

plt.figure(2)
plt.plot(q[70:], fhom[70:])
plt.savefig('fhom2.png')