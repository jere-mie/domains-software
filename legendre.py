from matplotlib import pyplot as plt
from scipy.special import eval_legendre as lg
from scipy.integrate import quad
import numpy as np


# equation 23 in its 2 forms

def integrand1(theta, l):
    return np.power(((2.0*l + 1)/(4.0*np.pi)), 1.0/2.0)*lg(l, np.cos(theta))*np.sin(theta)

def e23_1(l, ad):
    return (2*np.pi)*(quad(integrand1, 0, ad, args=(l))[0])

def integrand2(x, l):
    return lg(l, x)

def e23_2(l, ad):
    return np.power((np.pi*(2*l+1)), (1.0/2.0))*(quad(integrand2, np.cos(ad), 1, args=(l))[0])

# equation 26 function

def e26(l, ad):
    a = (np.power(np.pi*(2.0*l + 1.0), (1.0/2.0)))/np.float(l)
    b = np.cos(ad)*lg(int(l), np.cos(ad))
    c = lg(int(l+1), np.cos(ad))
    return a*(b-c)





def y(l, alphad, ad):
    # return (abs(e26(l, ad))**2)/float(ad)
    # return (abs(e23_1(l, ad))**2)/float(ad)
    return (abs(e23_2(l, alphad))**2)/ad

def alpha(n, ad):
    return (np.arccos(1-((2.0*ad)/n)))

a = []
b = []
f = open("w.txt", "w")
for i in range(0,20):
    a.append(y(i, alpha(1, 0.4), 0.4))
    f.write(str(y(i, alpha(1, 0.4), 0.4))+'\n')
    b.append(i)
plt.plot(b, a)
print(a)
plt.savefig('lg.png')