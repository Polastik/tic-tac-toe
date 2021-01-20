the_board = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}
board_keys = []
separator = "=" * 80

for key in the_board:
    board_keys.append(key)

print(separator)
print("Welcome to Tic Tac Toe".center(80," "))
print(separator)
print("""GAME RULES:
Each player can place one mark (or stone) per turn on the 3x3 grid
The WINNER is who succeeds in placing three of their marks in a
* horizontal,
* vertical or
* diagonal row""")
print(separator)


print("start the game:")
def print_board(board):
    print(separator)
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print(separator)

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        print_board(the_board)
        print("It's your turn," + turn + ".Move your stone!")

        move = input()

        while move not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            move  = input("Choose a position from 1-9")

        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nplace your stone elsewhere!")
            continue

        if count >= 5:
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ':
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['7'] == the_board['5'] == the_board['3'] != ' ':
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do you want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            the_board[key] = " "
        game()

if __name__ == "__main__":
    game()
