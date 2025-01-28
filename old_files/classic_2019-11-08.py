import math

def stirling_number(n, k):
    assert type(n) is int
    assert type(k) is int
    assert n >= 0
    assert k >= 0
    if n==0 and k==0:
        return 1
    elif k==0:
        return 0
    elif n==0:
        return 0
    else:
        return k*stirling_number(n-1,k) + stirling_number(n-1,k-1)

def choose(m, n):
    assert m >= n
    f = math.factorial
    return f(m)/(f(n)*f(m-n))

def faux_stirling_number(n, k):
    return k*sum([choose(k,i)*stirling_number(n-1,i) for i in range(1,k+1)])

print(faux_stirling_number(100,3))