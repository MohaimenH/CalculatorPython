print("Calculator started!")
print("Type ADD for addition and SUB for subtraction")

done = ""
stop = ""
num = []
i = 0
math = 0

func = input("Please enter what you what to do: ")

while stop != "STOP":

    temp = input("Please input a number or type STOP: ")
    if temp == "STOP":
        break

    num.append(int(temp))

while (done != "NO") & (done != "N"):

    if func == "ADD":
        for x in num:
            math += x
        print("The addition is: ", math)

    elif func == "SUB":
        math = num[0]
        print(math)
        for x in range(1, len(num)):
            print(num[x])
            math = math - num[x]
        print("The subtraction is: ", math)

    elif func == "MUL":
        math = num[0]
        for x in range(1, len(num)):
            math = math * num[x]
        print("The subtraction is: ", math)

    elif func == "DIV":
        math = num[0]
        for x in range(1, len(num)):
            math = math / num[x]
        print("The subtraction is: ", math)

    done = input("Do you want to do to any other operation?: ")

print("Thanks for using the calculator!")
