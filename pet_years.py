#Pet years to Human years

pet_type = input('Do you have a cat or a dog?: ')
pet_age = input('How old is your pet in human years?: ')
pet_age = int(pet_age)

while pet_type.lower() == 'cat':
    while pet_age == 1:
        pet_age = 15 
        
    if pet_age == 2:
        pet_age = 24
       
    elif pet_age > 2:
       pet_age= 24 + ((pet_age - 2) * 4) 
    print('Your cat is ', pet_age, 'years old in cat years.')

if pet_type.lower() == 'dog':
    while pet_age == 1:
        pet_age = 12
    if pet_age == 2:
        pet_age = 24
    elif pet_age > 2:
        pet_age = 24 + ((pet_age -2) * 4)
    print('Your dog is ', pet_age, 'years old in dog years.')

