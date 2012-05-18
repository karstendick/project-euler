#Project Euler problem #36

def memoize(fn):
    memo={}
    def memoizer(*param_tuple, **kwds_dict):
        if kwds_dict:
            return fn(*param_tuple, **kwds_dict)
        try:
            try:
                return memo[param_tuple]
            except KeyError:
                memo[param_tuple] = result = fn(*param_tuple)
                return result
        except TypeError:
            return fn(*param_tuple)
    return memoizer

bstr = lambda n: n>0 and bstr(n>>1)+str(n&1) or ''
bstr = memoize(bstr)

def is_palindrome(s):
    n=len(s)
    for i in range(n/2):
        if s[i] != s[n-1-i]:
            return False
    return True

sum=0
for i in range(1,1000000,2):
    if is_palindrome(str(i)) and is_palindrome(bstr(i)):
        sum+=i

print(sum)
