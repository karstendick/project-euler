#PE #38

# Answer not in 'i' range of [9,98] or [918,987]

MIN = 9182
MAX = 9876
cand = 2#918273645 #An example given
pand = sorted("123456789")

def concat(L):
    return ''.join(map(str,L))

for i in xrange(MIN,MAX+1):
    if str(i)[0] != '9':
        continue
    prods = []
    for n in xrange(1,10):
        prods.append(n*i)
        str_prods = concat(prods)
        if len(str_prods) > 9:
            break
        if sorted(str_prods) == pand:
            print str_prods
            cand = max(cand,int(''.join(str_prods)))

print "Done:\t", cand
