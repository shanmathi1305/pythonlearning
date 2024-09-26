def factorial(n):
    if n == 0:
        return 1
    else:
        return functools.reduce(lambda x,y: x*y, range(1,n+1))

print factorial(5)