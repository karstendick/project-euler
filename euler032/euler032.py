#PE #32

MAXA = 10**3
MAXB = 10**4

S = set([])
pand = sorted("123456789")

for a in xrange(2,MAXA):
    for b in xrange(a,MAXB):
        p = a*b
        pab = sorted(''.join([str(a), str(b), str(p)]))
        if len(pab) > 9: #This is the key optimization
            break
        if pab == pand:
            S.add(p)


print "Done:\t",
ans = sum(S)
print ans
