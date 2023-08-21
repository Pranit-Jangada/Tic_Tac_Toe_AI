#step 3, 4 & 5 can be added according to user perspective, But I have added one snippet which you can use to run this code in an another commit in this same repo

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
    # Implementation of the minimax algorithm
    # (Please insert the minimax code provided in the previous response here)

# Step 4: Terminal State Evaluation
def evaluate(board):
    # Implementation of the evaluate function
    # (Please insert the evaluate code provided in the previous response here)

# Step 5: Recursive Search
def find_best_move(board):
    # Implementation of the find_best_move function
    # (Please insert the find_best_move code provided in the previous response here)

# Step 6: AI Move Selection
def ai_move():
    move = find_best_move(board)
    board[move] = "O"

# Step 7: Game Loop
def game_loop():
    while True:
        player_move()
        if evaluate(board) != 0:
            break

        ai_move()
        if evaluate(board) != 0:
            break

# Step 8: Display Board
def display_board():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)

# Step 9: End of Game
def end_game(result):
    display_board()
    if result == 1:
        print("You win!")
    elif result == -1:
        print("AI wins!")
    else:
        print("It's a draw!")

# Main
game_loop()
end_game(evaluate(board))
