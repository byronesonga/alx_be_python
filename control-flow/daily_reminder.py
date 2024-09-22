task =input("Enter your task")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
match priority:
   case "high":
      print("Reminder: Thi is a high priority task that requires immediate attention today!")
   case "medium":
      print("Reminder:This is a medium priority task that you can perform later")
   case "low":
      print("Reminder:This is low medium priority task that can wait for now ")
if time_bound =="yes":
   print(" Reminder:Work on this task first")
else:
   print("Reminder:Work on the task later ")
