#PE #164

from copy import deepcopy

p = [0]*100
p[1:10] = [1]*9

n = deepcopy(p)

for d in range(1,20):
    for i in range(10):
        for j in range(10):
            n[10*i+j] = 0
            for k in range(10-i-j):
                n[10*i+j] += p[k*10+i]

    p = deepcopy(n)

print sum(p)
