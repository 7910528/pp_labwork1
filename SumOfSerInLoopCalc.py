def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

sum = 0
for n in range(1, 6):
    term = (3**n * factorial(n)) / (n**n)
    sum += term
    print(f"Sum after iteration {n}: {sum}")