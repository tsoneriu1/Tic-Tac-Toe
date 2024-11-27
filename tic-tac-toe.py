def draw_board(board):
    print('-------------')
    for i in range(3):
        print('|', end='')
        for j in range(3):
            print(f' {board[i*3+j]} |', end='')
        print('\n-------------')

def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]  # diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    for cell in board:
        if cell == ' ':
            return False
    return True

def main():
    board = [' '] * 9
    current_player = 'X'

    while True:
        draw_board(board)

        move = int(input(f"Player {current_player}'s turn. Enter a move (1-9): ")) - 1
        if board[move] == ' ':
            board[move] = current_player
        else:
            print("Invalid move. Try again.")
            continue

        if check_win(board, current_player):
            draw_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            draw_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()