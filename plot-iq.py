import numpy as np
from matplotlib import pyplot as plt
import re

I = []
q = []

both = []

with open("fig4/ad001.dat", 'r') as f:
    for i in f:
        both.append(re.findall("[\d.e-]+", i))
        I.append(float(both[-1][0]))
        q.append(float(both[-1][1]))
# print(both)
# print(I[0])
# print(q[0])

plt.plot(I, q)
plt.yscale('log')
plt.xscale('log')
plt.savefig('iq.png')