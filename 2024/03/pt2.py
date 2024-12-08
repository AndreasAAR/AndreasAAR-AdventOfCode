import os
import re


def process_corrupted_memory(corrupted_memory, mul_enabled):
    # Define regex pattern with named groups for each type of instruction
    combined_pattern = (
        r"(?P<mul>mul\(\s*(\d{1,4})\s*,\s*(\d{1,4})\s*\))|"
        r"(?P<do>do\(\))|"
        r"(?P<dont>don't\(\))"
    )

    # Find matches in the corrupted memory
    instructions = re.finditer(combined_pattern, corrupted_memory)

    total_sum = 0

    # Process each instruction in the order it appears
    for match in instructions:
        if match.lastgroup == "mul":  # It's a `mul(X, Y)` instruction
            if mul_enabled:
                x, y = int(match.group(2)), int(
                    match.group(3)
                )  # Groups 2 and 3 are the numbers
                total_sum += x * y
        elif match.lastgroup == "do":  # It's a `do()` instruction
            mul_enabled = True
        elif match.lastgroup == "dont":  # It's a `don't()` instruction
            mul_enabled = False

    return total_sum, mul_enabled


def compute_total_from_file(file_path):
    total_sum = 0
    mul_enabled = True  # Start with `mul` instructions enabled for the entire file

    # Open and read the file line by line
    with open(file_path, "r") as file:
        for line in file:
            # Strip whitespace and compute the sum for the line
            line_sum, mul_enabled = process_corrupted_memory(line.strip(), mul_enabled)
            total_sum += line_sum

    return total_sum


file_path = os.path.join(os.path.dirname(__file__), "data.txt")
print(compute_total_from_file(file_path))
