import sys

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print(sys.argv)
num = int(sys.argv[1])
print(fib(num))
