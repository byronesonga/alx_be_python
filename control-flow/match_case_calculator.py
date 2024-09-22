num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
result= input("Choose the operation (+, -, *, /):")
match result:
    case "+":
        print("The result is ",num1+num2)
    case "-":
        print("The result is",num1-num2)
    case "*":
        print("The result is",num1*num2)
    case "/":
        print("The result is",num1/num2)
    case _:
        print("Cannot divide by zero")

