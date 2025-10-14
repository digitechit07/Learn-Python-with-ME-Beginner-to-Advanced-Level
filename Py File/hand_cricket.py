import random

toss_list = ['odd','even']
print('player asks odd or even')
computer = random.choice(toss_list)
if computer == 'even':
    player = 'odd'
else:
    player = 'even'

print(f'computer chooses {computer}')
print(f'player is {player}')

computer_play = random.randint(1,6)
player_play = int(input('Enter the number to play toss (1 - 6): '))
print(f'computer plays {computer_play}')
toss_sum = player_play + computer_play
player_choice = 0
computer_choice = 0

if (toss_sum % 2 == 0 and player == 'even') or (toss_sum % 2 == 1 and player == 'odd'):
    print('Player won the toss')
    player_choice = int(input('Choose 1. Batting or 2. Balling: '))
    if player_choice == 1:
        print('Player chooses batting')
        computer_choice = 2
        print('Computer is balling')
    else:
        print('Player chooses balling')
        print('Computer is batting')
elif (toss_sum % 2 == 0 and player == 'odd') or (toss_sum % 2 == 1 and player == 'even'):
    print('Computer won the toss')
    computer_choice = random.randint(1,2)
    if computer_choice == 1:
        print('Computer chooses batting')
        player_choice = 2
        print('Player is balling')
    else:
        print('Computer chooses balling')
        print('Player is batting')

if player_choice == 1 or computer_choice == 2:
    play_sum = 0
    while True:
        try:
            player_play = int(input('Enter the number to bat(1-6): '))
            if not 1 <= player_play <= 6:
                print('Please enter a number between 1 and 6')
                continue
        except ValueError:
            print('Invalid input. Please enter a valid number')
            continue

        computer_play = random.randint(1,6)
        print(f'Computer plays {computer_play}')
        if player_play != computer_play:
            play_sum += player_play
            print(f'Player score: {play_sum}')
        else:
            print('Player is out')
            print(f'Final player score is {play_sum}')
            break

    second_play_sum = 0
    print(f'Score to beat {play_sum}')
    while second_play_sum <= play_sum:
        try:
            player_play = int(input('Enter the number to bat(1-6): '))
            if not 1 <= player_play <= 6:
                print('Please enter a number between 1 and 6')
                continue
        except ValueError:
            print('Invalid input. Please enter a valid number')
            continue

        computer_play = random.randint(1,6)
        print(f'Computer plays {computer_play}')
        if player_play != computer_play:
            second_play_sum += computer_play
            print(f'Computer score: {second_play_sum}')
            if second_play_sum > play_sum:
                print('Computer won the game')
                break
            elif second_play_sum == play_sum:
                print('Game tied')
                break
        else:
            print('Computer is out')
            print(f'Final computer score: {second_play_sum}')
            if second_play_sum < play_sum:
                print('Player won the game')
            elif second_play_sum == play_sum:
                print('Game tied')
            else:
                print('Computer won the game')
            break

elif player_choice == 2 or computer_choice == 1:
    play_sum = 0
    while True:
        try:
            player_play = int(input('Enter the number to bat(1-6): '))
            if not 1 <= player_play <= 6:
                print('Please enter a number between 1 and 6')
                continue
        except ValueError:
            print('Invalid input. Please enter a valid number')
            continue

        computer_play = random.randint(1,6)
        print(f'Computer plays {computer_play}')
        if player_play != computer_play:
            play_sum += computer_play
            print(f'Computer score: {play_sum}')
        else:
            print('Computer is out')
            print(f'Final computer score is {play_sum}')
            break

    second_play_sum = 0
    print(f'Score to beat {play_sum}')
    while second_play_sum <= play_sum:
        try:
            player_play = int(input('Enter the number to bat(1-6): '))
            if not 1 <= player_play <= 6:
                print('Please enter a number between 1 and 6')
                continue
        except ValueError:
            print('Invalid input. Please enter a valid number')
            continue

        computer_play = random.randint(1,6)
        print(f'Computer plays {computer_play}')
        if player_play != computer_play:
            second_play_sum += player_play
            print(f'Player score: {second_play_sum}')
            if second_play_sum > play_sum:
                print('Player won the game')
                break
            elif second_play_sum == play_sum:
                print('Game tied')
                break
        else:
            print('Player is out')
            print(f'Final player score: {second_play_sum}')
            if second_play_sum < play_sum:
                print('Computer won the game')
            elif second_play_sum == play_sum:
                print('Game tied')
            else:
                print('Player won the game')
                break