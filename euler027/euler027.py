#Project Euler problem #27

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

def buildq(a,b):
    return lambda n: n*n+a*n+b

def num_primes(f):
    global P
    i=0
    while True:
        p=f(i)
        if p not in P:
            return i
        i+=1



N=2000000
M=1000
M=42
#M=100
P = primes_less_than(N)
B = primes_less_than(M)

A = range(M-1,2,-2)
##A.append(1)
##A = [0]
#f=buildq(1,41)

max_n=1
aa,bb=0,0
for a in A:
    for b in B:
        f = buildq(a,b)
        n = num_primes(f)
        if n>max_n:
            max_n,aa,bb=n,a,b
        f = buildq(-a,b)
        n = num_primes(f)
        if n>max_n:
            max_n,aa,bb=n,-a,b


print max_n,aa,bb


        

