task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bond = input("Is it time-bound? (yes/no): ").strip().lower()
match priority:
     case "high" if time_bond == "yes":
              print(f"Reminder: {task} is a high priority", end=" ")
              print(f"that requires immediate attention today!")
              
     case "medium":
              print(f"Reminder: {task} is medium priority")
     case "low" if time_bond == "no":
            print(f"Note: {task} is a low priority task.", end=" ") 
            print(f"Consider completing it when you have free time.")