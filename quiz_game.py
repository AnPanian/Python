# Quiz Game

#Set player name and beginning score to 0

player_name = input('Please insert your gamer ID: ')
player_score = 0

questions = ['What is the capital of Peru?', 'Which is the longest river?' ]
answer_1 = ['Lima', 'Amazon']
for n in range(2):
    print(questions(n))
    answer = input('type your answer: ')
    if answer == answer_1():
        print('That is correct')
        player_score = player_score + 1
    else:
        print('Your answer is incorrect.')
        print(answer_1())

print(player_name, ', your final score is ', player_score, '. Play again.')










