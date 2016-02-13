# PE 90

from itertools import combinations, product

# all 210 ways to paint a cube with the numbers 0..9
l = [c for c in combinations(range(10),6)]

# all 44,100 ways to paint both cubes
p = list(product(l, repeat=2))


def pairToSets(pair):
    (left, right) = pair
    return (set(left), set(right))

squares = [[0,1],
           [0,4],
           [0,9],
           [1,6],
           [2,5],
           [3,6],
           [4,9],
           [8,1]]

def digitInSet(s, digit):
    if (digit==6 or digit==9) and ((6 in s) or (9 in s)):
        theseDigits = s | set([6,9])
    else:
        theseDigits = s
    return digit in theseDigits

def canDisplayOrdered(left, right, square):
    (leftDigit, rightDigit) = square
    return digitInSet(left, leftDigit) and digitInSet(right, rightDigit)

def canDisplay(left, right, square):
    return canDisplayOrdered(left, right, square) or canDisplayOrdered(right, left, square)

def canDisplayAll(pair):
    (left, right) = pairToSets(pair)
    for square in squares:
        if not canDisplay(left, right, square):
            return False
    return True

count = 0
for pair in p:
    if canDisplayAll(pair):
        count += 1

print count/2


