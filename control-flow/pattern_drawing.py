size = int(input("Enter the size of the pattern: "))
if size > 0:
    count = 0
    while count < size: 
        for i in range(size):
            print(size * "*" , end=" ")
            print()
            count +=1 
        
else:
    print("Error: Please enter a positive integer other than 0")