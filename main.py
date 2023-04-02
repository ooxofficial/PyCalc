# Welcome the user
print("Welcome! Enter two numbers!")
# Ask for the first number
first = input("> ")
# Try to convert it to an integer
try:
    first = int(first)
# If it can't be, it will say that it's not a valid number
except ValueError:
    print(f"{first} is not a number")
    exit()
# Ask for the second number
second = input("> ")
# Try to convert it to an integer
try:
    second = int(second)
# If it can't be, it will say that it's not a valid number
except ValueError:
    print(f"{second} is not a number")
    exit()

# Ask the user for the operator

print("Enter an operator (+, -, *, /)")

op = input("> ")

# If the operator is + it will print first + second
# If the operator is - it will print first - second
# If the operator is * it will print first * second
# If the operator is / it will print first / second

if op == "+":
	print(first + second)
elif op == "-":
	print(first - second)
elif op == "*":
	print(first * second)
elif op == "/":
	print(first / second)

# If the operator isn't a valid operator, it will print that it's not a valid one

else:
	print(f"{op} is not a valid operator")