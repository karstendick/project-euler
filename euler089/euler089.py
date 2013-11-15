#PE 089

#DEBUG=True
DEBUG=False

R = {'I':1,
     'V':5,
     'X':10,
     'L':50,
     'C':100,
     'D':500,
     'M':1000}

def romanToInt(s):
    total = 0
    for i,ch in enumerate(s):
        if (ch=='I' and ('V' in s[i:] or 'X' in s[i:]))\
           or (ch=='X' and ('L' in s[i:] or 'C' in s[i:]))\
           or (ch=='C' and ('D' in s[i:] or 'M' in s[i:])):
            total -= R[ch]
            if DEBUG:
                print(' -', R[ch], end='', sep='')
        else:
            total += R[ch]
            if DEBUG:
                print(' +', R[ch], end='', sep='')
    return total



def intToRoman(n):
    RR = {v:k for k,v in R.items()}
    minusRR = {900:'CM',
               400:'CD',
               90:'XC',
               40:'XL',
               9:'IX',
               4:'IV',
          }
    RR.update(minusRR)
    s = ''
    while n>0:
        k = max(RR.keys())
        if n>=k:
            s += RR[k]
            n -= k
        else:
            del RR[k]
    return s

f = open('roman.txt', 'r')

assert romanToInt('MMCCCLXXXXIX') == 2399


MAX=10
numChars = 0
numMinChars = 0
maxNum = 0
i = 0
for line in f:
    line = line.strip() # Remove trailing \n
    numChars += len(line)
    intNum = romanToInt(line)
    minRoman = intToRoman(intNum)
    numMinChars += len(minRoman)
    if (intNum > maxNum):
        maxNum = intNum
    if len(line) < len(minRoman):
        print("Error: ", line, " = ", intNum, " -> ", minRoman)
    if not DEBUG:
        continue
    if len(line) > len(minRoman):
        print(line, ": ", intNum, " -> ", minRoman)
        i += 1
    if i >= MAX:
        break

print(numChars)
print(numMinChars)
print(numChars - numMinChars)


