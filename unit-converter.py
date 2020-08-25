#Converts units

#Get inches from user
inch = input('Howdy Partner, how many inches do you have?: ')

# create an interger
inch = int(inch)

# math
centi = inch * 2.54

#Give answer

print('Wow, ', inch, 'inch(es) is ', centi, 'centimeters!')

# Get pounds 
pounds = input('How heavy is that item in pounds?: ')

# convert to interger
pounds = int(pounds)

# Convert to kiligrams
kg = pounds * 2.2

# Answer
print('Right on, that is ', kg, 'kilograms!')

# Get temperature in fahrenheit
fahrenheit = input('What is the temperture in fahrenheit?: ')

#Convert to interger
fahrenheit = int(fahrenheit)

#Convert to celsius
celsius = fahrenheit - 32/(9/5)

#Answer
print(fahrenheit, 'in Fahrenheit is ', celsius, 'in Celsius!')


