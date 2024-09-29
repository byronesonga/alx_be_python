from datetime import *
# print(dir(datetime))
def display_current_datetime():
    global current_date
    current_date = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))
display_current_datetime()
days_added = int(input("Enter the number of days to add to the current date:"))
def calculate_future_date():
    future_date = current_date + timedelta(days=days_added)
    print(future_date.strftime("%Y-%m-%d %H:%M:%S"))
calculate_future_date()