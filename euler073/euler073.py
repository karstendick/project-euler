#Project Euler problem #73

from fractions import Fraction
from fractions import gcd
#from bisect import *

#DMAX = 8
DMAX = 10000

L = []
count = 0
for d in xrange(1,DMAX+1):
    for n in xrange(1,d):
##        if (Fraction(1,3) < Fraction(n,d)
##            and Fraction(n,d) < Fraction(1,2)):
        if (1.0/3.0 < (1.0*n)/d and (1.0*n)/d < 0.5):
            if gcd(n,d) == 1:
                #insort(L,Fraction(n,d))
                count +=1

#print L

#start = bisect(L,Fraction(1,3))
#end = bisect(L,Fraction(1,2))

#print end-start-1
#print len(L)

print count
