"""
PROBLEM: We need to create a function where it takes an integer. Then, we will return the sum of the two preceeding numbers.
SOLUTION: A recursive approach can solve this problem, however, this is not an optimized solution. Time complexity for using this approach is O(n), which is bad!
"""

def fib(n):
    print(n)
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))

x = 5
y = fib(x)
print(y)