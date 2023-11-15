def max_of_two(a, b):
    return a if a > b else b

num1, num2 = map(int, input("Enter  two numbers: ").split())

result = max_of_two(num1, num2)
print(f"The maximum of {num1} and {num2} is: {result}")

