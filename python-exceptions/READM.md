def check_temperature(temp):
    """Function to check if the temperature is hot, warm, or cold."""
    if temp > 30:
        return "It's hot outside!"
    elif 15 <= temp <= 30:
        return "It's a warm day."
    else:
        return "It's cold outside!"

# Using the function
print(check_temperature(25))
print(check_temperature(10))
print(check_temperature(35))

