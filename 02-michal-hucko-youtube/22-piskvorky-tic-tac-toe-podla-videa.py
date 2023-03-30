import sys


# === grid_handler ===
# vytvorenie hracieho pola (moze byt potom akosamostatny modul)
# vykreslenie pola
def print_grid(grid, rows, columns):
    print("  ", end="")  # len pre odsadenie 1. riadku
    # vypise 1. riadok s cislami
    for column in range(0, columns):
        print(column, end=" ")
    print()
    # print("") # to iste ako print()
    # vypise telo pola
    for row in range(0, rows):
        print(row, end=" ")  # vypis cisel pre kazdy riadok
        for column in range(0, columns):
            print(grid[row][column], end=" ")
        print()


# vytvorenie dvojrozmerneho pola
def create_grid(rows, columns, empty_sign="_"):
    # vytvorim prazdne pole typu list
    grid = []
    for row in range(0, rows):
        # vytvorim prazdny riadok
        grid.append([])
        # temp_row = [] # iny sposob
        # riadok naplnim symbolmi "_"
        for column in range(0, columns):
            grid[row].append(empty_sign)
            # temp_row.append(empty_sign)
        # grid.append(temp_row)
    return grid


# === input_handler ===
# funkcia na nacitavanie znakov z klavesnice
# musim importovat modul sys (import sys)
def get_input():
    while True:  # aby sme opakovali zadavanie vstupu pokial nebude spravny
        try:
            x = int(sys.stdin.readline())
        except Exception:  # nie idealne davat Exception (zachytavanie vsetkych chyb)
            print("Enter only integer value")
            continue
        break  # ak zada spravne tak ukonci cyklus while
    return x


# === game_handler ===
# funkcia na overenie ci hrac vyhral
def check_game(grid, rows, columns, player_symbol):
    # overenie pre riadky
    for row in range(0, rows):
        # porovnam ci sa v danom riadku nachadzaju 3 rovnake symboly
        # vytvorim si porovnavaci riadok (typu list) z 3 rovnakych symbolov
        # [player_symbol] * 3
        if grid[row] == [player_symbol] * 3:
            return True

    # overenie pre stlpce
    for column in range(0, columns):
        # vytvorim pomocnu premennu kde ulozim jednotlive prvky
        temp_col = []
        for row in range(0, rows):
            temp_col.append(grid[row][column])
        if temp_col == [player_symbol] * 3:
            return True

    # overenie pre diagonaly
    # !!! PLATI IBA PRE STVORCOVU HRACIU PLOCHU !!!
    # hlavna diagonala
    temp_list = []
    for row in range(0, rows):
        temp_list.append(grid[row][row])
    if temp_list == [player_symbol] * 3:
        return True
    # hlavna diagonala
    temp_list = []
    for row in range(0, rows):
        # !!! pozri len vztah pre vypocet indexu stlpca [rows - row - 1]
        temp_list.append(grid[row][rows - row - 1])
    if temp_list == [player_symbol] * 3:
        return True

    # ak nie je pravda
    return False


# === main ===
rows = 3
columns = 3
empty_sign = "_"  # na overenie ci neprepisujem zadany znak druheho hraca
# priradenie symbolov hracom
player_sym = {0: "x", 1: "o"}
grid = create_grid(rows, columns)
# premenna obsahujuca pocet vsetkych poli, resp. tahov
empty_places = rows * columns


# funkcia pre pocet a striedanie jednotlivych kol hry
# mame max pocet kol 5, pretoze 9 poli / 2 hraci a samozrejme zaokruhlenie nahor
move_counter = 0
# pomocna premenna pre ukoncenie hry
game_ended = False
for round_id in range(1, 6):
    print("Round no. is:", round_id)
    # striedanie hracov
    for player in range(0, 2):
        while (
            True
        ):  # pre if podmienky ci sa nachadzam v hracom poli a ci neprepisujem cudzie hodnoty
            print("Player", player, "turn")
            print_grid(grid, rows, columns)
            print("Enter the x coordinate")
            x = get_input()
            print("Enter the y coordinate")
            y = get_input()
            # podm ci sa nachadzam, resp. ci som zadal suradnice v rozsahu hracieho pola
            if x >= columns or x < 0 or y >= rows or y < 0:
                print("Coordinates out of range, please reenter")
                continue  # posuniem sa spat na zaciatok iteracie while cyklu
            # podm na overenie ci neprepisujem zadany znak druheho hraca
            if grid[x][y] != empty_sign:
                print("Coordinate is taken, choose another one")
                continue  # posuniem sa spat na zaciatok iteracie while cyklu
            else:
                break  # ukonci while cyklus
        # priradenie symbolu podla "iteracie" hraca
        # a prepisanie pola/grid podla zadanych x,y suradnic
        # grid[x][y] - prepisujem element v liste grid na pozicii x,y
        # player_sym[player] - nacitavam key hodnotu z dict player_sym podla
        # iteracie (player je ozn v cykle for in range(0, 2)), cize pre
        # player = 0 priradi symbol "x" player = 1 priradi symbol "o"
        grid[x][y] = player_sym[player]
        # podm na overenie vitazstva chech_game()
        if check_game(grid, rows, columns, player_sym[player]):
            print(f"Player {player} has won")
            game_ended = True
            print_grid(grid, rows, columns)
            break
        move_counter += 1
        # podm ak je vycerpany pocet volnych poli
        # plati pre hraca, teda este raz skopirujem podmienku a odsadim ju
        if move_counter == empty_places:
            print("Game over - Draw")
            print_grid(grid, rows, columns)
            break  # prerusi for cyklus pre hraca
    # odsadena a skopirovana podm
    if move_counter == empty_places:
        break  # prerusi for cyklus pre round_id
    # podmienka ukoncenia hry
    if game_ended is True:
        print("Congratulations!!")
        break


# print_grid(grid, rows, columns)
