"""
info for next time:
~I need to loop through j and k and actually do the sum
~fred will give me the j and k vectors, you use these, calculate the angle between them,
    and use that for thetajk
~remember number of domains in alphad
~remember we want total ad, so ad per times the number of domains (in our case ad per is 0.05,
    so 2 domains is 0.1)
"""


"""
# code for angle between
import numpy as np
# from numpy import (array, dot, arccos, clip)
# from numpy.linalg import norm

u = np.array([1,2,3,4])
v = np.array([1,2,3,4])
c = np.dot(u,v)/np.linalg.norm(u)/np.linalg.norm(v) # -> cosine of the angle
angle = np.arccos(np.clip(c, -1, 1)) # if you really want the angle
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.special import eval_legendre as lg
import re

def e26(l, ad):
    a = (np.power(np.pi*(2.0*l + 1.0), (1.0/2.0)))/np.float(l)
    b = np.cos(ad)*lg(int(l), np.cos(ad))
    c = lg(int(l+1), np.cos(ad))
    return a*(b-c)

# n is number of domains
# ad is TOTAL domain area fraction
def alpha(n, ad):
    return (np.arccos(1-((2.0*ad)/n)))

# angle between two vectors, a and b
def angle(a, b):
    c = np.dot(a,b)/np.linalg.norm(a)/np.linalg.norm(b)
    return np.arccos(np.clip(c, -1, 1))


l = []
yaxis = []

# ad = float(input("total domain area fraction: "))
# ad = 0.05 times number of domains
domains = int(input("number of domains: "))
ad = 0.05*domains
ealpha = alpha(domains, ad)
vectors = []

with open('fig6-in.txt', 'r') as f:
    vect = []
    for i in f:
        vectors.append(re.findall("[\d.e-]+", i))
        vectors[-1] = [float(num) for num in vectors[-1]]
print(vectors)
f = open('fig6.txt', 'w')

for i in range(1, 15):
    tot = 0
    l.append(i)
    for j in range(domains):
        for k in range(domains):
            if j!=k:
                element = e26(i, ealpha)
                element = np.abs(element)**2
                ang = angle(vectors[j], vectors[k])
                element = element*lg(i, np.cos(ang))
                tot+=element
    yaxis.append(tot)
    f.write(f'{tot}\n')
f.close()
plt.plot(l, yaxis)
plt.savefig('fig6.png')
