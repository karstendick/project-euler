#PE #49

from itertools import combinations

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

def canonical(n):
    a = []
    for i in range(4):
        a.append(n % 10)
        n /= 10
    a.sort()
    return tuple(a)
        
        

allP = primes_less_than(10**4)
P = [p for p in allP if p >= 1000]

d = {}

for p in P:
    pdigits = canonical(p)
    if pdigits in d:
        d[pdigits].append(p)
    else:
        d[pdigits] = [p]

print len(d)

for (k,v) in d.items():
    if len(v) < 3:
        del d[k]

print len(d)


for (k,v) in d.items():
    for trip in combinations(v,3):
        if trip[2] - trip[1] == trip[1] - trip[0]:
            print trip
