#Project Euler problem #23
import math

def abundants(N):
    return [i for i in range(12,N) if isabundant(i)]

def isabundant(N):
    return sum_divisors(N) > N

def sum_divisors(N):
    s=1
    for d in range(2,N):
        if N%d == 0:
            s += d
    return s

def sumof2a(N):
    global A
    for i in range(12,N/2+1):
        if i in A and N-i in A:
            return True
    return False

ub = 28123
#ub = 1000
A = abundants(ub)

s = sum(range(1,12))
for n in range(12,ub):
    if not sumof2a(n):
        s += n

print s
