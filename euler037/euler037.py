#Project Euler problem #37

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

def ltrunc(n):
    global P
    s = str(n)
    for c in s:
        s = s[1:]
        if s != '' and int(s) not in P:
            return False
    return s == ''

def rtrunc(n):
    global P
    s = str(n)
    for c in s:
        s = s[:-1]
        if s != '' and int(s) not in P:
            return False
    return s == ''



N = 10**6

P = primes_less_than(N)
T = []

for p in P[4:]:
    if ltrunc(p) and rtrunc(p):
        T.append(p)

print T
print sum(T)
