#Project Euler problem #53
from math import factorial

def C(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

count = 0
for n in range(1,101):
    for r in range(0,n+1):
        if C(n,r) > 1000000:
            count += 1

print count
