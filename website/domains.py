import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def generate(F, r, q, path, rm, o, ps, ad):
    F0 = F[0]
    # open txt files from path
    z = []
    with open(f'{path}/z.txt', 'r') as f:
        for i in f:
            z.append(float(i))
    d = []
    with open(f'{path}/d.txt', 'r') as f:
        for i in f:
            d.append(float(i))
    m = []
    with open(f'{path}/m.txt', 'r') as f:
        for i in f:
            m.append(float(i))
    s = []
    with open(f'{path}/s.txt', 'r') as f:
        for i in f:
            s.append(float(i))
    t = []
    with open(f'{path}/t.txt', 'r') as f:
        for i in f:
            t.append(float(i))
    w = []
    with open(f'{path}/w.txt', 'r') as f:
        for i in f:
            t.append(float(i))

    # generate matrices from them
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

    # generating H0 and K0
    H0 = F0.dot(Tmat)
    K0 = F0.dot(Omat)

    # generating Ihom
    Ihom = np.zeros(len(H0)*len(H0[0])).reshape(len(H0),len(H0[0]))
    s = np.array(s)

    sqrpi = np.longdouble(np.sqrt(np.pi))
    sqrpiby2 = np.longdouble(sqrpi*2)

    for i in range(len(H0)):
        for j in range(len(H0[0])):
            p1 = np.longdouble(sqrpiby2*H0[i][j])
            p2 = 2*ad*sqrpi
            p2*=K0[i][j]
            psum = p1+p2
            Ihom[i][j] = np.longdouble(np.power(psum,2))

    # generating ihom and fhom
    ihom = Ihom.dot(s)

    fhom = np.zeros(len(ihom))
    for i in range(len(Ihom)):
        fhom[i] = np.longdouble(0)
        for j in range(len(Ihom[i])):
            fhom[i]+=(s[j]*np.sqrt(Ihom[i][j]))    

    # plotting ihom and fhom
    plt.figure(0)
    plt.plot(q, fhom)
    plt.savefig(f'{path}/fhom.png')

    plt.figure(1)
    plt.plot(q,ihom)
    plt.yscale('log')
    plt.xscale('log')
    plt.savefig(f'{path}/ihom.png')

    plt.figure(2)
    plt.plot(q[70:], fhom[70:])
    plt.savefig(f'{path}/fhom2.png')
    print("hi")
    plt.close('all')