# Step 1: Game Setup
board = [" " for _ in range(9)]

# Step 2: Player Moves
def player_move():
    valid_move = False
    while not valid_move:
        move = int(input("Enter your move (1-9): ")) - 1
        if move >= 0 and move < 9 and board[move] == " ":
            board[move] = "X"
            valid_move = True
        else:
            print("Invalid move. Try again.")

# Step 3: Minimax Algorithm
def minimax(board, depth, is_maximizing):
    scores = {
        "X": -1,
        "O": 1,
        "draw": 0
    }

    if evaluate(board) != 0:
        return scores[evaluate(board)]

    if is_maximizing:
        best_score = float("-inf")
        for move in range(9):
            if board[move] == " ":
                board[move] = "O"
                score = minimax(board, depth + 1, False)
                board[move] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for move in range(9):
            if board[move] == " ":
                board[move] = "X"
                score = minimax(board, depth + 1, True)
                board[move] = " "
                best_score = min(score, best_score)
        return best_score

# Step 4: Terminal State Evaluation
def evaluate(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return board[combo[0]]

    if " " not in board:
        return "draw"
    
    return 0

# Step 5: Recursive Search
def find_best_move(board):
    best_move = -1
    best_score = float("-inf")

    for move in range(9):
        if board[move] == " ":
            board[move] = "O"
            score = minimax(board, 0, False)
            board[move] = " "

            if score > best_score:
                best_score = score
                best_move = move

    return best_move

# Rest of the code remains the same as before...
