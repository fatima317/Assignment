import time
import calendar
from datetime import datetime
import math

# epoch in python
epoch = time.time()
print("Seconds since Unix epoch (Jan 1, 1970):", epoch)

# getting current time
current_time = time.ctime()
print("Current time:", current_time)

# formatting time
formatted = time.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted time:", formatted)

# getting calender 
print(calendar.month(2025, 5))  # May 2025

# datetime
dt = datetime(2025, 5, 25, 14, 30)
print("Custom datetime:", dt)

# strftime() method
now = datetime.now()
formatted = now.strftime("%A, %d %B %Y")
print("Formatted date:", formatted)

# math module
print("Square root of 16:", math.sqrt(16))
print("Pi value:", math.pi)
print("Cosine of 0:", math.cos(0))

# NAN (Not a Number) 
nan_value = float('nan')
print("Is NaN:", math.isnan(nan_value))  # True

# Infinity
infinity = float('inf')
print("Infinity value:", infinity)
print("Is infinity greater than 1e308?", infinity > 1e308)
