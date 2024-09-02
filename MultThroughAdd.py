def multiply_using_addition(a, b):
    result = 0
    for _ in range(b):
        result += a
    return result
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a <= 0 or b <= 0:
    print("Both numbers must be natural numbers.")
else:
    result = multiply_using_addition(a, b)
    print(f"The result of {a} multiplied by {b} using addition is: {result}")