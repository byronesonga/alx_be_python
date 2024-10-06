def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to float for division
        num = float(numerator)
        denom = float(denominator)
        
        # Check for division by zero
        if denom == 0:
            raise ValueError("Cannot divide by zero.")
        
        result = num / denom
        return result
    
    except ValueError as e:
        return f"Error: {e}"
    except TypeError:
        return "Error: Inputs must be numeric."

def main():
    print("Welcome to the Division Calculator!")
    
    while True:
        numerator = input("Enter the numerator (or 'exit' to quit): ")
        if numerator.lower() == 'exit':
            print("Exiting the calculator.")
            break
            
        denominator = input("Enter the denominator: ")
        
        result = divide(numerator, denominator)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
