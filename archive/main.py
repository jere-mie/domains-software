# imports section
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
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

F0 = F[0]

from omega import Omat, Tmat, ad, s, q
print(len(Omat))
print(len(Tmat))


H0 = F0.dot(Tmat)
K0 = F0.dot(Omat)
print("H0 and K0:")
print(H0.shape)
print(K0.shape)
print("")
Ihom = np.zeros(len(H0)*len(H0[0])).reshape(len(H0),len(H0[0]))
s = np.array(s)

sqrpi = np.sqrt(np.pi)
sqrpiby2 = sqrpi/2

for i in range(len(H0)):
  for j in range(len(H0[0])):
    p1 = sqrpiby2*H0[i][j]
    p2 = 2*ad*sqrpi
    p2*=K0[i][j]
    psum = p1+p2
    Ihom[i][j] = np.power(psum,2)
    # Ihom[i][j] = ((sqrpi*H0[i][j]) + ((2*ad*np.sqrt(np.pi))*K0[i][j]))**2
    # Ihom[i][j] = (((np.sqrt(np.pi)/2)*H0[i][j]) + ((2*ad*np.sqrt(np.pi))*K0[i][j]))**2
ihom = Ihom.dot(s)
print("ihom shape should be Q")
print(ihom.shape)

fhom = []
for i in range(len(Ihom)):
  fhom.append(0)
  for j in range(len(Ihom[i])):
    fhom[i]+=(s[j]*np.sqrt(Ihom[i][j]))    

fhom = np.array(fhom)
print("fhom shape should be Q")
print(fhom.shape)

df = pd.DataFrame(fhom)
filepath = 'fhom.xlsx'
df.to_excel(filepath, index=False)

# plotting stuff
qline = []
step = 0.005
for i in range(500):
  qline.append(step)
  step+=0.001

plt.figure(0)
plt.plot(qline[70:],fhom[70:])
# plt.yscale('log')
# plt.xscale('log')
plt.savefig('fhom.png')

plt.figure(1)
plt.plot(qline,ihom)
plt.yscale('log')
plt.xscale('log')
plt.savefig('ihom.png')

# matrix multiplication step

# Wp = []
# for i in range(len(F)):
#     Wp.append(F[i].dot(Omat))
# Wp = np.array(Wp)
# print(len(Wp))
# print(len(Wp[0]))
# print(len(Wp[0][0]))
# Wp = np.swapaxes(Wp,0,1)
# print()
# print(len(Wp))
# print(len(Wp[0]))
# print(len(Wp[0][0]))
# print(Wp.shape)
# for i in range(len(Wp)):
#     for j in range(len(Wp[0])):
#         for k in range(len(Wp[0][0])):
#             Wp[i][j][k] = np.abs(Wp[i][j][k]**2)