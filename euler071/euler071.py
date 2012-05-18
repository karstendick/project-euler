#Project Euler problem #73
# Just compute all the mediants between 2/5 and 3/7

N = 1000000
count = 0

a,b,c,d = 2,5,3,7

while b+d<N:
    a,b = a+c,b+d
    count += 1

print "Answer: ", a

# Second attempts
##def farey( n, asc=True ):
##    """Python function to print the nth Farey sequence, either ascending or descending."""
##    if asc: 
##        a, b, c, d = 0, 1,  1  , n     # (*)
##    else:
##        a, b, c, d = 1, 1, n-1 , n     # (*)
##    #print "%d/%d" % (a,b)
##    while (asc and c < n) or (not asc and a > 0):
##        k = int((n + b)/d)
##        a, b, c, d = c, d, k*c - a, k*d - b
##        #print "%d/%d" % (a,b)
##        yield (a,b)

##for f in farey(N):
##    if f == (3,7):
##        print oldf
##        exit
##    oldf = f
##    count += 1


# First attempt
##from fractions import Fraction
##from fractions import gcd
###from bisect import *
##
##DMAX = 10000
###DMAX = 10000
##TARGET = 3.0/7.0
##candidate = 2.0/5.0
##
##answer = 0
##for d in xrange(1,DMAX+1):
##    for n in xrange(1,d):
##        if (candidate < (1.0*n)/d and (1.0*n)/d < TARGET):
##            candidate = (1.0*n)/d
##            if gcd(n,d) == 1:
##                answer = n
##
##
##
##print answer
