# PE #124

from itertools import izip

def Rads(nmax):
    # calculate totient(n) for n=2..N
    N = nmax + 1
    rad = [1]*(N)
    for n in xrange(2, N):
        if rad[n] == 1:
            for k in xrange(n, N, n):
                rad[k] *= n
    return rad

def mycmp(x,y):
    if x[0] < y[0]:
        return -1
    if x[0] > y[0]:
        return 1
    return cmp(x[1],y[1])

MAX = 10**5
rads = Rads(MAX)

#print rads[-10:]

##for i in izip(xrange(MAX+1), rads):
##    print i

L = zip(rads, xrange(MAX+1))

#print L[-10:]

L.sort(mycmp)

#print L[-10:]

print L[10**4]
