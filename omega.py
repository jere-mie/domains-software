import numpy as np
import pandas as pd
# declaring constants
rm = 500
o = 0.25
ps = 0.0636305

# declaring vectors

# dim Q
q = []
with open('q.txt', 'r') as f:
    for i in f:
        q.append(float(i))
# dim R
r = []
with open('r.txt', 'r') as f:
    for i in f:
        r.append(float(i))

# dim Z
z = []
with open('z.txt', 'r') as f:
    for i in f:
        z.append(float(i))

d = []
with open('d.txt', 'r') as f:
    for i in f:
        d.append(float(i))

m = []
with open('m.txt', 'r') as f:
    for i in f:
        m.append(float(i))

# dim S
s = []
with open('s.txt', 'r') as f:
    for i in f:
        s.append(float(i))

t = []
with open('t.txt', 'r') as f:
    for i in f:
        t.append(float(i))

# dim L
# l = []
# with open('l.txt', 'r') as f:
#     for i in f:
#         l.append(float(i))

# declaring matrices

Dmat = np.full((len(r),len(s)), ps)
Mmat = np.full((len(r),len(s)), ps)

# Dmat stuff
for i in range(len(s)):
    for j in range(len(r)):
        if r[j] == t[i]+z[0]+1:
            for elem in d:
                Dmat[j][i] = elem
                j+=1

# Mmat stuff
for i in range(len(s)):
    for j in range(len(r)):
        if r[j] == t[i]+z[0]+1:
            for elem in m:
                Mmat[j][i] = elem
                j+=1
Omat = Dmat-Mmat
Tmat = Mmat - ps

f = open('omat.txt', 'w')
f.write(str(Omat))
f.close()
for i in range(100):
    print(str(i+1)+' '+str(Tmat[i][0]))
print(Omat[57][0])
print(Omat[62][1])
f = open('Mmat.txt', 'w')
f.write(str(Mmat))
f.close()

# df = pd.DataFrame(Mmat)
# filepath = 'Mmat.xlsx'
# df.to_excel(filepath, index=False)

# df = pd.DataFrame(Dmat)
# filepath = 'Dmat.xlsx'
# df.to_excel(filepath, index=False)


# df = pd.DataFrame(Omat)
# filepath = 'Omat.xlsx'
# df.to_excel(filepath, index=False)

# df = pd.DataFrame(Tmat)
# filepath = 'Tmat.xlsx'
# df.to_excel(filepath, index=False)