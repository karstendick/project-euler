# PE 243

from fractions import gcd as fgcd
from fractions import Fraction

def memoize(fn):
    memo={}
    def memoizer(*param_tuple, **kwds_dict):
        if kwds_dict:
            return fn(*param_tuple, **kwds_dict)
        try:
            try:
                return memo[param_tuple]
            except KeyError:
                memo[param_tuple] = result = fn(*param_tuple)
                return result
        except TypeError:
            return fn(*param_tuple)
    return memoizer

@memoize
def gcd(a,b):
    return fgcd(a,b)

@memoize
def phi(n):
    s = 0
    for i in range(n):
        if gcd(n,i) == 1:
            s += 1
    return s

def R(n):
    return Fraction(phi(n),(n-1))

#MAXR = Fraction(4,10)
MAXR = Fraction(15499,94744)
MIN = 10**4
MAX = 10**5 #This won't run in the allotted time

for i in range(MIN,MAX):
    if R(i) < MAXR:
        print (i, R(i))
        break

print('done')
