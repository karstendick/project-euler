#Project Euler problem #30

##def sumof5s(n):
##    return sum([int(c)**5 for c in str(n)])
    
ub = 200000
#ub = 10000

print sum([i for i in range(10,ub) if i == sum([int(c)**5 for c in str(i)])])
print [i for i in range(10,ub) if i == sum([int(c)**5 for c in str(i)])]
##s=0
##for i in range(10,ub):
##    if i == sumof5s(i):
##        s += i
##
##print s
