print("Calculator started!")
print("Type ADD for addition and SUB for subtraction")


func = input("Please enter what you what to do: ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if func == "ADD":
    print(num1 + num2)

print("Thanks for using the calculator!")
