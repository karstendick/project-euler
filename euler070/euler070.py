#PE #70

from sys import exit
from copy import deepcopy


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

def ispermut(a,b):
    return sorted(str(a)) == sorted(str(b))


MAX = 4*10**7

min_ratio = 6
min_n = 0
min_phi = 0

phis = totients(MAX)

exit()

phis2 = deepcopy(phis)
phis3 = deepcopy(phis)

##print phis[87109]
##
##exit(0)

for n in xrange(2,MAX):
    if ispermut(n, phis[n]):
        cand_ratio = n*1./phis[n]
        if cand_ratio < min_ratio:
            min_ratio = cand_ratio
            min_n = n
            min_phi = phis[n]
            print min_n, min_phi, min_ratio

print min_n, min_ratio
