def get_country(city):
    # Define cities in each country
    australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
    uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
    india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
    
    # Determine the country based on the city
    if city in australia:
        return "Australia"
    elif city in uae:
        return "UAE"
    elif city in india:
        return "India"
    else:
        return None

# Ask user for two city names
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Get the country for each city
country1 = get_country(city1)
country2 = get_country(city2)

# Check if both cities belong to the same country and print the result
if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the list")
