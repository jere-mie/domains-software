import time
f = open('data2.txt', 'r')
start = time.time()
a = f.read()
f.close()
# print(a[0:100])
a = a.split(' ')
a = a[0:len(a)-1]
for i in range(len(a)):
    a[i] = float(a[i])
    if i%100000==0:
        print(i)
print(time.time()-start)
print(a[0:3])
print(len(a))
# [10083.338568776844, 10284.65219319752, 10487.945239143999]