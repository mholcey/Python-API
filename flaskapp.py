def fibonacci(n):
    a = 0
    b = 1
    if n <= 0:
        print("Number too low")
    if n >= 100:
        print("Number too high")
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b
print(fibonacci(7))
