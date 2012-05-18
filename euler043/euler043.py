#PE #43

from itertools import permutations

def ltoi(L):
    tens = 1
    n = 0
    for l in reversed(L):
        n+= tens*l
        tens *= 10
    return n

digits = range(10)

mysum = 0

for p in permutations(digits):
    if p[0] == 0:
        continue
    if ltoi(p[7:10]) % 17 == 0\
    and ltoi(p[6:9]) % 13 == 0\
    and ltoi(p[5:8]) % 11 == 0\
    and ltoi(p[4:7]) % 7 == 0\
    and ltoi(p[3:6]) % 5 == 0\
    and ltoi(p[2:5]) % 3 == 0\
    and ltoi(p[1:4]) % 2 == 0:
        mysum += ltoi(p)

print "Done:\t", mysum
