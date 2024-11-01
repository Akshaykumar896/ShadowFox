def calculate_speed(distance, time_minutes):
    # Convert time from minutes to seconds
    time_seconds = time_minutes * 60
    
    # Calculate speed in meters per second
    speed = distance / time_seconds
    
    # Return the speed as an integer to remove decimals
    return int(speed)

# Given distance and time
distance = 490
time_minutes = 7

# Calculate and print speed
speed_mps = calculate_speed(distance, time_minutes)
print("Speed in meters per second:", speed_mps)
