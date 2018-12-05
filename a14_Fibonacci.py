def fibonacci(n):
    fib = []
    x = 1
    if n == 0:
        fib = []
    elif n == 1:
        fib = [1]
    elif n == 2:
        fib = [1, 1]
    else:
        fib = [1, 1]
        while x < (n -1):
            fib.append(fib[x] + fib[x-1])
            x += 1
    return fib


n = int(input("Enter number: "))
print(fibonacci(n))
