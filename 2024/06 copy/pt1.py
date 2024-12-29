from collections import defaultdict
import re
import os
import time

import pt1


from enum import Enum


def evaluate_with_optimized_dp(numbers, target):
    """
    Check if a combination of + and * operators can produce the target using dynamic programming with bounds.
    :param numbers: List of numbers.
    :param target: The target value.
    :return: True if target can be achieved, False otherwise.
    """

    # Start with the first number as the only possible result
    possible_results = {numbers[0]}

    # Iterate through the rest of the numbers

    for i, num in enumerate(numbers[1:], start=1):
        new_results = set()
        for result in possible_results:
            # Precompute results to avoid re-evaluation
            sum_result = result + num
            product_result = result * num

            # Add the current number
            if sum_result <= target:
                new_results.add(sum_result)

            # Multiply the current number
            if product_result <= target:
                new_results.add(product_result)

        possible_results = new_results

    # Final check
    return target in possible_results


def parse_and_evaluate(filepath):
    """
    Parse the file, extract the target and numbers, and evaluate using evaluate_with_optimized_dp.
    :param filepath: Path to the input file.
    :return: List of tuples (target, numbers, result) for each line.
    """
    result_sum = 0

    # Read the file and process each line
    with open(filepath, "r") as file:
        for line in file:
            # Remove leading/trailing whitespace
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Split the line at the colon
            parts = line.split(":")
            if len(parts) != 2:
                raise ValueError(f"Invalid line format: {line}")

            # Extract the target and numbers
            target = int(parts[0].strip())
            numbers = list(map(int, parts[1].strip().split()))

            # Evaluate the target and numbers
            if evaluate_with_optimized_dp(numbers, target):
                result_sum += target

    return result_sum


# Example usage
file_path = os.path.join(os.path.dirname(__file__), "data_07.txt")
print(parse_and_evaluate(file_path))

# Print the results
