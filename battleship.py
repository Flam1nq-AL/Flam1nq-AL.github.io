import os

grid1 = [['0' for a in range(8)] for b in range(8)]
grid2 = [['0' for a in range(8)] for b in range(8)]
guess_p1 = [['?' for a in range(8)] for b in range(8)]
guess_p2 = [['?' for a in range(8)] for b in range(8)]

p1_ships = 4
p2_ships = 4


def clear():
    os.system('cls')


def guess(row, column, grid, player):

    def destroyed(grid, length):
        if not any(length in x for x in grid):
            return True
        else:
            return False
    if grid[row][column] == '2':
        grid[row][column] = '2X'
        if destroyed(grid, '2'):
            print('You destroyed the enemy ship of length 2!')
            if player == 1:
                global p1_ships
                p1_ships -= 1
            else:
                global p2_ships
                p2_ships -= 1
        else:
            print('Boom! You hit a ship!')
    elif grid[row][column] == '3':
        grid[row][column] = '3X'
        if destroyed(grid, '3'):
            print('You destroyed the enemy ship of length 3!')
            if player == 1:
                p1_ships -= 1
            else:
                p2_ships -= 1
        else:
            print('Boom! You hit a ship!')
    elif grid[row][column] == '4':
        grid[row][column] = '4X'
        if destroyed(grid, '4'):
            print('You destroyed the enemy ship of length 4!')
            if player == 1:
                p1_ships -= 1
            else:
                p2_ships -= 1
        else:
            print('Boom! You hit a ship!')
    elif grid[row][column] == '5':
        grid[row][column] = '5X'
        if destroyed(grid, '5'):
            print('You destroyed the enemy ship of length 5!')
            if player == 1:
                p1_ships -= 1
            else:
                p2_ships -= 1
        else:
            print('Boom! You hit a ship!')

    else:
        print('Oops! You missed.')
        grid[row][column] == 'O'


def checkwin(ships1, ships2):
    if ships1 == 0 or ships2 == 0:
        return True
    else:
        return False


def input_coords():
    again = True
    while again == True:
        try:
            x1 = int(
                input('What is your guess for the row? (0-7)'))
        except ValueError:
            print("That is not a valid integer (0-7).")
            continue
        except x1 < 0 or x1 > 7:
            print("That is not a valid integer 0-7.")
            continue
        else:
            again = False

    again = True
    while again == True:
        try:
            y1 = int(input('What is you guess for the column? (0-7)'))
        except ValueError:
            print("That is not a valid integer 0-7. Please try again.")
            continue
        except y1 < 0 or y1 > 7:
            print("That is not a valid integer 0-7.")
            continue
        else:
            again = False

    return x1, y1


def place_ship(length, grid):

    def check_valid(row, column, direction, length, grid):
        things = []
        if direction == 'u':
            for i in range(length):
                things.append(grid[row-i][column])
        if direction == 'd':
            for i in range(length):
                things.append(grid[row+i][column])
        if direction == 'l':
            for i in range(length):
                things.append(grid[row][column-i])
        if direction == 'r':
            for i in range(length):
                things.append(grid[row][column+1])
        if ('2' not in things) and ('3' not in things) and ('4' not in things) and ('5' not in things):
            if direction == 'u':
                if row - length < 0:
                    return False
                else:
                    return True
            elif direction == 'd':
                if row + length > 8:
                    return False
                else:
                    return True
            elif direction == 'l':
                if column - length < 0:
                    return False
                else:
                    return True
            else:
                if column + length > 8:
                    return False
                else:
                    return True
        else:
            return False

    again = True
    while again == True:
        try:
            row = int(
                input(f'Please enter the row (0-7) for the {length} length ship'))
        except ValueError:
            print("That is not a valid integer 0-7.")
            continue
        except row < 0 or row > 7:
            print("That is not a valid integer 0-7.")
            continue
        else:
            again = False

    again = True
    while again == True:
        try:
            column = int(
                input(f'Please enter the column (0-7) for the {length} length ship'))
        except ValueError:
            print("That is not a valid integer 0-7.")
            continue
        except column < 0 or column > 7:
            print("That is not a valid integer 0-7.")
            continue
        else:
            again = False

    direction = input(
        'Which direction? Left,right,up or down? (L/R/U/D)'.lower())
    while direction != 'l' and direction != 'r' and direction != 'u' and direction != 'd':
        direction = input(
            'Invalid input. Left, right, up or down? (L/R/U/D)'.lower())

    while check_valid(row, column, direction, length, grid) == False:
        print('Those are not valid coordinates. Please try again')
        again = True
        while again == True:
            try:
                row = int(
                    input(f'Please enter the row (0-7) for the {length} length ship'))
            except ValueError:
                print("That is not a valid integer 0-7.")
                continue
            except row < 0 or row > 7:
                print("That is not a valid integer 0-7.")
                continue
            else:
                again = False

        again = True
        while again == True:
            try:
                column = int(
                    input(f'Please enter the column (0-7) for the {length} length ship'))
            except ValueError:
                print("That is not a valid integer 0-7.")
                continue
            except column < 0 or column > 7:
                print("That is not a valid integer 0-7.")
                continue
            else:
                again = False

        direction = input(
            'Which direction? Left,right,up or down? (L/R/U/D)'.lower())
        while direction != 'l' and direction != 'r' and direction != 'u' and direction != 'd':
            direction = input(
                'Invalid input. Left, right, up or down? (L/R/U/D)'.lower())
    if direction == 'r':
        if length == 2:
            for i in range(length):
                grid[row][column+i] = '2'
        elif length == 3:
            for i in range(length):
                grid[row][column+i] = '3'
        elif length == 4:
            for i in range(length):
                grid[row][column+i] = '4'
        elif length == 5:
            for i in range(length):
                grid[row][column+i] = '5'
    elif direction == 'l':
        if length == 2:
            for i in range(length):
                grid[row][column-i] = '2'
        elif length == 3:
            for i in range(length):
                grid[row][column-i] = '3'
        elif length == 4:
            for i in range(length):
                grid[row][column-i] = '4'
        elif length == 5:
            for i in range(length):
                grid[row][column-i] = '5'
    elif direction == 'u':
        if length == 2:
            for i in range(length):
                grid[row-i][column] = '2'
        elif length == 3:
            for i in range(length):
                grid[row-i][column] = '3'
        elif length == 4:
            for i in range(length):
                grid[row-i][column] = '4'
        elif length == 5:
            for i in range(length):
                grid[row-i][column] = '5'
    else:
        if length == 2:
            for i in range(length):
                grid[row+i][column] = '2'
        elif length == 3:
            for i in range(length):
                grid[row+i][column] = '3'
        elif length == 4:
            for i in range(length):
                grid[row+i][column] = '4'
        elif length == 5:
            for i in range(length):
                grid[row+i][column] = '5'


def display(grid):
    for r in grid:
        for c in r:
            print(c, end=' ')
        print()


def play():
    print('Player 1, get ready to place your ships.')
    for i in range(2, 6):
        place_ship(i, grid1)
        display(grid1)

    print('Player 2, get ready to place your ships.')
    for i in range(2, 6):
        place_ship(i, grid2)
        display(grid2)

    while checkwin(p1_ships, p2_ships) == False:
        display(guess_p1)
        print('Player 1, make your guess.')
        x1, y1 = input_coords()

        guess(x1, y1, grid2, 2)

        print(grid2[x1][y1])
        if grid2[x1][y1] == '2X':
            guess_p1[x1][y1] = '2'
        elif grid2[x1][y1] == '3X':
            guess_p1[x1][y1] = '3'
        elif grid2[x1][y1] == '4X':
            guess_p1[x1][y1] = '4'
        elif grid2[x1][y1] == '5X':
            guess_p1[x1][y1] = '5'
        else:
            guess_p1[x1][y1] = 'O'

        display(guess_p2)
        print('Player 2, make your guess.')
        x2, y2 = input_coords()

        guess(x2, y2, grid1, 1)

        print(grid1[x2][y2])
        if grid1[x2][y2] == '2X':
            guess_p2[x2][y2] = '2'
        elif grid1[x2][y2] == '3X':
            guess_p2[x2][y2] = '3'
        elif grid1[x2][y2] == '4X':
            guess_p2[x2][y2] = '4'
        elif grid1[x2][y2] == '5X':
            guess_p2[x2][y2] = '5'
        else:
            guess_p1[x2][y2] = 'O'

    if p1_ships == 0:
        print('Player 2 Won!')
    else:
        print('Player 1 Won!')
    play_again = input('Would you like to play again? (Y or N)'.lower())
    while play_again != 'y' and play_again != 'n':
        play_again = input(
            'Invalid input. Would you like to play again? (Y or N)'.lower())

    if play_again == 'y':
        play()


play()
