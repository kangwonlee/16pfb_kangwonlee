import sys


def factorial(n):
    if 1 == n:
        return 1
    elif 1 < n:
        return n * factorial(n - 1)
    else:
        print("Impossible! n = %d" % n)
        sys.exit(0)


print(factorial(-1))
