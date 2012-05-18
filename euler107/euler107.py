#Project Euler problem #107

INF = 1000



C = []
#m = 0
total_cost = 0
for line in open('network_min.txt','r'):
    c = []
    for e in line.split(','):
        if e == '-' or e == '-\r\n' or e == '-\n':
            c.append(INF)
        else:
            c.append(int(e))
            total_cost += int(e)
    #m = max(m,max(c))
    C.append(c)
    
total_cost /= 2


min_cost = 0
n = len(C)
lowcost = [0 for x in range(n)]
closest = [0 for x in range(n)]

for i in range(2,n+1):
    lowcost[i-1] = C[1-1][i-1]
    closest[i-1] = 1
print 'lowcost:\t',lowcost
print 'closest:\t',closest

for i in range(2,n+1):
    mmin = lowcost[2-1]
    k = 2
    for j in range(3,n+1):
        if lowcost[j-1] < mmin:
            mmin = lowcost[j-1]
            k = j
    print k,closest[k-1]
    print 'cost:\t', C[k-1][closest[k-1]-1]
    
    min_cost += C[k-1][closest[k-1]-1]
    lowcost[k-1] = INF
    for j in range(2,n+1):
        if C[k-1][j-1] < lowcost[j-1] and lowcost[j-1] < INF:
            print 'INNER LOOP:\t',k,j
            lowcost[j-1] = C[k-1][j-1]
            closest[j-1] = k
    print 'lowcost:\t',lowcost
    print 'closest:\t',closest
print total_cost - min_cost
