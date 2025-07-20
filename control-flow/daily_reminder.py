task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        Reminder = f"{task} is a high priority task"
    case "medium":
        Reminder = f"{task} is a medium priority task"
    case "low":
        Reminder = f"{task} is a low priority task"
    case _:
        Reminder = f"{task} has no specified priority"

if time_bound == "yes":
    Reminder += " that requires immediate attention today!"
else:
    Reminder += ". Consider completing it when you have free time."

print(f"Reminder: {Reminder}")