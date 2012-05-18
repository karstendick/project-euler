#Project Euler problem #22

def score(s):
    return sum([ord(c)-ord('A')+1 for c in s])
        

fin = open('names.txt', 'r')

names = sorted([s.strip('\"') for s in fin.readline().split(',')])

print sum([(i+1)*score(names[i]) for i in range(len(names))])
