#Project Euler problem #52


for i in range(10**5,10**6):
    if sorted(str(i)) == sorted(str(2*i)) \
       == sorted(str(3*i)) \
       == sorted(str(4*i)) \
       == sorted(str(5*i)) \
       == sorted(str(6*i)):
        print i
        break
