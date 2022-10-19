def multiples_of_three(n):
    """
    Recursive function to find multiples of 3
    """
    if n == 1:
        return 3
    else:
        return multiples_of_three(n-1) + 3

for i in range(1,10):
    print(multiples_of_three(i))

