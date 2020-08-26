# Resturant bill calculator
meal_total = input('How much was your bill today?: $')

# Get tip percentage from user
tip = input('What percentage would you like to tip your server?: ')

# How many people are splitting the bill
diners = input('How many people are splitting the bill?: ')

# Turn bill number into and interger
meal_total = int(meal_total)

# Turn tip into interger
tip = int(tip)

# Diners to interger
diners = int(diners)

# Turn tip into percentage of total bill
tip_total = meal_total * (tip / 100)



# set total bill
bill_total = meal_total + tip_total

# Total per person

meal_due = meal_total / diners

whats_due = bill_total / diners

tip_due = tip_total / diners

print('Your share of the meal was $', meal_due, 'which makes your share of the tip $', tip_due, 'and your overall total today $', whats_due,'.' )







