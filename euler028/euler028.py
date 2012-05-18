#Project Euler problem #28
##import math
##
##def printspiral(a):
##    for i in range(len(a)):
##        print a[i]
##
##def newspiral(n):
##    a = []
##    for i in range(n):
##        a.append([])
##        for j in range(n):
##            a[i].append(0)    
##    return a
##
##def setspiral(a,i):
##    n
##
##a = newspiral(5)
##printspiral(a)

N=1001
s=1
for i in range(1,N//2+1):
   sq = (2*i+1)**2
   s += sq + sq-2*i + sq-4*i + sq-6*i

print s
