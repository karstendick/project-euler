#PE #158

from copy import deepcopy

def nstr(N):
    p = [1]*26 + [0]*26
    n = deepcopy(p)

    for i in range(1,N):
        print i-1,p
##        n[0] = sum(p[0:26])
##        n[1] = sum(p[1:26])
##        n[25] = sum(p[25:26])
        for j in range(26):
            n[j] = sum(p[j:26])

##        n[26] = sum(p[26:52]) + sum(p[0:0])
##        n[27] = sum(p[27:52]) + sum(p[0:1])
##        n[28] = sum(p[28:52]) + sum(p[0:2])
##        n[51] = sum(p[51:52]) + sum(p[0:25])
        for j in range(26):
            n[26+j] = sum(p[26+j:52]) + sum(p[0:j])

        p = deepcopy(n)
    print i,p

    return sum(p[26:52])


##L = map(nstr,range(1,27))
##print L
##print max(L)
