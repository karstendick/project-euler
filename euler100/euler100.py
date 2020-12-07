nmin, nmax = 10**12, 10**13
nmin, nmax = 1, 10**6

for n in range(nmin, nmax):
    bmin = int(n * 0.6)
    bmax = int(n * 0.8)
    for b in range(bmin, bmax):
        if 2*b*(b-1) == n*(n-1):
            print(f"b: {b} | n: {n} | b/n: {b/n}")
            # break

print("All done!")
