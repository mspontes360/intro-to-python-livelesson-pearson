"""
Given a temperature in Fahrenheit, return the temperature in Celsius

T<°C> = (T<°F> - 32) * 5 / 9

"""
# Ask for a temperature in Fahrenheit
temp_fahrenheit = input("What's the temperature in Fahrenheit? ")

# Calculate it in Celsius
temp_celsius = (float(temp_fahrenheit) - 32) * 5 / 9

# Tell the user what it is
print("The temperature in Celsius is " + str(temp_celsius))
