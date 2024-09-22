task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
   case "high":
      reminder = f"Reminder: '{task}' is of high priority."
   case "medium":
      reminder =f"Reminder: '{task}'is a medium priority."
   case "low":
      reminder =f"Reminder:'{task}'is low medium priority."
   case _:
      reminder = "Not a priority. Please enter(high/medium/low)"
if time_bound =="yes":
   reminder +="Work on this task first"
else:
   reminder +="Work on the task later."
print(f"Reminder: '{task}' is of high priority.")
print(reminder)
