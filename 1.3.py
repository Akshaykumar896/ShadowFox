# Store the principal amount, rate of interest, and time
principal = float(input("Enter the principal amount (P): "))
rate_of_interest = float(input("Enter the rate of interest (R): "))
time = 3  # Since we need to calculate SI for 3 years

# Calculate Simple Interest
simple_interest = (principal * rate_of_interest * time) / 100

# Display the result
print("The Simple Interest for 3 years is:", simple_interest)
