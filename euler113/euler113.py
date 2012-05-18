#PE #113

from copy import deepcopy

N = 100


#numbers with N digits that are increasing
def inc(N):
    p = [1]*9
    n = deepcopy(p)
    for i in range(1,N):
        for j in range(1,10):
            n[j-1] = sum(p[0:j])
        p = deepcopy(n)

    return sum(p) - 9

#numbers with N digits that are increasing
def dec(N):
    p = [1]*10
    p[0] = 0
    n = deepcopy(p)
    for i in range(1,N):
        for j in range(10):
            n[j] = sum(p[j:10])
        p = deepcopy(n)

    return sum(p) - 9

#numbers with N digits that are all the same, e.g. 111, 222, ..., 999
def rep(N):
    return 9

N = 100
count = 0 # non-bouncy nums
for i in range(1,N+1):
    count += inc(i) + dec(i) + rep(i)

print count
