task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bond = input("Is it time-bound? (yes/no): ").strip().lower()
match priority:
     case "high":  
         Reminder =f"{task} is a high priority task"
     case "medium":
        Reminder = f"{task} is a medium priority task"
     case "low":
        Reminder = f"{task} is a low priority task" 
     case _:
        Reminder = f"{task} has no priority task"
if time_bond == "yes":
      Reminder += "that requires immediate attention today!"
else:
      Reminder += "Consider completing it when you have free time."
print(f"Reminder: {Reminder}")