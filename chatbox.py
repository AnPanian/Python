Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
# An interactive chat program that allows inputs from the user and generates outputs.

# Chat box introduction
print('Hello, I am Chattex2020. I am your personal chatbox.')
print('I like animals and I love to talk about food')
name = input('What is your name?: ')
print('Hello', name, ', Nice to meet you')

# get year information
year = input('I am not very good at dates, what year is it? ')
print('Yes, I think that is correct. Thanks!')

# ask user t guess age
myage = input('Can you guess my age? Enter a number: ')
print('Yes, you are right. I am ', myage)

# do math to clculate when chatbot will be 100
myage = int(myage)
nyears = 100 - myage
print('I will be 100 in', nyears, 'years.')

# food conversation
print('I love chocolate and I also like trying out new kinds of food')
food = input('How about you? What is your favorite food?: ')
print('I like ', food, 'too!')
question = 'How often do you eat ' + food + '?:'
howoften = input(question)
print('Interesting. I wonder if that is good for your health.')

# animal conversation
animal - input('My favorite animal is a giraffe. What is yours?: ')
print(animal, '! I do not like them.')
print('I wonder if a', animal, 'likes to eat', food, '?')

# conversation about feelings
feeling = input('How are you feeling today?: ')
print('Why are you feeling', feeling, 'now?')
reason = input('Please tell me: ')
print('I understand, thanks for sharing')
