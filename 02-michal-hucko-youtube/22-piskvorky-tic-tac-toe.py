import sys
import random
import os

# vytvorenie hracieho pola
# grid = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


# vykreslenie hracieho pola
def game_grid(grid):
    print("")
    print("  0 1 2")
    for row in range(0, len(grid)):
        print(row, end=" ")
        for col in range(0, len(grid)):
            print(grid[row][col], end=" ")
        print("")
    print("")


def player_name():
    print("1st player name:")
    player1_name = sys.stdin.readline().strip("\n")
    print("2nd player name")
    player2_name = sys.stdin.readline().strip("\n")
    return player1_name, player2_name


def player_order(tup_player_name):
    index = random.randint(0, 1)
    first_player = tup_player_name[index]
    if first_player == tup_player_name[0]:
        second_player = tup_player_name[1]
    else:
        second_player = tup_player_name[0]
    return first_player, second_player


def player_symbol(count):
    if count % 2 == 1:
        player_sym = "x"
    elif count % 2 == 0:
        player_sym = "o"
    return player_sym


def insert_to_grid(fgrid, count, row, col):
    if fgrid[row][col] != "_":
        print("You can not overwrite this value. Others symbol on this field")
    else:
        fgrid[row][col] = player_symbol(count)


def get_player_input(count, fi_player, se_player):
    if count % 2 == 1:
        print(f"{fi_player}: input row no.: ")
        row_y = sys.stdin.readline()
        print(f"{fi_player}: input col no.: ")
        col_x = sys.stdin.readline()
    elif count % 2 == 0:
        print(f"{se_player}: input row no.: ")
        row_y = sys.stdin.readline()
        print(f"{se_player}: input col no.: ")
        col_x = sys.stdin.readline()
    return int(col_x), int(row_y)


def intro():
    print("__________________________________________________________\n")
    print("WELCOME IN TIC-TAC-TOE GAME")
    print("__________________________________________________________\n")
    print("Please input PLAYERS NAME\n")
    first_player, second_player = player_order(player_name())
    print("__________________________________________________________\n")
    print(f"First player is: {first_player} and has symbol 'x'.")
    print(f"Second player is: {second_player} and has symbol 'o'.")
    print("__________________________________________________________\n")
    return first_player, second_player


def check_continue(g_grid):
    cont = False
    for row in range(0, len(g_grid)):
        for col in range(0, len(g_grid)):
            if g_grid[row][col] == "_":
                cont = True
    return cont


def check_winner(fgrid, f_player, s_player):
    winner = False
    # for rows
    for row in range(0, len(fgrid)):
        if fgrid[row][0] == fgrid[row][1] == fgrid[row][2] == "x":
            print(f"Winner is {f_player}")
            winner = True
        elif fgrid[row][0] == fgrid[row][1] == fgrid[row][2] == "o":
            print(f"Winner is {s_player}")
            winner = True
    # for columns
    for col in range(0, len(fgrid)):
        if fgrid[0][col] == fgrid[1][col] == fgrid[2][col] == "x":
            print(f"Winner is {f_player}")
            winner = True
        elif fgrid[0][col] == fgrid[1][col] == fgrid[2][col] == "o":
            print(f"Winner is {s_player}")
            winner = True
    # for diagonals
    if fgrid[0][0] == fgrid[1][1] == fgrid[2][2] == "x":
        print(f"Winner is {f_player}")
        winner = True
    elif fgrid[0][0] == fgrid[1][1] == fgrid[2][2] == "o":
        print(f"Winner is {s_player}")
        winner = True
    elif fgrid[0][2] == fgrid[1][1] == fgrid[2][0] == "x":
        print(f"Winner is {f_player}")
        winner = True
    elif fgrid[0][2] == fgrid[1][1] == fgrid[2][0] == "o":
        print(f"Winner is {s_player}")
        winner = True
    return winner


def main_game():
    grid = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    first_player, second_player = intro()
    count = 1
    while True:
        game_grid(grid)
        player_input = get_player_input(count, first_player, second_player)
        x_col, y_row = player_input
        try:
            insert_to_grid(grid, count, y_row, x_col)
        except IndexError:
            print("out of range")
        count += 1
        if check_winner(grid, first_player, second_player) is True:
            game_grid(grid)
            break
        if check_continue(grid) is False:
            print("GAME OVER - TWICE")
            game_grid(grid)
            break

    lets_continue = input("New GAME? [yes / no]: ")

    if lets_continue == "yes":
        os.system("clear")
        main_game()
    elif lets_continue == "no":
        os.system("clear")


main_game()
