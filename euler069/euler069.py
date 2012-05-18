#PE #69

def totients(dmax):
    # calculate totient(n) for n=2..N
    N = dmax + 1; totient = range(N)
    for n in xrange(2, N):
        if totient[n] == n:
            for k in xrange(n, N, n):
                totient[k] *= (n - 1);
                totient[k] //=  n;
    # find number of reduced proper fraction
    #return sum(totient[2:])
    return totient


MAX = 10**6

max_ratio = 0
max_n = 0

phis = totients(MAX)

for n in xrange(2,MAX):
    cand_ratio = n*1./phis[n]
    if cand_ratio > max_ratio:
        max_ratio = cand_ratio
        max_n = n

print max_n, max_ratio
