#Global Variables
board = [["-","-","-"],["-","-","-"],["-","-","-"]]
player = "X"
#prints board
def print_board():
    print("   0     1     2")
    print()
    counter = 0
    for row in board:
        print(str(counter) + " ", end="")
        counter += 1
        for cel in row:
            print(" " + cel + "    ", end="")
        print()
        print()

#returns true if a row,col entered by user is available move on board
def is_valid_move(row, col):
    output = False
    if row in [0,1,2] and col in [0,1,2]:
        output = True
    if board[row][col]  != "-":
        print("Error: Cel is occupied!")
        output = False
    return output
        
#places player on row,col of board
def place_player(player, row, col):
    board[row][col] = player
    
#Asks the user to enter a row and col until the user enters a valid location
#Adds user location to the board, and prints the board
def take_turn(player):
    valid = False
    while not valid:
        if player == "X":
            row = int(input("Enter a row "))
            col = int(input("Enter a col "))
            valid = is_valid_move(row, col)
        if player == "O":
            row = minimax("O")[1]
            col = minimax("O")[2]
            valid = is_valid_move(row, col)
            
        

    place_player(player, row, col)
    print_board()

#check win functions:
def check_col_win(player):
    output = False
    if board[0][0] == board[1][0] == board[2][0] == player:
        output = True
    if board[0][1] == board[1][1] == board[2][1] == player:
        output = True
    if board[0][2] == board[1][2] == board[2][2] == player:
        output = True
    return output

def check_row_win(player):
    output = False
    if board[0][0] == board[0][1] == board[0][2] == player:
        output = True
    if board[1][0] == board[1][1] == board[1][2] == player:
        output = True
    if board[2][0] == board[2][1] == board[2][2] == player:
        output = True
    return output

def check_diag_win(player):
    output = False
    if board[0][0] == board[1][1] == board[2][2] == player:
        output = True
    if board[0][2] == board[1][1] == board[2][0] == player:
        output = True
    return output

def check_win(player):
    return check_col_win(player) or check_row_win(player) or check_diag_win(player)

def check_tie():
    full = True
    for row in board:
        for cel in row:
            if cel == "-":
                full = False
    if not check_win("X") and not check_win("O") and full:
        return True
    else: 
        return False
    

#function to save all available spaces on board
def get_available_moves():
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                moves.append((i,j))
    return moves
optimalRow = -1
optimalCol = -1
#recursive function to maximize NPC gains and minimize user gains
def minimax(player):
    #
    #base case:
    if check_tie():
        return (0, None, None)
    elif check_win("X"):
        return(-10, None, None)
    elif check_win("O"):
        return (10, None, None)
    
    #recursive case
    if player == "O":
        best = -10000
        for coords in get_available_moves():
            board[coords[0]][coords[1]] = "O"
            score = minimax("X")[0]
            board[coords[0]][coords[1]] = "-"
            if best<score:
                best = max(best, score)
            
                optimalRow = coords[0]
                optimalCol = coords[1]
                
            
        return (best, optimalRow, optimalCol)
                
    if player == "X":
        worst = 10000
        for coords in get_available_moves():          
            board[coords[0]][coords[1]] = "X"
            score = minimax("O")[0]
            board[coords[0]][coords[1]] = "-"
            if worst>score:
                worst = min(worst, score)
                optimalRow = coords[0]
                optimalCol = coords[1]
            
        return (worst, optimalRow, optimalCol)
#function to switch from player to player in game        
def flip_player():
    global player, stop
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    else:
        print("Error: Player is not X or O")
        stop = True

#main code

print("\t\tWelcome to Tic Tac Toe!")
print_board()

stop = False
while not stop:
    print()
    print(f"Player {player} is up...")
    print()
    take_turn(player)
    print(22 * "=")
    print()
    if check_win(player):
        print(f"Player {player} wins !")
        break
    elif check_tie():
        print(f"It's a tie !")
        break
    flip_player()
    print_board()