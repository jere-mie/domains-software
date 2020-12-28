"""
info for next time:
~I need to loop through j and k and actually do the sum
~fred will give me the j and k vectors, you use these, calculate the angle between them,
    and use that for thetajk
~remember number of domains in alphad
~remember we want total ad, so ad per times the number of domains (in our case ad per is 0.05,
    so 2 domains is 0.1)
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.special import eval_legendre as lg

def e26(l, ad):
    a = (np.power(np.pi*(2.0*l + 1.0), (1.0/2.0)))/np.float(l)
    b = np.cos(ad)*lg(int(l), np.cos(ad))
    c = lg(int(l+1), np.cos(ad))
    return a*(b-c)

def alpha(n, ad):
    return (np.arccos(1-((2.0*ad)/n)))

l = []
yaxis = []
# ad = float(input("total domain area fraction: "))
# TOTAL DOMAIN FRACTION
ad = 0.1
f = open('fig6.txt', 'w')
# NUMBER OF DOMAINS IS IMPORTANT
ealpha = alpha(2, ad)
for i in range(1,15):
    l.append(i)
    element = e26(i, ealpha)
    element = np.abs(element)**2
    element = element*lg(i, -1)
    element*=2
    yaxis.append(element)
    f.write(f'{element}\n')
f.close()
plt.plot(l, yaxis)
plt.savefig('fig6.png')