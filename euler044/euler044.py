#Project Euler problem #44
import math
from itertools import combinations
from sys import exit


def binary_search(seq, t):
    min = 0; max = len(seq) - 1
    while 1:
        if max < min:
            return -1
        m = (min + max) / 2
        if seq[m] < t:
            min = m + 1
        elif seq[m] > t:
            max = m - 1
        else:
            return m


def pent(n):
    return n*(3*n-1)/2
def ispent(n):
    if n < 0:
        return 0
    if int(math.sqrt(24*n+1)) == math.sqrt(24*n+1):
        return 1
    else:
        return 0

N=10**4
P = [pent(n) for n in range(1,N+1)]
D = []

for pair in combinations(P,2):
    diff = pair[1] - pair[0]
    if binary_search(P, diff) != -1:
        if binary_search(P, pair[0]+pair[1]) != -1:
            print (diff,pair)
            exit()
            #D.append((diff, pair))
        #print diff

#print len(D)
    

###PP = [(x,y,x+y,math.abs(x-y)) for x in P for y in P]
##Psum = [(x+y)*ispent(x+y) for x in P for y in P]
##Pdiff = [abs(x-y)*ispent(abs(x-y)) for x in P for y in P]
##
##for i in range(len(Psum)):
##    if Psum[i] >0 and Pdiff[i]>0:
##        print i, Psum[i], Pdiff[i]
