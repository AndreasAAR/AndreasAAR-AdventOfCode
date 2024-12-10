import numpy as np
import os


def count_x_patterns(grid):
    # Convert the grid to a NumPy array
    matrix = np.array([list(row) for row in grid])
    rows, cols = matrix.shape
    total_count = 0

    # Define valid patterns
    valid_patterns = {"MAS", "SAM"}

    # Check every possible center for the "X" pattern
    for i in range(1, rows - 1):  # Center A can't be on the edges
        for j in range(1, cols - 1):  # Same for columns
            # Check diagonals forming the "X" pattern
            try:
                # Top-left to bottom-right diagonal
                diag1 = matrix[i - 1, j - 1] + matrix[i, j] + matrix[i + 1, j + 1]
                # Top-right to bottom-left diagonal
                diag2 = matrix[i - 1, j + 1] + matrix[i, j] + matrix[i + 1, j - 1]

                # Count valid "X-MAS" patterns
                if diag1 in valid_patterns and diag2 in valid_patterns:
                    total_count += 1

            except IndexError:
                # Ignore out-of-bound errors (edges already excluded, but just in case)
                continue

    return total_count


def read_grid_from_file(file_path):
    # Read the grid from the text file
    with open(file_path, "r") as file:
        grid = [
            line.strip() for line in file if line.strip()
        ]  # Remove whitespace and empty lines
    return grid


# File path to the grid
file_path = os.path.join(os.path.dirname(__file__), "data.txt")
grid = read_grid_from_file(file_path)

# Count X patterns
result = count_x_patterns(grid)
print("Total X-MAS patterns:", result)
