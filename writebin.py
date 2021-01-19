import struct
import time
print("starting F")
f = open('data100.txt', 'r')
start = time.time()
F = f.read()
f.close()
F = F.split(' ')
F = F[0:len(F)-1]
for i in range(len(F)):
    F[i] = float(F[i])
print(time.time()-start)
print(len(F))
# print("Writing to binary now")

# with open('data100.dat', 'wb') as f:
#     for i in F:
#         f.write(struct.pack('f', i))

# print('done writing')