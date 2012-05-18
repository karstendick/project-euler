#PE #78

##def memoize(fn):
##    memo={}
##    def memoizer(*param_tuple, **kwds_dict):
##        if kwds_dict:
##            return fn(*param_tuple, **kwds_dict)
##        try:
##            try:
##                return memo[param_tuple]
##            except KeyError:
##                memo[param_tuple] = result = fn(*param_tuple)
##                return result
##        except TypeError:
##            return fn(*param_tuple)
##    return memoizer
##
##
##@memoize
##def p(n):
##    sum = 0
##    for k in xrange(1,(n/2)+1):
##        sum += pi(k,n-k)
##    return sum+1
##
##@memoize
##def pi(k,n):
##    if (k > n):
##        return 0
##    if (k == n):
##        return 1
##    return pi(k+1,n) + pi(k,n-k)

d = 1000000

m=100000
p = [0]*(m+1)
p[0] = 1

for i in xrange(1,m+1):
    j=1
    k=1
    s=0
    while j>0:
        j = i-(3*k*k+k)/2
        if j>=0:
            s = s - ((-1)**k)*p[j]
        j = i-(3*k*k-k)/2
        if j>=0:
            s = s - ((-1)**k)*p[j]
        k += 1

    p[i] = s % d

print p[m]

##for e in p:
##    if e%1000000 == 0:
##        print "Found it: ", e

print p.index(0)

print "Done!"
