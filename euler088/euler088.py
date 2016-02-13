#PE 088

kmax = 12000
n = [2*kmax]*kmax

def prodsum(p, s, c, start):
    k = p - s + c
    if k<kmax:
        if p<n[k]:
            n[k] = p
        for i in xrange(start, kmax//p * 2):
            prodsum(p*i, s+i, c+1, i)

prodsum(1, 1, 1, 2)

K = set(n[2:])
ksum = sum(K)


print ksum
