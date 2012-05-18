#Project Euler problem #234

import math

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

def primes_less_than(N):
    primes = [x for x in (2,3,5,7,11,13) if x < N]
    if N<=17: return primes

    candidates = [x for x in xrange((N-2)|1,15,-2)
                  if x%3 and x%5 and x%7 and x%11 and x%13]
    top=int(N**0.5)
    while(top+1)*(top+1) <= N:
        top += 1

    while True:
        p = candidates.pop()
        primes.append(p)
        if p > top:
            break
        candidates = filter(p.__rmod__, candidates)

    candidates.reverse()
    primes.extend(candidates)
    return primes


##
##def isprime(n):
##    i=2
##    while i<=n**0.5:
##    #for i in range(2,int(n**0.5)+1):
##        if n%i == 0:
##            return False
##        i+=1
##    return True
##    
###@memoize
##def lps(n):
##    """lower prime square root"""
##    i=int(n**0.5)
##    while i>=2:
##    #for i in range(int(n**0.5),1,-1):
##        if isprime(i):
##            return i
##        i-=1
##
###@memoize
##def ups(n):
##    """upper prime square root"""
##    i=int(math.ceil(n**0.5))
##    while True:
##    #for i in range(int(math.ceil(n**0.5)),n):
##        if isprime(i):
##            return i
##        i+=1

def xor(a,b):
    return (a or b) and not(a and b)

#N=999966663333
#N=1000004
N=math.ceil(15**0.5)
P=primes_less_than(N)
sum=0
##i=4
##while i<N+1:
##    if xor(i%lps(i)==0, i%ups(i)==0):
##        sum+= i
##    i+=1
##print sum

count=0
for k in range(len(P)-1):
    for i in range(P[k]**2+1,P[k+1]**2):
        if xor(i%P[k]==0, i%P[k+1]==0):
            print i,count
            sum += i
            count += 1

print sum












