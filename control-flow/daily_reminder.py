task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bond = input("Is it time-bound? (yes/no): ").strip().lower()
match priority:
     case "high":
              print(f"Reminder: {task} is a high priority", end=" ")
              if time_bond =="yes":
                     print("that requires immediate attention today!")
              
     case "medium":
              print(f"Reminder: {task} is medium priority", end=" ")
     case "low":
            print(f"Note: {task} is a low priority task.", end =" ") 
            if time_bond == "no" :
                   print("Consider completing it when you have free time.")

             