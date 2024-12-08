import os


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


def sum_absolute_differences(list1, list2):

    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")

    total_distance = 0
    for a, b in zip(list1, list2):
        total_distance += abs(a - b)

    return total_distance


print("test")
# Example usage
file_path = os.path.join(os.path.dirname(__file__), "data.txt")
left, right = read_file_to_lists(file_path)

left.sort()
right.sort()
print(sum_absolute_differences(left, right))
