import os

from collections import Counter


def read_file_to_lists(file_path):
    left_list = []
    right_list = []

    # Open the file and read it line by line
    with open(file_path, "r") as file:
        for line in file:
            # Split the line into two numbers
            tokens = line.strip().split()
            if len(tokens) == 2:  # Ensure the line has exactly two tokens
                left_list.append(int(tokens[0]))
                right_list.append(int(tokens[1]))

    return left_list, right_list


def calculate_similarity_score(left_list, right_list):

    # Count occurrences of each number in the right list
    right_count = Counter(right_list)

    # Calculate similarity score
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_count.get(num, 0)

    return similarity_score


print("test")
# Example usage
file_path = os.path.join(os.path.dirname(__file__), "data.txt")
left, right = read_file_to_lists(file_path)

left.sort()
right.sort()
print(sum_absolute_differences(left, right))
