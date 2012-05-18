#PE #178

# 169656501226L
# this is the sum of all the 40-digit strings

# P[dxy] stores the number of strings at the ith step that
# end in digit d
# have hit 0 if x=1
# have hit 9 if y=1

from copy import deepcopy


def nums(N):
    p = {}
    p['010'] = 0
    p['011'] = 0

    p['100'] = 1
    p['101'] = 0
    p['110'] = 0
    p['111'] = 0

    p['200'] = 1
    p['201'] = 0
    p['210'] = 0
    p['211'] = 0

    p['300'] = 1
    p['301'] = 0
    p['310'] = 0
    p['311'] = 0

    p['400'] = 1
    p['401'] = 0
    p['410'] = 0
    p['411'] = 0

    p['500'] = 1
    p['501'] = 0
    p['510'] = 0
    p['511'] = 0

    p['600'] = 1
    p['601'] = 0
    p['610'] = 0
    p['611'] = 0

    p['700'] = 1
    p['701'] = 0
    p['710'] = 0
    p['711'] = 0

    p['800'] = 1
    p['801'] = 0
    p['810'] = 0
    p['811'] = 0

    p['901'] = 1
    p['911'] = 0

    n = deepcopy(p)

    for i in range(1,N):
        n['010'] = p['100'] + p['110']
        n['011'] = p['101'] + p['111']

        n['100'] = p['200']
        n['101'] = p['201']
        n['110'] = p['010'] + p['210']
        n['111'] = p['011'] + p['211']

        n['200'] = p['100'] + p['300']
        n['201'] = p['101'] + p['301']
        n['210'] = p['110'] + p['310']
        n['211'] = p['111'] + p['311']

        n['300'] = p['200'] + p['400']
        n['301'] = p['201'] + p['401']
        n['310'] = p['210'] + p['410']
        n['311'] = p['211'] + p['411']

        n['400'] = p['300'] + p['500']
        n['401'] = p['301'] + p['501']
        n['410'] = p['310'] + p['510']
        n['411'] = p['311'] + p['511']

        n['500'] = p['400'] + p['600']
        n['501'] = p['401'] + p['601']
        n['510'] = p['410'] + p['610']
        n['511'] = p['411'] + p['611']

        n['600'] = p['500'] + p['700']
        n['601'] = p['501'] + p['701']
        n['610'] = p['510'] + p['710']
        n['611'] = p['511'] + p['711']

        n['700'] = p['600'] + p['800']
        n['701'] = p['601'] + p['801']
        n['710'] = p['610'] + p['810']
        n['711'] = p['611'] + p['811']

        n['800'] = p['700']
        n['801'] = p['701'] + p['901']
        n['810'] = p['710']
        n['811'] = p['711'] + p['911']

        n['901'] = p['800'] + p['801']
        n['911'] = p['810'] + p['811']

        p = deepcopy(n)

    s = p['011']+p['111']+p['211']+p['311']+p['411']+p['511'] \
          +p['611']+p['711']+p['811']+p['911']
    return s


##for i in range(10):
##    print "p[\'%d00\'] = 0" % i
##    print "p[\'%d01\'] = 0" % i
##    print "p[\'%d10\'] = 0" % i
##    print "p[\'%d11\'] = 0" % i
##    print
N = 40
s = 0
for i in range(1,N+1):
    s += nums(i)
    print i,s

print s
