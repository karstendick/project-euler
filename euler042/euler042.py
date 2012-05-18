#Project Euler problem #42
import math

def score(s):
    return sum([ord(c)-ord('A')+1 for c in s])
def istriangular(n):
    return int(math.sqrt(8*n+1)) == math.sqrt(8*n+1)

fin = open('words.txt','r')
words = [s.strip('\"') for s in fin.readline().split(',')]
values = [score(word) for word in words]
T = [v for v in values if istriangular(v)]
print len(T)
