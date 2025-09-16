def solve_n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # Check upper left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check upper right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def solve(row):
        if row == n:
            solutions.append(["".join(r) for r in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"
                solve(row + 1)
                board[row][col] = "."

    solve(0)
    return solutions


# Example usage
if __name__ == "__main__":
    n = 8   # Change N here for difficulty (8 is standard)
    result = solve_n_queens(n)
    print(f"Total solutions for {n}-Queens: {len(result)}")
    for sol in result[:3]:  # Print only first 3 solutions
        for row in sol:
            print(row)
        print()
