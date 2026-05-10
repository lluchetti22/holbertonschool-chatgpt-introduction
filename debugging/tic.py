def print_board(board):
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("---" * 3)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    # Returns True if there are no empty spaces left
    return all(cell != " " for row in board for cell in row)

def get_valid_input(prompt):
    # Enforces integer inputs strictly bound between 0 and 2
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1, 2]:
                return value
            print("Out of bounds. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        row = get_valid_input(f"Enter row (0, 1, or 2) for player {player}: ")
        col = get_valid_input(f"Enter column (0, 1, or 2) for player {player}: ")
        
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue
            
        board[row][col] = player
        
        # Check win state BEFORE swapping turns
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
            
        # Check tie state BEFORE swapping turns
        if is_board_full(board):
            print_board(board)
            print("The game is a draw!")
            break
            
        # Turn swapping logic safely positioned at the end
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
