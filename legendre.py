from matplotlib import pyplot as plt
# import scipy.special.eval_legendre as lg
from scipy.special import eval_legendre as lg
# print(lg)
from scipy.integrate import quad
import numpy as np

def integrand(x, l):
    return lg(l, x)

def element(l, ad):
    return pow((np.pi*(2*l+1)), (1.0/2.0))*(quad(integrand, np.cos(ad), 1, args=(l))[0])

def ele2(l, ad):
    return (pow(element(l,ad), 2))*(pow(ad, -1))

# with open('w.txt', 'w') as f:
#     for i in range(1, 11):
#         f.write(str(element(i, np.pi/2.0))+"\n")

a = []
b = []
for i in range(1,11):
    a.append(ele2(i, 0.025))
    b.append(i)
plt.plot(b, a)
print(a)
plt.savefig('lg.png')

# def integrated(q,r1,r2,l):
#   return (q**-3)*(quad(integrand,q*r1,q*r2, args=(l))[0])
