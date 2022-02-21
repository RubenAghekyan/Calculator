def calculator():
    numb1 = int(input("Please write your first number:\n "))
    numb2 = int(input("Please write your second number:\n "))
    command = input("Please write what do you want to do(-,+):\n ")
    if command == "-":
        return numb1 - numb2
    elif command == "+":
        return numb1 + numb2
    elif command == "/":
        return numb1 / numb2
    elif command == "*":
        return numb1 * numb2
    elif command == "%":
        return numb1 % numb2
    else:
        print("=================================================")
        print("Please write the required command: ")
        return calculator()



print(calculator())
