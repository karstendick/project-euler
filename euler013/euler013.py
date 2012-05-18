#Project Euler problem #13

f=open("euler013_input.txt","r")
print f

sum=0
for line in f:
    sum+=int(line)

print sum
print str(sum)[0:10]
