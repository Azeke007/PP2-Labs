from datetime import datetime
date1 = input()
date2 = input()
datetime1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
datetime2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
difference_in_seconds = (datetime2 - datetime1).total_seconds()

print(f"The difference between {date2} and {date1} is {difference_in_seconds} seconds.")
