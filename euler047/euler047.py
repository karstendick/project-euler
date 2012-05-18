#Project Euler problem #47

def count_prime_factors(n):
    if n<2:
        return 0
    count=0
    d=2
    while n>1:
        if n%d == 0:
            count+=1
            while n%d == 0:
                n/=d
        d+=1
    return count


N=1000000
#C = [count_prime_factors(i) for i in range(N)]
C=[0,0,0,0]
for i in range(N-4):
    C[i%4] = count_prime_factors(i)
    if C == [4, 4, 4, 4]:
        print i
        break

##C=[0,0]
##for i in range(N-2):
##    C[i%2] = count_prime_factors(i)
##    if C == [2,2]:
##        print i
##        break
