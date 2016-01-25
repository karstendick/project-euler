# PE #91

def pv(a1,a2,b1,b2):
    #print '[{} {}], [{} {}]'.format(a1,a2,b1,b2)
    pass

#N = 2
N = 50

count = 0
for a1 in range(N+1):
    for a2 in range(N+1):
        for b1 in range(N+1):
            for b2 in range(N+1):
                if a1==0 and a2==0:
                    pass
                elif b1==0 and b2==0:
                    pass
                elif a1==b1 and a2==b2:
                    pass
                elif 0 == a1*b1 + a2*b2:
                    count += 1
                    pv(a1,a2,b1,b2)
                elif 0 == a1*(a1-b1) + a2*(a2-b2):
                    count += 1
                    pv(a1,a2,b1,b2)
                elif 0 == b1*(a1-b1) + b2*(a2-b2):
                    count += 1
                    pv(a1,a2,b1,b2)

print "count: ", count/2
