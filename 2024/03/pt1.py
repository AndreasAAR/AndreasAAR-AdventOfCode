import re
import os


def extract_and_compute_mul_sum(corrupted_memory):
    # Regex pattern for valid `mul(X,Y)` instructions
    pattern = r"mul\(\s*(\d{1,4})\s*,\s*(\d{1,4})\s*\)"

    # Find all matches in the corrupted memory
    matches = re.findall(pattern, corrupted_memory)

    # Compute the sum of the results of valid mul instructions
    total_sum = sum(int(x) * int(y) for x, y in matches)

    return total_sum


def compute_total_from_file(file_path):
    total_sum = 0

    # Open and read the file line by line
    with open(file_path, "r") as file:
        for line in file:
            # Strip whitespace and compute the sum for the line
            line_sum = extract_and_compute_mul_sum(line.strip())
            total_sum += line_sum

    return total_sum


file_path = os.path.join(os.path.dirname(__file__), "data.txt")
print(compute_total_from_file(file_path))
