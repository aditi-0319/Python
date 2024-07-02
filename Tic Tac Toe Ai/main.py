import random

board = [' ' for x in range(10)]


def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')


def IsWinner(b, l):
    return (b[1] == l and b[2] == l and b[3] == l) or (b[4] == l and b[5] == l and b[6] == l) or \
        (b[7] == l and b[8] == l and b[9] == l) or \
        (b[1] == l and b[4] == l and b[7] == l) or (b[3] == l and b[6] == l and b[9] == l) or \
        (b[2] == l and b[5] == l and b[8] == l) or \
        (b[1] == l and b[5] == l and b[9] == l) or (b[3] == l and b[5] == l and b[7] == l)


def spaceIsFree(pos):
    return board[pos] == ' '


def insertLetter(letter, pos):
    board[pos] = letter


def playerMove(symbol):
    if symbol == 'X':
        run = True
        while run:
            move = input("\n\nPlease select a position to enter the {sym} between 1 to 9: ".format(sym=symbol))
            try:
                move = int(move)
                if 1 <= move <= 9:
                    if spaceIsFree(move):
                        run = False
                        insertLetter(symbol, move)
                    else:
                        print('Sorry, this space is occupied.')
                else:
                    print('Please type a number between 1 and 9: ')
            except ValueError:
                print('Please type a number: ')
    else:
        print("\n\nAI's move:")
        move = aimove()
        insertLetter(symbol, move)
        print("AI placed the 'O' at position: ", move)


def aimove():
    my_sym = 'O'
    opp_sym = 'X'
    available_moves = [pos for pos in range(1, 10) if spaceIsFree(pos)]

    if spaceIsFree(2) and (board[1] == board[3] == opp_sym or board[5] == board[8] == opp_sym):
        return 2
    elif spaceIsFree(3) and (
            board[1] == board[2] == opp_sym or board[6] == board[9] == opp_sym or board[5] == board[7] == opp_sym):
        return 3
    elif spaceIsFree(4) and (board[1] == board[7] == opp_sym or board[5] == board[6] == opp_sym):
        return 4
    elif spaceIsFree(5) and (
            board[1] == board[9] == opp_sym or board[3] == board[7] == opp_sym or board[2] == board[8] == opp_sym or
            board[4] == board[6] == opp_sym):
        return 5
    elif spaceIsFree(6) and (board[3] == board[9] == opp_sym or board[4] == board[5] == opp_sym):
        return 6
    elif spaceIsFree(7) and (
            board[1] == board[4] == opp_sym or board[8] == board[9] == opp_sym or board[5] == board[3] == opp_sym):
        return 7
    elif spaceIsFree(8) and (board[2] == board[5] == opp_sym or board[7] == board[9] == opp_sym):
        return 8
    elif spaceIsFree(9) and (
            board[7] == board[8] == opp_sym or board[3] == board[6] == opp_sym or board[5] == board[1] == opp_sym):
        return 9
    elif spaceIsFree(1) and (
            board[2] == board[3] == opp_sym or board[4] == board[7] == opp_sym or board[5] == board[9] == opp_sym):
        return 1
    elif spaceIsFree(2) and (board[1] == board[3] == my_sym or board[5] == board[8] == my_sym):
        return 2
    elif spaceIsFree(3) and (
            board[1] == board[2] == my_sym or board[6] == board[9] == my_sym or board[5] == board[7] == my_sym):
        return 3
    elif spaceIsFree(4) and (board[1] == board[7] == my_sym or board[5] == board[6] == my_sym):
        return 4
    elif spaceIsFree(5) and (
            board[1] == board[9] == my_sym or board[3] == board[7] == my_sym or board[2] == board[8] == my_sym or board[
        4] == board[6] == my_sym):
        return 5
    elif spaceIsFree(6) and (board[3] == board[9] == my_sym or board[4] == board[5] == my_sym):
        return 6
    elif spaceIsFree(7) and (
            board[1] == board[4] == my_sym or board[8] == board[9] == my_sym or board[5] == board[3] == my_sym):
        return 7
    elif spaceIsFree(8) and (board[2] == board[5] == my_sym or board[7] == board[9] == my_sym):
        return 8
    elif spaceIsFree(9) and (
            board[7] == board[8] == my_sym or board[3] == board[6] == my_sym or board[5] == board[1] == my_sym):
        return 9
    elif spaceIsFree(1) and (
            board[2] == board[3] == my_sym or board[4] == board[7] == my_sym or board[5] == board[9] == my_sym):
        return 1
    elif spaceIsFree(1) and spaceIsFree(2) and spaceIsFree(3) and spaceIsFree(4) and spaceIsFree(5) and spaceIsFree(
            6) and spaceIsFree(7) and spaceIsFree(8) and spaceIsFree(9):
        return random.randint(1, 9)

    if available_moves:
        return random.choice(available_moves)
    else:
        return None


def isBoardFull():
    return ' ' not in board[1:]


while True:
    printBoard(board)
    playerMove('X')
    if IsWinner(board, 'X'):
        printBoard(board)
        print("Player 'X' Wins!")
        break
    elif isBoardFull():
        printBoard(board)
        print("The game is a draw!")
        break

    printBoard(board)
    playerMove('O')
    if IsWinner(board, 'O'):
        printBoard(board)
        print("Player 'O' Wins!")
        break
    elif isBoardFull():
        printBoard(board)
        print("The game is a draw!")
        break


