def draw_board(board, N):
    for i in range(N):
        print('---+' * (N - 1) + '---')
        print('|', end='')
        for j in range(N):
            print(f' {board[i*N+j]} |', end='')
        print('\n')
    print('---+' * (N - 1) + '---')

def check_win(board, N, player):
    # Check rows
    for i in range(N):
        if all(board[i*N+j] == player for j in range(N)):
            return True

    # Check columns
    for j in range(N):
        if all(board[i*N+j] == player for i in range(N)):
            return True

    # Check diagonals
    if all(board[i*N+i] == player for i in range(N)):
        return True
    if all(board[i*N+(N-i-1)] == player for i in range(N)):
        return True

    return False

def check_draw(board, N):
    for i in range(N * N):
        if board[i] == ' ':
            return False
    return True



def main():
    N = int(input("Enter the board size (N): "))
    board = [' '] * N * N
    current_player = 'X'

    while True:
        draw_board(board, N)

        move = int(input(f"Player {current_player}'s turn. Enter a move (1-{N*N}): ")) - 1
        if board[move] == ' ':
            board[move] = current_player
        else:
            print("Invalid move. Try again.")
            continue

        if check_win(board, N, current_player):
            draw_board(board, N)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board, N):
            draw_board(board, N)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'




if __name__ == "__main__":
    main()