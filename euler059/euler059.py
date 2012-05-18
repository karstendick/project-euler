#Project Euler problem #59
# ord, chr

def decrypt(key,text):
    pt = []
    for i,c in enumerate(text):
        pt.append(ord(c) ^ ord(key[i%3]))
    return ''.join([chr(j) for j in pt])

        

for line in open('cipher1.txt','r'):
    input = [chr(int(x)) for x in line.split(',')]

ct = ''.join(input)

for k1 in xrange(97,123):
    for k2 in xrange(97,123):
        for k3 in xrange(97,123):
            key = chr(k1) + chr(k2) + chr(k3)
            spt = decrypt(key,input)
            if spt.find('and') != -1:
                print key, ":\t", spt[:50]

print 'Done!'
