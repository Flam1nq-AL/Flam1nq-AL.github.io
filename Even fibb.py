def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n = 0
num = fibonacci(n)
total = 0
while num < 4000000:
    n += 1
    num = fibonacci(n)
    if num % 2 == 0:
        total += num

print(total)
    