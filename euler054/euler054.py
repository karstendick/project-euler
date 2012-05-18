#Project Euler problem #54
#Poker!
#
#File contains no:
# Royal flush
# Straight flush
# Four of a kind
# Ace-low straight
#
# Only 2 full houses, both in h2.
# In each case, h2 wins anyway just for having trips.
#
# Only 2 flushes, one in each player's hand.
# Several straights, with 4 in h1.
# Some trips, but never in both hands at once.
#
# Many two pairs, but never in both hands at once.
#
# Lots of pairs, even in both hands.

from itertools import groupby

D={'T':10,'J':11,'Q':12,'K':13,'A':14}

def isflush(h):
    return all([h[i][1]==h[i+1][1] for i in range(len(h)-1)])

def isstraight(h):
    return h == range(h[0],h[0]+5)

def isfour(h):
    L = sorted([(len(list(g)),k) for k,g in groupby(h)])
    return any([l[0]==4 for l in L])

def isthree(h):
    L = sorted([(len(list(g)),k) for k,g in groupby(h)])
    return any([l[0]==3 for l in L])

def isfullhouse(h):
    L = sorted([len(list(g)) for k,g in groupby(h)])
    return L == [2,3]

def istwopair(h):
    return 2== len(filter(lambda x: x==2,[len(list(g)) for k,g in groupby(h)]))

def stripsuit(h):
    return sorted([int(D.get(c[0],c[0])) for c in h])

fin = open('poker.txt','r')

p1wins = 0
for line in fin:
    h1,h2 = line[:14].split(),line[15:].split()
    isf1,isf2 = map(isflush,[h1,h2])

    if isf1 or isf2:
        p1wins += isf1
        continue
    
    h1,h2 = map(stripsuit,[h1,h2])

    if isfullhouse(h2):
        continue

    if isstraight(h1) or isstraight(h2):
        p1wins += isstraight(h1)
        continue

    if isthree(h1) or isthree(h2):
        p1wins += isthree(h1)
        continue

    if istwopair(h1) or istwopair(h2):
        p1wins += istwopair(h1)
        continue

    Lh1 = sorted([(len(list(g)),k) for k,g in groupby(h1)],reverse=True)
    Lh2 = sorted([(len(list(g)),k) for k,g in groupby(h2)],reverse=True)

    p1wins += (Lh1 > Lh2)

print p1wins
