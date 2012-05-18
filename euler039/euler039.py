#Project Euler problem #39
import math

Pmax = 1000
#Pmax = 100
PT = []

##for k in range(1,Pmax/2):
##    for n in range(1,Pmax):
##        for m in range(n+1,Pmax):
##            a = k*2*m*n
##            b = k*(m*m-n*n)
##            c = k*(m*m+n*n)
##            if a+b+c <= Pmax:
##                if a > b:
##                    PT.append((b,a,c))
##                else:
##                    PT.append((a,b,c))

for a in range(2,Pmax):
    for b in range(2,Pmax):
        for c in range(2,Pmax):
            if a+b+c <= Pmax and a*a+b*b == c*c:
                if a > b:
                    PT.append((b,a,c))
                else:
                    PT.append((a,b,c))



PT = sorted(set(PT))
print len(PT)
P=[sum(pt) for pt in PT]
print P
