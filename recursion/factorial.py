def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))

def iterative_factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

for i in range(5):
    print(i, iterative_factorial(i))
