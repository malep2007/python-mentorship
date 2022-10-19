"""
Write a recursive Python function that returns the sum of the first n integers. 
(Hint: The function will be similiar to the factorial function!)
"""

def sumn(n):
    if n == 0:
        return 0
    else:
       return n + sumn(n-1)
