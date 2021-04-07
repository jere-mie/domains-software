import numpy as np

x1 = [0.1]
y1 = []
for i in range(15):
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
print(x1)
print(y1)
print(x2)
print(y2)
