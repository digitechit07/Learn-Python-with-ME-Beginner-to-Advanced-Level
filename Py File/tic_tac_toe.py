board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def play():
    for i in range(3):
        if i < 2:
            print(f' {board[3*i+1]} | {board[3*i+2]} | {board[3*i+3]} ')
            print('___|___|___')
        else:
            print(f' {board[3*i+1]} | {board[3*i+2]} | {board[3*i+3]} ')
            print('   |   |   ')
    # print(board)

def check(player):
    conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)
    ]
    for a, b, c in conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def draw():
    return ' ' not in board[1:]

print('Tic Tac Toe Game')
print('Choose a cell where you wish to place the mark (X or O)')
print(' 1 | 2 | 3 ')
print('___|___|___')
print(' 4 | 5 | 6 ')
print('___|___|___')
print(' 7 | 8 | 9 ')
print('   |   |   ')
while True:
    player = input('Choose which one you want (X or O): ').upper()
    if player not in ['X','O']:
        print('Invalid choice, choose X or O.')
    else:
        break

while True:
    print(f'Player {player} turn')
    position = int(input('Enter which cell you want to put: '))
    if position < 1 or position > 9 or board[position] != ' ':
        print('Invalid move')
        continue
    board[position] = player
    play()
    if check(player):
        print(f'Player {player} wins')
        break
    elif draw():
        print('Draw')
        break
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
