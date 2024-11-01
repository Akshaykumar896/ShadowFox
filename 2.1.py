def format_number(number, representation):
    # Use format to return the formatted string
    formatted_string = format(number, representation)
    return formatted_string

# Call the function with 145 and 'o'
result = format_number(145, 'o')
print("Formatted Result:", result)
