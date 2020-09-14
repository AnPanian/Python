#mode
import time

#Introduction
print('Welcome to the Santa Cruz Mountain Adventure Game!')
print('**************************************************')
print('You are visiting Santa Cruz, California.')
print('You go on an evening hike in the mountains alone.')
print('You can take one item with you -    ')
print('map(m), flashlight(f), chocolate(c), rope(r), or stick(s): ')
item = input('What do you choose?  ')
print('You hear a humming sound. ')

choice1 = input('Do you follow it? y or n: ')
if choice1.lower() == 'y':
    print('You keep moving closer to the sound.')
    print('The sound suddenly stops.')
    time.sleep(3)
    print('You are now LOST! ... ')
    time.sleep(3)
    print('You try to call on your phone, but there is no signal.')
    direction = input('What direction do you go? north, south, east, west: ')
    if direction.lower() == 'north':
        print('You reach an abandoned cabin: ')
        if item == 'm':
            print('You use the map to find your way home.')
            print('CONGRATULATIONS! You won the game!')
        else:
            print('If you had the map, you could find your way from here.')
            time.sleep(3)
            print('---You are still lost. You lost the game.---')
    elif direction.lower() == 'south':
        print('You reach a river with a broken bridge.')
        if item.lower() == 'r' or item.lower() == 's':
            print('You chose an item that can fix the bridge')
            print('You fix the bridge, cross it, and find your way home.')
            print('CONGRATULATIONS! You won the game!')
        else:
            print('If you had a rope or a stick you could fix the bridge.')
            time.pause(3)
            print('---You are still lost. You lost the game.---')
    elif direction.lower() == 'west':
        print('You are walking and you trip over a fallen log.')
        print('You hurt your foot. You sit down and wait for help.')
        time.pause(5)
        print('This could be a long time. You are still lost.')
        time.pause(3)
        print('---You lost the game!---')
    else:
        print('You reach the side of a highway. It is dark.')
        if item.lower() == 'f':
            print('You use the flashlight to signal.')
            print('A car stops and gives you a ride home.')
            print('CONGRATULATIONS! You won the game!')
        else:
            print('If you had the flashlight you could signal for help.')
            time.pause(3)
            print('----You are still lost. You lost the game.----')


else: 
    print('Good idea. You are not taking any risks. ')
    print('You start walking back to the starting point.')
    time.pause(3)
    print('You realize you are LOST! ... ')
    print('The sound behind you is getting louder. You panic!')
    time.pause(3)
    action = input('Do you start running(r), or stop to make a call(c)?: ')
    while action.lower() == 'c':
        print('The call does not go through')
        action = input('Do you start running(r), or stop to make a call(c)?: ')
    print('You are running fast. The sound gets really loud.')
    print('A woman on an electric scooter comes up behind you.')
    answer = input('She says, "Name my favorite programming language.": ')
    if answer.lower() == 'python':
        print('She says, "Yes, Python is my favorite programming language."')
        print('"If you have some chocolate, I can help you"')
        if item.lower() == 'c':
            print('Luckily you did choose correctly!')
            print('You give her the chocolate.')
            print('She helps you get home.')
            print('CONGRATULATIONS! You got out safely. You won the game.')
        else:
            print('You should have chosen that chocolate!')
            print('She rides away, leaving you alone and lost.')
            time.pause(3)
            print('----You lost the game----')
    else:
        print('She did not like your answer.')
        print('She rides away, leaving you alone and lost.')
        time.pause(3)
        print('----You lost the game----')








