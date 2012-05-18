#PE #62

def canonical(n):
    a = []
    while n>0:
        a.append(n % 10)
        n /= 10
    a.sort()
    return tuple(a)

N = 10**4

cubes = [n**3 for n in range(1,N+1)]

d = {}

for c in cubes:
    cdigits = canonical(c)
    if cdigits in d:
        d[cdigits].append(c)
    else:
        d[cdigits] = [c]

for (k,v) in d.items():
    if len(v) == 5:
        print v
