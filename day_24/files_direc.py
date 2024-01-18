from datetime import datetime, timedelta

# Get the current date and time
current_datetime = datetime.now()



# Add 70 years to the current year
future_datetime = current_datetime.replace(year=current_datetime.year + 70)

# Add 5 hours and 30 minutes
time_delta = timedelta(hours=5, minutes=-30)
future_datetime += time_delta

# Print the future datetime
print("Future datetime:", future_datetime)

# Convert the future datetime to a timestamp
future_timestamp = int(future_datetime.timestamp())

# Print the timestamp of the future datetime
print("Future timestamp:", future_timestamp)
