def perform_operation(num1, num2,operation):
    print("Arithmetic Operations")
num1 = float(input("Enter the first number:"))
num2 =float(input("Enter the second number:"))
operation =input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
match operation:
    case "add":
        result =num1+num2
        print(f"Result:{result}")
    case "subtract":
        result=num1-num2
        print(f"Result:{result}")
    case "multipy":
        result=num1*num2
        print(f"Result:{result}")
    case "divide":
        result=num1/num2
        if num1==0:
            print("Cannot divide by zero")
        else:
            print(f"Result:{result}")
perform_operation(num1,num2,operation)