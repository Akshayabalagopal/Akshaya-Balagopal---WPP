'''1. Consider the 8 queen's problem, it is a 8*8 chess board
where you need to place queens according to the following
constraints.
a. Each row should have exactly only one queen.
b. Each column should have exactly only one queen.
c. No queens are attacking each other.
'''

import numpy as np

# Check if it's safe to place a queen at (row, col)
def is_safe(board, row, col):
    # Check the column
    if col in board[:row]:
        return False
    
    # Check the diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    
    return True

# Function to solve the N-Queens problem using backtracking
def solve_n_queens(board, row):
    n = len(board)
    
    # If all queens are placed, print the board
    if row == n:
        print_board(board)
        return True  # Stop after the first solution

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col  # Place queen at (row, col)
            if solve_n_queens(board, row + 1):  # Recur to place queens in the next row
                return True  # Stop after the first solution
            board[row] = -1  # Backtrack if solution doesn't work

    return False

# Print the chessboard
def print_board(board):
    n = len(board)
    for row in range(n):
        line = ['Q' if col == board[row] else '.' for col in range(n)]
        print(' '.join(line))
    print("\n")

# Main function to initiate the N-Queens solution
def solve_n_queens_problem(n):
    board = np.full(n, -1)  # Initialize board with -1 (empty)
    if not solve_n_queens(board, 0):
        print(f"No solution found for {n}-Queens problem.")
        
# Driver code: User input for the size of the chessboard
if __name__ == "__main__":
    try:
        n = int(input("Enter the size of the chessboard (N) for the N-Queens problem: "))
        if n < 4:
            print("There are no solutions for N < 4.")
        else:
            solve_n_queens_problem(n)
    except ValueError:
        print("Invalid input! Please enter a valid integer for the size of the board.")


