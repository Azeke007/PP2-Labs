from datetime import datetime, timedelta
current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)
print("yesterday:", yesterday)
print("today:", current_date)
print("tomorrow:", tomorrow)