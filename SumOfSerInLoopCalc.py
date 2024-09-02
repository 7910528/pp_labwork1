import math

sum = 0
for n in range(1, 6):
    term = (3**n * math.factorial(n)) / (n**n)
    sum += term
    print(f"Sum after iteration {n}: {sum}")