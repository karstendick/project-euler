#Project Euler problem #92

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
def link(n):
    digits = [int(c) for c in str(n)]
    return sum(d*d for d in digits)

@memoize
def end89(n):
    if n == 1:
        return 0
    if n == 89:
        return 1
    return end89(link(n))

N = 10**7
#N = 10**5

count = 0
for n in xrange(1,N):
    count += end89(n)

print count
