from timeit import Timer 

def fib(n):
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fibi(n):
    old, new = 0, 1
    if n == 0:
        return 0
    for i in range(n -1):
        old, new = new, old + new 
    return new 

memo = {0:0, 1:1}
def fibm(n):
    """
    recursive Fibonacci function which memoizes previously calculted values the help of a dictionariy memo
    """
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n -2)
    return memo[n]


class FibonacciLike:
    def __init__(self, i1=0, i2=1):
        self.memo = {0:i1, 1:i2}
    
    def __call__(self, n):
        if n not in self.memo:
            self.memo[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.memo[n]


t1 = Timer("fib(10)", "from fibonacci import fib")
for i in range(1,20):
    cmd = "fib(" + str(i) + ")"
    t1 = Timer(cmd, "from fibonacci import fib")
    time1 = t1.timeit(3)
    cmd = "fibi(" + str(i) + ")"
    t2 = Timer(cmd, "from fibonacci import fibi")
    time2 = t2.timeit(3)
    cmd = "fibm(" + str(i) + ")"
    t3 = Timer(cmd, "from fibonacci import fibm")
    time3 = t3.timeit(3)
    print(f"n={i:2d}, fib: {time1:8.6f}, fibi: {time2:7.6f}, time1/time2: {time1/time2:10.2f}, fibm: {time3:7.6f}, time1/time3: {time1/time3}")


fibf = FibonacciLike() # create a callable to create the Fibonacci numbers
lucas = FibonacciLike(2,1)

for i in range(1,16):
    print(i, fibf(i), lucas(i))


class kFibonacci:
    def __init__(self, k, initials, coefficients):
        self.memo = dict(zip(range(k), initials))
        self.coeffs = coefficients
        self.k = k
    
    def __call__(self, n):
        k = self.k
        if n not in self.memo:
            result = 0
            for coeff, i in zip(self.coeffs, range(1, k+1)):
                result = result + (coeff * self.__call__(n-i))
            self.memo[n] = result
        return self.memo


fib = kFibonacci(2, (0,1), (1,1))
lucas = kFibonacci(2,(2,1), (1,1))

for i in range(1,16):
    print(i, fib(i), lucas(i))
