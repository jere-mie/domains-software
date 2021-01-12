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

q = [j*(10**11) for j in q]
q = [j*(0.55) for j in q]
# q = [j*(0.15) for j in q]

I_mine = []
q_mine = list(range(1,501))
for i in range(len(q_mine)):
    q_mine[i] = np.longdouble(q_mine[i]/1000)

with open('iq.txt', 'r') as f:
    for i in f:
        I_mine.append(float(i))

# q_mine = [j*(10**10) for j in q_mine]

plt.plot(I, q)
plt.plot(q_mine, I_mine)

plt.yscale('log')
plt.xscale('log')
plt.savefig('iq-2.png')