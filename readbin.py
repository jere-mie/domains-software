import struct
import numpy as np
import time

F = np.zeros(95000000)
start = time.time()
with open('data100.dat', 'rb') as f:
    for i in range(95000000):
        F[i] = struct.unpack('f', f.read(4))[0]
F = F.reshape(100, 1900, 500)
print(time.time()-start)
print(type(F[0]))


# start = time.time()
# with open('data100.dat', 'rb') as f:
#     buffer = f.read()

# for i in range(95000000):
#     F.append(struct.unpack('f', buffer[i*4:(i+1)*4])[0])
# print(time.time()-start)
# print(type(F[0]))