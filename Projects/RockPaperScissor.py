# Project Idea: Rock Paper Scissors Game

import random


choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)
player = None

while player not in choices:
    player = input('Enter Your Choice (Rock, Paper, Scissors): ').lower()

if player == computer:
    print(f'Computer Chose: {computer}')
    print(f'Player Chose: {player}') 
    print('It\'s a Tie!')
elif player == 'rock':
    if computer == 'paper':
        print(f'Computer Chose: {computer}')
        print(f'Player Chose: {player}')
        print('You Lose!')
    else:
        print(f'Computer Chose: {computer}')
        print(f'Player Chose: {player}') 
        print('You Win!')
elif player == 'paper':
    if computer == 'scissors':
        print(f'Computer Chose: {computer}')
        print(f'Player Chose: {player}')    
        print('You Lose!')
    else:
        print(f'Computer Chose: {computer}')
        print(f'Player Chose: {player}') 
        print('You Win!')
else:  # player == 'scissors'
    if computer == 'rock':
        print(f'Computer Chose: {computer}')
        print(f'Player Chose: {player}') 
        print('You Lose!')
    else:
        print(f'Computer Chose: {computer}')
        print(f'Player Chose: {player}') 
        print('You Win!')

# print(f'Computer Chose: {computer}')
# print(f'Player Chose: {player}')