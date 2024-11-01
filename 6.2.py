# Dictionaries for expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses for you and your partner
total_your_expenses = sum(your_expenses.values())
total_partner_expenses = sum(partner_expenses.values())

# Determine who spent more
if total_your_expenses > total_partner_expenses:
    spender = "You spent more"
elif total_partner_expenses > total_your_expenses:
    spender = "Your partner spent more"
else:
    spender = "You both spent the same amount"

# Find the category with the largest spending difference
max_difference = 0
significant_category = None

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > max_difference:
        max_difference = difference
        significant_category = category

# Print the results
print("Your total expenses:", total_your_expenses)
print("Your partner's total expenses:", total_partner_expenses)
print(spender)
print(f"The largest difference is in '{significant_category}' with a difference of {max_difference}.")
