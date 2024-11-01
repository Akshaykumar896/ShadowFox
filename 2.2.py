def pond_water_amount(radius, pi=3.14, water_per_sq_meter=1.4):
    # Calculate the area of the pond
    area = pi * (radius ** 2)
    
    # Calculate the total water in the pond
    total_water = area * water_per_sq_meter
    
    # Convert to an integer to remove decimal points and return
    return int(total_water)

# Given radius of the pond
radius = 84

# Calculate and print the total amount of water in liters
total_water_liters = pond_water_amount(radius)
print("Total amount of water in the pond (in liters):", total_water_liters)
