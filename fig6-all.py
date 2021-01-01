import numpy as np
from matplotlib import pyplot as plt
from scipy.special import eval_legendre as lg
import re

l = list(range(1,15))
nums = []
with open('fig6-all.txt', 'r') as f:
    for i in f:
        nums.append(float(i))

for i in range(5):
    plt.plot(l, nums[14*i:14*(i+1)])
plt.savefig('fig6-all.png')
