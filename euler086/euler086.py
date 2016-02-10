#PE #86

from math import floor, sqrt
import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap

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

#from gmpy2 import is_square

def isqrt(n):
    return floor(sqrt(n))

@memoize
def is_square(n):
    return n == isqrt(n)**2

M = 100

@memoize
def countPath(ab, c):
    cand = ab*ab + c*c
    if is_square(cand):
        return 1
    else:
        return 0

@timing
def countPaths(M):
    total = 0
    for a in xrange(1, M+1):
        for b in xrange(a, M+1):
            for c in xrange(b, M+1):
                total += countPath(a+b, c)
                
                #cand = (a + b)*(a + b) + c*c
                
                #cand1 = (a + b)*(a + b) + c*c
                #cand2 = (b + c)*(b + c) + a*a
                #cand3 = (c + a)*(c + a) + b*b
                #cand = min([cand1, cand2, cand3])

                #if is_square(cand):
                #    total += 1
    return total

print(99, countPaths(99))
print(100, countPaths(100))


