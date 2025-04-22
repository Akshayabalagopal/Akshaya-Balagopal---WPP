import numpy as np
import random

# Check if the queens are attacking each other
def is_safe(board, n):
    # Check columns and diagonals
    for row in range(n):
        for prev_row in range(row):
            # Check if two queens are in the same column or on the same diagonal
            if board[row] == board[prev_row] or \
               abs(board[row] - board[prev_row]) == abs(row - prev_row):
                return False
    return True

# Function to place queens randomly and check if the solution is valid
def solve_random_queens(n):
    while True:
        # Randomly place queens in each row
        board = np.random.permutation(n)  # Randomly shuffle column positions for each row
        
        # Check if the placement is safe
        if is_safe(board, n):
            print_board(board, n)
            return board  # Return the valid board once found

# Print the chessboard
def print_board(board, n):
    for row in range(n):
        line = ['Q' if col == board[row] else '.' for col in range(n)]
        print(' '.join(line))
    print("\n")

# Driver code to solve the N-Queens problem with random placements
if __name__ == "__main__":
    try:
        n = int(input("Enter the size of the chessboard (N) for the N-Queens problem: "))
        if n < 4:
            print("There are no solutions for N < 4.")
        else:
            solve_random_queens(n)
    except ValueError:
        print("Invalid input! Please enter a valid integer for the size of the board.")
