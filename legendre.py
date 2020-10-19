# import scipy.special.eval_legendre as lg
from scipy.special import eval_legendre as lg
# print(lg)
from scipy.integrate import quad
import numpy as np

def integrand(x, l):
    return lg(l, x)

def element(l, ad):
    return pow((np.pi*(2*l+1)), (1.0/2.0))*(quad(integrand, np.cos(ad), 1, args=(l))[0])

with open('w.txt', 'w') as f:
    for i in range(1, 251):
        f.write(str(element(i, np.pi/2.0))+"\n")
# def integrated(q,r1,r2,l):
#   return (q**-3)*(quad(integrand,q*r1,q*r2, args=(l))[0])
