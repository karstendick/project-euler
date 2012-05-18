#Project Euler problem #41

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

N = 10**7
P = primes_less_than(N)
print len(P)

##P = []
##for line in open('primes50000.txt','r'):
##    P += [int(x) for x in line.split()]
##    
###print len(P)
##
for p in P[10**4:]:
    L = [int(x) for x in sorted(str(p))]
    if L == range(1,8):
        print p
