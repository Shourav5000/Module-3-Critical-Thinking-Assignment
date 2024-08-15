# 24-Hour Clock Alarm

# Ask the user for the current time (in hours)
current_time = int(input("Enter the current time (0-23): "))

# Ask the user for the number of hours to wait for the alarm
hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the time when the alarm will go off
alarm_time = (current_time + hours_to_wait) % 24

# Display the result
print(f"The time when the alarm will go off is: {alarm_time}:00")
