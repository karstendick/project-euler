#Project Euler problem #17

def toword(n):
    lt20 = ['','one', 'two','three','four','five',
            'six','seven','eight','nine','ten',
            'eleven','twelve','thirteen','fourteen','fifteen',
            'sixteen','seventeen','eighteen','nineteen']
    tens = ['','','twenty','thirty','forty','fifty',
            'sixty','seventy','eighty','ninety']
    # n=[1,19]
    if n < 20:
        return lt20[n]
    # n=[20,99]
    if n < 100:
        return tens[n//10] + toword(n%10)
    # n=[100,999]
    if n < 1000:
        if n % 100 == 0:
            return toword(n//100) + 'hundred'
        else:
            return toword(n//100) + 'hundredand' + toword(n%100)
    if n == 1000:
        return 'onethousand'
    return ''

N=1000
##s=''
##for i in range(1,N+1):
##    s = s + toword(i)
##    
##print len(s)


print reduce((lambda x,y: x+y),map(len,[toword(i) for i in range(1,N+1)]))
