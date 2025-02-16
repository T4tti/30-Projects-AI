# Tic Tac Toe AI using Minimax Algorithm

# Define the board as a list of 9 elements
board = [' ' for _ in range(9)] # 3x3 board

# Function to print the board
def print_board(board):
    for row in [board[i*3:(i + 1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check if a player has won
def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6] # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the game is a tie (no more empty spaces)
def check_tie(board):
    return ' ' not in board

# Function to evaluate the board for Minimax Algorithm
def evaluate(board):
    if check_win(board, 'O'): # AI is 'O'
        return 1
    elif check_win(board, 'X'): # Player is 'X'
        return -1
    else:
        return 0
    
# Function to implement Minimax Algorithm
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 1 or score == -1 or check_tie(board):
        return score

    if is_maximizing: # AI's turn
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O' # AI's move
                best_score = max(best_score, minimax(board, depth + 1, False))
                board[i] = ' ' # undo move
        return best_score
    else: # Player's turn
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X' # Player's move
                best_score = min(best_score, minimax(board, depth + 1, True))
                board[i] = ' ' # undo move
        return best_score
    
# Function to find the best move for AI
def find_best_move(board):
    best_value = -float('inf')
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' # AI's move
            move_value = minimax(board, 0, False)
            board[i] = ' ' # undo move
            if move_value > best_value:
                best_value = move_value
                best_move = i

    return best_move

# Main function to play the game
def play_game():
    while True:
        print_board(board)

        # Player's turn
        player_move = int(input('Enter your move (1-9): ')) - 1
        if board[player_move] != ' ':
            print('Invalid move!')
            continue
        board[player_move] = 'X'

        # Check if player has won
        if check_win(board, 'X'):
            print_board(board)
            print('Player wins!')
            break

        # Check if the game is a tie
        if check_tie(board):
            print_board(board)
            print('It\'s a tie!')
            break

        # AI's turn
        print('AI is thinking...')
        ai_move = find_best_move(board)
        board[ai_move] = 'O'

        # Check if AI has won
        if check_win(board, 'O'):
            print_board(board)
            print('AI wins!')
            break

        # Check if the game is a tie
        if check_tie(board):
            print_board(board)
            print('It\'s a tie!')
            break

# Play the game
play_game()



