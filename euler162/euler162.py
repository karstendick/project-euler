#PE #162

from copy import deepcopy

N = 16

def nums(N):
    p = [13,1,1,0,0,0,0,0]
    n = deepcopy(p)

    for i in range(1,N):
        n[0] = 13*p[0]
        n[1] = 14*p[1] + p[0]
        n[2] = 14*p[2] + p[0]
        n[3] = 15*p[3] + p[1] + p[2]
        n[4] = 14*p[4] + p[0]
        n[5] = 15*p[5] + p[1] + p[4]
        n[6] = 15*p[6] + p[2] + p[4]
        n[7] = 16*p[7] + p[3] + p[5] + p[6]

        p = deepcopy(n)

    return p[7]

s = 0
for i in range(1,N+1):
    s += nums(i)
    print i,nums(i)

print s
print hex(s)
hs = str(hex(s)).upper()[2:-1]
print hs

