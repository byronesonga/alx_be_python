def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            print("Error: Cannot divide by zero.")
            return 
        print(f"The result of the division is {numerator / denominator}")
    except ValueError:
        print("Error: Please enter numeric values only.")
            
    
