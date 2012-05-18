#PE #50

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


def binary_search(seq, t):
    min = 0; max = len(seq) - 1
    while 1:
        if max < min:
            return -1
        m = (min + max) / 2
        if seq[m] < t:
            min = m + 1
        elif seq[m] > t:
            max = m - 1
        else:
            return m

def isprime(n):
    return (binary_search(P,n) != -1)

MAX = 10**6 #10**6

P = primes_less_than(MAX)

N = len(P)

maxnterms = 0
anssum = 0

for i in xrange(N):
    ssum = 0
    for j in xrange(i+1,N+1):
        ssum += P[j-1]
        #print (i,j), ssum

        if ssum >= MAX:     #This is the key optimization.
            break

        if (j-i) > maxnterms:
            if isprime(ssum):
                maxnterms = (j-i)
                anssum = ssum
                #print maxnterms, anssum

print maxnterms, anssum
