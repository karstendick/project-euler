# PE 204

# Big help from "Enumerating and Counting Smooth Integers"
# by Daniel J. Bernstein
# https://cr.yp.to/papers/epsi.pdf
# I implement that paper's Algorithm 2

from copy import deepcopy

# all primes <= y for y-smooth integers
# for y=5
# primes = [2,3,5]
# for y=100
primes = [2,3,5,7,11,13,17,19,23,29,
          31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

# inclusive maximum
x = 10**9
#x = 162

S = deepcopy(primes)

for prime in primes:
    k = 1
    while True:
        cand = prime**(2**k)
        if cand <= x:
            S.append(cand)
            k += 1
        else:
            break
S = sorted(S)

print "Computed ", len(S), " elements of S"

ans = []
P = set([1])
D = set([])

for s in S:
    Q = set([])
    newP = deepcopy(P)
    for p in P:
        ps = p * s
        if ps <= x:
            Q.add(ps)
        else:
            newP.remove(p)
            D.add(p)
    P = newP.union(Q)
    if not P:
        print "The answer was D!"
        ans = D
        break
print "The answer is P U D"
ans = P.union(D)

print "len(ans): ", len(ans)


