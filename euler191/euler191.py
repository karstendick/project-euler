#PE problem #191

from copy import deepcopy

p = [1,0,0,0,0,0]
n = range(6)

for i in range(30):
    n = [sum(p[0:3]),p[0],p[1],sum(p),p[3],p[4]]
    p = deepcopy(n)

    print(i+1,sum(p),p)
