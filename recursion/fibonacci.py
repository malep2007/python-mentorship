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
