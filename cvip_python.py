#defining the operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y
#to select the operations
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")


user_choice = input("Enter choice (1/2/3/4): ")


if user_choice in ('1', '2', '3', '4'):
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    if user_choice == '1':
        print("Result:", add(number1, number2))
    elif user_choice == '2':
        print("Result:", subtract(number1, number2))
    elif user_choice == '3':
        print("Result:", multiply(number1, number2))
    elif user_choice == '4':
        print("Result:", divide(number1, number2))
else:
    print("Invalid Input")
