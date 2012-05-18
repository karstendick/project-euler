#Project Euler problem #87

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


MAX = 5*10**7
POW4 = 85
POW3 = 369
POW2 = 7072


P4 = primes_less_than(POW4+1)
P3 = primes_less_than(POW3+1)
P2 = primes_less_than(POW2+1)

L = []

for p4 in P4:
    for p3 in P3:
        for p2 in P2:
            n = p4**4 + p3**3 + p2**2
            if n < MAX:
                L.append(n)

print len(set(L))





