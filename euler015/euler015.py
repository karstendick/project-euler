#Project Euler problem #15

N=21

a = []
for i in range(N):
    a.append([0 for j in range(N)])

for i in range(N):
    a[0][i] = 1
    a[i][0] = 1

for i in range(N):
    for j in range(N):
        if a[i][j] == 0:
            a[i][j] = a[i-1][j] + a[i][j-1]

print a[N-1][N-1]
