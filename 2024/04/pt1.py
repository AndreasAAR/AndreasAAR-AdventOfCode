import numpy as np
import os


def count_xmas_with_numpy(grid):
    # Convert the grid to a NumPy array
    matrix = np.array([list(row) for row in grid])
    # Debug: Print the matrix shape
    print("Matrix shape:", matrix.shape)
    words = ["XMAS", "SAMX"]  # Check both the word and its reverse
    total_count = 0

    # Check horizontally
    for row in matrix:
        row_str = "".join(row)
        for word in words:
            total_count += row_str.count(word)

    # Check vertically
    for col in matrix.T:  # Transpose the matrix to iterate over columns
        col_str = "".join(col)
        for word in words:
            total_count += col_str.count(word)

    # Check diagonals (top-left to bottom-right)
    for offset in range(-matrix.shape[0] + 1, matrix.shape[1]):
        diagonal = "".join(np.diagonal(matrix, offset=offset))
        for word in words:
            total_count += diagonal.count(word)

    # Check diagonals (top-right to bottom-left)
    flipped_matrix = np.fliplr(matrix)  # Flip the matrix horizontally
    for offset in range(-flipped_matrix.shape[0] + 1, flipped_matrix.shape[1]):
        diagonal = "".join(np.diagonal(flipped_matrix, offset=offset))
        for word in words:
            total_count += diagonal.count(word)

    return total_count


def read_grid_from_file(file_path):
    # Read the grid from the text file
    with open(file_path, "r") as file:
        grid = [
            line.strip() for line in file if line.strip()
        ]  # Remove whitespace and empty lines
    return grid


file_path = file_path = os.path.join(os.path.dirname(__file__), "data.txt")
grid = read_grid_from_file(file_path)


result = count_xmas_with_numpy(grid)
print("Total XMAS occurrences:", result)
