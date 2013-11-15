#PE 75

from fractions import gcd
from collections import defaultdict

MAXL = 1500000

d = defaultdict(int)

for m in range(1,2+MAXL//2,1):
    for n in range(1+(m%2),m,2):
        if m*(m+n) > MAXL:
            break
        if gcd(m,n) == 1:
            for k in range(1, 2+MAXL//(m*(m+n)),1):
                p = 2*k*m*(m+n)
                if p > MAXL:
                    break
                d[p] += 1

#print(len(d))

total=0
for key in d.keys():
    if d[key] == 1 and key<=MAXL:
        total += 1

print(total)
