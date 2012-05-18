#PE #112

def isbouncy(n):
    s = str(n)
    return list(s) != sorted(s) and list(s) != sorted(s,reverse=True)

N = 10000000
count = 0

for i in range(1,N):
    if isbouncy(i):
        count += 1
        if count/(1.0*i) >= .99:
            print(count,i,count/(1.0*i))
            break
print 'Nope.'
