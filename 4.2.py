def find_country(city):
    # Define cities in each country
    australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
    uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
    india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
    
    # Determine the country based on city input
    if city in australia:
        country = "Australia"
    elif city in uae:
        country = "UAE"
    elif city in india:
        country = "India"
    else:
        country = None
    
    # Print the result based on the country found
    if country:
        print(f"{city} is in {country}")
    else:
        print(f"{city} is not in the list")

# Ask user for a city name
city_name = input("Enter a city name: ")
find_country(city_name)
