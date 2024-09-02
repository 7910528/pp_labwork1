def division_using_subtraction(a, b):
    result = 0
    while a >= b:
        a -= b
        result += 1
    return result
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a <= 0 or b <= 0:
    print("Both numbers must be natural numbers.")
elif b > a:
    print("The second number must be less than or equal to first.")
else:
    result = division_using_subtraction(a, b)
    print(f"The result of {a} divided by {b} using subtraction is: {result}")