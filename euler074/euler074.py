#Project Euler problem #74

from math import factorial

def link(n):
    digits = [int(x) for x in str(n)]
    return sum([factorial(d) for d in digits])

def numlinks(n):
    L = []
    count = 0
    while n not in L:
        L.append(n)
        n = link(n)
        count +=1
    return count


N = 10**6

count = 0
for n in range(1,N):
    if numlinks(n) == 60:
        count +=1

print count
