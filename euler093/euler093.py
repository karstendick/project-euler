# PE 093

import numbers
from itertools import permutations, product, combinations_with_replacement
from fractions import Fraction

digits = [1,2,3,4]
#digits = [2,9,5,7]
operators = ['+','-','*','/']

def genExp(ds, op, form):
    if form == 0:
        return [ds[0],ds[1],op[0],ds[2],op[1],ds[3],op[2]]
    elif form == 1:
        return [ds[0],ds[1],ds[2],op[0],op[1],ds[3],op[2]]
    elif form == 2:
        return [ds[0],ds[1],op[0],ds[2],ds[3],op[1],op[2]]
    elif form == 3:
        return [ds[0],ds[1],ds[2],op[0],ds[3],op[1],op[2]]
    elif form == 4:
        return [ds[0],ds[1],ds[2],ds[3],op[0],op[1],op[2]]
    raise IndexError

def genExps(digits):
    digitPerms = permutations(digits)
    opsCombs = product(operators,repeat=3)
    forms = range(5)
    return product(digitPerms, opsCombs, forms)

def evalExps(digits):
    for ge in genExps(digits):
        ds, ops, form = ge
        exp = genExp(ds, ops, form)
        value = evalPost(exp, digits)
        if value is None:
            #print ds, ops, form
            #print "exp: ", exp
            pass
        yield value
        

def isNum(n):
    return isinstance(n, numbers.Number)

def evalPost(exp, digits):
    stack = []
    while exp:
        x = exp.pop(0)
        #print "x: ", x, " exp: ", exp
        if x in digits:
            stack.append(Fraction(x))
        else:
            if len(stack) < 2:
                #print "a"
                return None
            right = stack.pop()
            left = stack.pop()
            
            # TODO: remove this? Seems unnecessary
#            if not isNum(left) or not isNum(right):
#                print "b"
#                return None

            if x == '+':
                value = left + right
            elif x == '-':
                value = left - right
            elif x == '*':
                value = left * right
            elif x == '/':
                if right == 0:
                    #print "div by 0!"
                    return None
                value = left / right
            else:
                #print "c"
                return None
            #print "value: ", value
            stack.append(value)
        #print "stack: ", stack
    if len(stack) == 1:
        value = stack.pop()
        if value.denominator == 1:
            return value.numerator
        else:
            return None
    else:
        #print "d"
        return None

#exp = [9,7,5,2,'-','-','-']
#print "ans: ", evalPost(exp, digits)

def calcValues(digits):
    values = set(evalExps(digits))
    values = [v for v in values if v is not None and v > 0]
    values = sorted(values)
    return values

def calcAllValues(digits):
    for v in evalExps(digits):
        if v is None:
            break

def findLongest(a):
    for i,e in enumerate(a):
        if e != i+1:
            return i
    return i

longest = 0

for a in xrange(1,7):
    print "a: ", a
    for b in xrange(2,8):
        print "b: ", b
        for c in xrange(3,9):
            for d in xrange(4,10):
                values = calcValues([a,b,c,d])
                cand = findLongest(values)
                if cand > longest:
                    longest = cand
                    ans = [a,b,c,d]
                    print longest, ans

print "All done!"
print longest
print ans









