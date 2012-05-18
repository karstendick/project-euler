#PE #58

def nrect(n,m):
    return n*(n+1)*m*(m+1)/4

MAX = 10**3
target = 2*10**6

dist = MAX
ans = 0

for n in xrange(1,MAX):
    for m in xrange(1,MAX):
        cand = nrect(n,m)
        if abs(target - cand) < dist:
            dist = abs(target - cand)
            ans = n*m
            #print (ans, n, m)

print (dist, ans)
