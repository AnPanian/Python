#Sample password program

set_password = input('Set your password.: ')
password = input('What is your password?: ')

while password != set_password:
    print('That is not the correct password')
    password = input(' Please enter password again')
print(' That is correct')






