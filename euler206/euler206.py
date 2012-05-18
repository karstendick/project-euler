#Project Euler problem #206

##def ismatch(n):
##    digits = [int(x) for x in str(n)]
##    return (digits[0] == 1 and
##            digits[2] == 2 and
##            digits[4] == 3 and
##            digits[6] == 4 and
##            digits[8] == 5 and
##            digits[10] == 6 and
##            digits[12] == 7 and
##            digits[14] == 8 and
##            digits[16] == 9)
def ismatch(n):
    if n%10 != 9:
        return False
    n/=100
    if n%10 != 8:
        return False
    n/=100
    if n%10 != 7:
        return False
    n/=100
    if n%10 != 6:
        return False
    n/=100
    if n%10 != 5:
        return False
    n/=100
    if n%10 != 4:
        return False
    n/=100
    if n%10 != 3:
        return False
    n/=100
    if n%10 != 2:
        return False
    n/=100
    if n%10 != 1:
        return False
    return True

lb = 101010101
ub = 138902662
#ub = lb+11010101

for n in xrange(lb, ub+1):
    if ismatch(n*n):
        print n, n*n

print 'Done!'
