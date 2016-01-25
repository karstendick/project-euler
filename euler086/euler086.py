#PE #86

from gmpy2 import is_square

M = 100

def countPaths(M):
    total = 0
    for a in range(1, M+1):
        for b in range(a, M+1):
            for c in range(b, M+1):
                cand1 = (a + b)*(a + b) + c*c
                cand2 = (b + c)*(b + c) + a*a
                cand3 = (c + a)*(c + a) + b*b
                cand = min([cand1, cand2, cand3])
                if is_square(cand):
                    total += 1
    return total

def countPaths2(M):
    total = 0
    for n in range(1, M+1):
        for m in range(n+1, M+1):
            pass

print(99, countPaths(99))
print(100, countPaths(100))

