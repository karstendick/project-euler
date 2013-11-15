#PE 68

from itertools import permutations

#First, solve it for the magic 3-gon with 6 elements
def solSet6(p):
    return [p[3],p[0],p[1],
            p[4],p[1],p[2],
            p[5],p[2],p[0]]

def filterfn6(p):
    return min(p[3],p[4],p[5]) == p[3]


l6 = range(1,7)
sols6 = []

for p in permutations(l6):
    sum1 = p[3]+p[0]+p[1]
    sum2 = p[4]+p[1]+p[2]
    sum3 = p[5]+p[2]+p[0]
    if (sum1 == sum2 and sum2 == sum3):
        sols6.append(p)

sols6 = list(filter(filterfn6, sols6))
sols6 = list(filter(lambda s: len(s)==6, sols6))
mapSols6 = list(map(solSet6, sols6))
ans6 = sorted(mapSols6,reverse=True)[0]
ansStr6 = ''.join([str(c) for c in ans6])
print(ansStr6)

#Next, solve it for the magic 5-gon with 10 elements
def solSet10(p):
    return [p[5],p[0],p[1],
            p[6],p[1],p[2],
            p[7],p[2],p[3],
            p[8],p[3],p[4],
            p[9],p[4],p[0]]

def filterfn10(p):
    return min(p[5:10]) == p[5]

l10 = range(1,11)
sols10 = []

for p in permutations(l10):
    sum1 = p[5]+p[0]+p[1]
    sum2 = p[6]+p[1]+p[2]
    sum3 = p[7]+p[2]+p[3]
    sum4 = p[8]+p[3]+p[4]
    sum5 = p[9]+p[4]+p[0]
    if(len(set([sum1,sum2,sum3,sum4,sum5])))==1:
        sols10.append(p)

#60: print(len(sols10))
print(len(sols10))
print()
sols10 = list(filter(filterfn10, sols10))
print(len(sols10))
print(sols10)
print()
##sols10 = list(filter(lambda s: len(s)==16, sols10))
##print(len(sols10))
##print()
mapSols10 = list(map(solSet10, sols10))
print(len(sols10))
print()
ans10 = sorted(mapSols10, reverse=True)[0]
ansStr10 = ''.join([str(c) for c in ans10])
print(ansStr10)
