# imports
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.integrate import quad
from scipy.special import spherical_jn as jn
import time

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
q = list(range(1,501))
for i in range(len(q)):
    q[i] = np.longdouble(q[i]/1000)

# q = []
# with open('q.txt', 'r') as f:
#     for i in f:
#         q.append(float(i))

r = list(range(100,2000))
# l = list(range(20))
# generating F0
# start = time.time()
# F0 = np.zeros(len(q)*len(r)).reshape(len(q),len(r))
# for i in range(len(q)):
#     for j in range(len(r)):
#         F0[i][j] = np.longdouble(integrated(q[i], r[j], r[j]+1, 0))
# print(time.time()-start)

f = open('databig.txt', 'r')
start = time.time()
F = f.read()
f.close()
# print(a[0:100])
F = F.split(' ')
F = F[0:len(F)-1]
for i in range(len(F)):
    F[i] = float(F[i])
F = np.array(F).reshape(20,500,1900)

F0 = F[0]



start = time.time()

l = []
with open('w.txt', 'r') as f:
    for i in f:
        l.append(float(i))


# dim Z
z = []
with open('data/z.txt', 'r') as f:
    for i in f:
        z.append(float(i))

d = []
with open('data/d.txt', 'r') as f:
    for i in f:
        d.append(float(i))

m = []
with open('data/m.txt', 'r') as f:
    for i in f:
        m.append(float(i))

# dim S
s = []
with open('data/s.txt', 'r') as f:
    for i in f:
        s.append(float(i))

t = []
with open('data/t.txt', 'r') as f:
    for i in f:
        t.append(float(i))


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
sqrpiby2 = np.longdouble(sqrpi*2)

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
print(f"{time.time()-start}s")

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
Wp = np.swapaxes(Wp,0,2)
Wp = np.swapaxes(Wp,1,2)
Imon = []
for i in range(len(Wp)):
    Imon.append(Wp[i].dot(l))
Imon = np.array(Imon)
print(Imon.shape)
Imon = np.swapaxes(Imon,0,1)
print(Imon.shape)
ipoly = Imon.dot(s)
print(ipoly.shape)
print(time.time()-start)

plt.figure(3)
plt.plot(q, ipoly)
plt.yscale('log')
plt.xscale('log')
plt.savefig('imon.png')
print(f"{time.time()-start}s")