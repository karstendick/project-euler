#Project Euler problem #31

def p(n):
    return 1
def tp(x):
    if x >= 0:
        return tp(x-2) + p(x)
    return 0
def n(x):
    if x >= 0:
        return n(x-5) + tp(x)
    return 0
def d(x):
    if x >= 0:
        return d(x-10) + n(x)
    return 0
def td(x):
    if x >= 0:
        return td(x-20) + d(x)
    return 0
def c(x):
    if x >= 0:
        return c(x-50) + td(x)
    return 0
def lb(x):
    if x >= 0:
        return lb(x-100) + c(x)
    return 0
def lb2(x):
    if x >= 0:
        return lb2(x-200) + lb(x)
    return 0

print lb2(200)

