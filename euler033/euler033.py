#Project Euler problem #33


for j in range(10,100):
    for i in range(10,j):
        if i%10==0 or j%10==0:
            continue
        if i%10==j/10:
            p = i/10
            q = j%10
            if i*q == j*p:
                print (i,j), '==', (p,q)
        if i/10==j%10:
            p = i%10
            q = j/10
            if i*q == j*p:
                print (i,j), '==', (p,q)
