import numpy as np


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

    print(change_x(x1, y1, x2))