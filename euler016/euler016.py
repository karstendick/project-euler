#Project Euler problem #16

s = str(2**1000)
#print s

sum=0
for i in range(len(s)):
    sum += int(s[i])
    
