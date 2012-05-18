#PE #104

pand = sorted('123456789')

def ispand(s):
    return sorted(s) == pand

MAX = 10**5

fn1 = 1
fn2 = 1

for k in xrange(3,MAX+1):
    fn = fn1 + fn2
    #print fn

    s = str(fn)

##    if ispand(s[:9]):
##        print "front: ", k
##    if ispand(s[-9:]):
##        print "back:  ", k
    
    if ispand(s[-9:]) and ispand(s[:9]):
        print k
        break
    
    fn2 = fn1
    fn1 = fn
    
