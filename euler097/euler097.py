#Project Euler problem #97


def modpow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if ((exponent & 1) == 1):
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result

base = 2
exponent = 7830457
modulus = 10**10

n = modpow(base, exponent, modulus)

n = 28433*n + 1

print str(n)[-10:]
