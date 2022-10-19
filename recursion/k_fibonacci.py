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