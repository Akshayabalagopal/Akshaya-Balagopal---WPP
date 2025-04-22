import pandas as pd
import datetime

dt_a = pd.to_datetime("2012-01-15")
print("a) DateTime object for Jan 15, 2012:", dt_a)

dt_b = pd.to_datetime("2012-01-15 21:20")
print("b) Specific date and time (9:20 PM):", dt_b)

dt_c = pd.to_datetime("now")
print("c) Local date and time:", dt_c)

dt_d = pd.to_datetime("2012-01-15").date()  # .date() to get the date part only
print("d) Date without time:", dt_d)

current_date = pd.to_datetime("today").date()  # Today's date without time
print("e) Current date:", current_date)

user_input = input("Enter a date and time (e.g., '2012-01-15 21:20'): ")
dt_f = pd.to_datetime(user_input)
time_from_dt = dt_f.time()  # Extract only the time
print("f) Time from date-time:", time_from_dt)

current_local_time = pd.to_datetime("now").time()  # Get the time part of the current local time
print("g) Current local time:", current_local_time)
