from matplotlib import pyplot as plt
# import scipy.special.eval_legendre as lg
from scipy.special import eval_legendre as lg
# print(lg)
from scipy.integrate import quad
import numpy as np


# def eq26(ad, l):
#     return ((np.power((np.pi* ((2*l)+1) ), (1.0/2.0)))/l) * (np.cos(ad)*lg(l, np.cos(ad)) - lg(l+1, np.cos(ad)))

# def elem(ad, l):
#     return (np.power(np.abs(eq26(ad, l)),2) * np.power(ad, -1))

def integrand(x, l):
    return np.power(((2*l+1)/(4*np.pi)), 1.0/2.0) * lg(l, np.cos(x)) * np.sin(x)

def eq23(ad, l):
    return (2*np.pi)*(quad(integrand, 0, ad, args=(l))[0])

def elem(ad, l):
    return (np.power(np.abs(eq23(ad, l)),2) * np.power(ad, -1))

# f = open("lg.txt", 'w')
# ad = 0.5
# for i in range(1, 12):
#     f.write(f'{elem(ad, i)}\n')
# f.close()

a = []
b = []
for i in range(1,11):
    a.append(elem(0.5, i))
    b.append(i)
plt.plot(b, a)
print(a)
plt.savefig('lg.png')