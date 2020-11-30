from scipy.integrate import quad
from scipy.special import spherical_jn as jn
import numpy as np
import time

"""
November 30 Parameters For Reference:
R: 100-2000 (1900 elements)
q: 0.001-0.500 (500 elements)
l: 0-240 (250 elements)

"""

def integrand(x,l):
  return jn(l,x) * x**2

def integrated(q,r1,r2,l):
  return (q**-3)*(quad(integrand,q*r1,q*r2, args=(l))[0])

# a = []
# b = 0.01
# for i in range(75000000):
#     a.append(b)
#     if i%1000==0:
#       print(i)
#     b+=0.01
# print(len(a))
# start = time.time()
# for i in a:
#     c= integrated(i,100,101,0)
# # print(integrated(0.1,100,101,0))
# print(type(c))
# print((time.time()-start)/1000)
# while(True):
#     q = float(input('q: '))
#     r1 = int(input('r1: '))
#     r2 = int(input('r2: '))
#     l = int(input('l: '))
#     print(integrated(q,r1,r2,l))

z = []
rlower = int(input("R lower bound: "))
rupper = int(input("R upper bound: "))
rstep = int(input("R step: "))
numr = int(input("Number of R Elements: "))

qlower = float(input("Q lower bound: "))
qupper = float(input("Q upper bound: "))
qstep = float(input("Q step: "))
numq = int(input("Number of Q Elements: "))

llower = int(input("L lower bound: "))
lupper = int(input("L upper bound: "))
lstep = int(input("L step: "))
numl = int(input("Number of L Elements: "))

rl = rlower
ql = qlower
ll = llower

percentage=0
elems = 0

f = open('databig.txt', 'w')
start = time.time()
for i in range(numl):
  qlower = ql
  rlower = rl
  for j in range(numq):
    rlower = rl
    for k in range(numr):
      elems+=1
      # anumber = integrated(qlower,rlower,rlower+rstep,llower)
      f.write(str(integrated(qlower,rlower,rlower+rstep,llower))+' ')
      rlower+=rstep
    qlower+=qstep
  llower+=lstep
  print(f"{i+1} of {numl}")
print(time.time()-start)

print(f'{elems} elements')
f.close()
# while llower < lupper:
#   qlower = ql
#   rlower = rl
#   while qlower < qupper:
#     rlower = rl
#     while rlower < rupper:
#       z.append(integrated(qlower,rlower,rlower+rstep,llower))
#       # print('r')
#       rlower+=rstep
#     # print('q')
#     qlower+=qstep
#   percentage+=1
#   print(f'{percentage}% done')
#   llower+=lstep



# z = np.array(z)
# z.reshape()
# .reshape((rupper-rlower)/rstep, (qupper-qlower)/qstep, (lupper-llower)/lstep)
# print(z)
# zstr = str(z)
# f = open('matrix.txt', 'w')
# f.write(zstr)
# f.close()
# print(len(z))