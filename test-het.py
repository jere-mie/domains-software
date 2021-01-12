# imports
import numpy as np
from matplotlib import pyplot as plt
import time

# getting constants
# rm = np.longdouble(300)
# o = np.longdouble(0.25)
ps = np.longdouble(0.181)

# getting vectors
q = list(range(1,501))
for i in range(len(q)):
    q[i] = np.longdouble(q[i]/1000)

r = list(range(100,2000))

w = []
with open('w2.txt', 'r') as f:
    for i in f:
        w.append(float(i))


# dim Z
z = []
with open('data2/z.txt', 'r') as f:
    for i in f:
        z.append(float(i))

d = []
with open('data2/d.txt', 'r') as f:
    for i in f:
        d.append(float(i))

m = []
with open('data2/m.txt', 'r') as f:
    for i in f:
        m.append(float(i))

# dim S
s = []
with open('data2/s.txt', 'r') as f:
    for i in f:
        s.append(float(i))

t = []
with open('data2/t.txt', 'r') as f:
    for i in f:
        t.append(float(i))


print("starting F")
f = open('data100.txt', 'r')
start = time.time()
F = f.read()
f.close()
F = F.split(' ')
F = F[0:len(F)-1]
for i in range(len(F)):
    F[i] = float(F[i])
F = np.array(F).reshape(len(w)+1,len(q),len(r))
F = F[1:]
print('done with F')

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

# now we get into the fun stuff
Wp = []
for i in range(len(F)):
    Wp.append(F[i].dot(Omat))
Wp = np.array(Wp)

print(Wp.shape)
# LQS
Wp = np.swapaxes(Wp, 0, 2)
# SQL
print(Wp.shape)

# # LQS
# Wp = np.swapaxes(Wp,0,1)
# # QLS
# Wp = np.swapaxes(Wp,0,2)
# # SLQ
# Wp = np.swapaxes(Wp,1,2)
# # SQL

# Wp = |Wp^2|
for i in range(len(Wp)):
    for j in range(len(Wp[0])):
        for k in range(len(Wp[0][0])):
            Wp[i][j][k] = np.abs(Wp[i][j][k]**2)

# dotting each QL sub matrix by the L vector (w)
Imon = []
for i in range(len(Wp)):
    Imon.append(Wp[i].dot(w))

Imon = np.array(Imon)
# SQ
print(Imon.shape)
Imon = np.swapaxes(Imon,0,1)
# QS
print(Imon.shape)
# QS dot S = Q
ipoly = Imon.dot(s)

plt.figure(3)
plt.plot(q, ipoly)
plt.yscale('log')
plt.xscale('log')
plt.savefig('imon.png')

with open('test-het.txt', 'w') as file:
    for i in ipoly:
        file.write(f'{i}\n')