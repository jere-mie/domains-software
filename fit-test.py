import numpy as np
# import scipy as sp
from scipy.stats import chisquare
import time
# modified binary search where we only care about matching the element most close to 'x' within a threshhold
def f_bs(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0 
    while low <= high: 
        mid = (high + low) // 2
        if abs(arr[mid]-x) < 0.05:
            return mid
        elif arr[mid] < x:
            low = mid + 1 
        else:
            high = mid - 1
    return -1

# uses f_bs to transform a larger array into a wanted x range
def change_x(x_old, y_old, x_wanted):
    return [y_old[f_bs(x_old, i)] for i in x_wanted]


if __name__ == "__main__":
    x1 = [0.1]
    y1 = []
    for i in range(17):
        x1.append(x1[-1]+0.1)
    for i in x1:
        y1.append(i*3)

    x2 = [0.3]
    y2 = []
    for i in range(5):
        x2.append(x2[-1]+0.3)
    for i in x2:
        y2.append(i*3)

    # x1 = 0.1, 0.2, 0.3, ...
    # y1 = 0.3, 0.6, 0.9, ...
    # x2 = 0.3, 0.6, 0.9, ...
    # y2 = 0.9, 1.8, 2.7, ... 

    # print(change_x(x1, y1, x2))
    # res = change_x(x1, y1, x2) # fitting the function to desired x range

    # the lower, the better the fit
    # print(chisquare(y2, f_exp=res)[0]) 
    # print(chisquare([1,2,3,4,5,6], f_exp=[6,5,4,3,2,1])[0])

    start = time.time()
    a1 = [3,6,9,12,15,18,21]
    a2 = [1,2,3,4,5,6,7]

    min = 9999
    best = 0
    for i in range(1,4):
        res = [j*i for j in a2]
        goodness = chisquare(a1, f_exp=res)[0]
        if goodness < min:
            min = goodness
            best = i
    print(best)
    print(time.time()-start)