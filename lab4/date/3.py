from datetime import datetime
dt_with_microseconds = datetime(2022, 2, 18, 12, 30, 45, 123456)
dt_without_microseconds = dt_with_microseconds.replace(microsecond=0)
print("Datetime with microseconds:", dt_with_microseconds)
print("Datetime without microseconds:", dt_without_microseconds)
