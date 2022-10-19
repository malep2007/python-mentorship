# Recursion 
Recursion is a topic that is theoretically simple to conceive, because it involves simply that, recursion. Or as I can plainly put it. Repetition. I have learnt that it is easy for me to get lost in thinking about the depths of how far I can repeat a task over and over again, till a break point but computers are built for that. Even with that said, I have also come to learn that there are times when this is not the most elegant way to solve a problem, but it is still quite valuable and straightforward solutions can be designed from this concept. 

## Fibonacci Series
This is a simple place to start when trying to teach the concept of recursion. So what is the Fibonacci series? This is simply a series in which a number is the sum of the two preceding numbers in the same series. Let’s assume we have an initial number of 1, the next number would be 1, then the next 2, and the next 3 and so on,
```
1,1,2,3,5,8,13,… 
```
```python
def fib(n):
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```