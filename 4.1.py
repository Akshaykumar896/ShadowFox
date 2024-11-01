def calculate_bmi_category():
    # Get user input for height and weight
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))
    
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    # Determine BMI category
    if bmi >= 30:
        category = "Obesity"
    elif 25 <= bmi < 30:
        category = "Overweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    else:
        category = "Underweight"
    
    # Print the result
    print("Output:", category)

# Run the function
calculate_bmi_category()
