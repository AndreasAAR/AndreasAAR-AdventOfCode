from collections import defaultdict
import re
import os


def load_rules_and_updates(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Dictionary to store rules: key is Y, value is a set of Xs
    rules_dict = defaultdict(set)
    updates = []
    parsing_updates = False  # Toggle to switch between parsing rules and updates

    for line in lines:
        line = line.strip()
        if not line:
            parsing_updates = True  # Empty line indicates the start of updates
            continue

        if parsing_updates:
            # Parse updates (list of numbers separated by commas)
            updates.append(list(map(int, line.split(","))))
        else:
            # Parse rules (pairs of numbers)
            match = re.findall(r"(\d{2})\|(\d{2})", line)
            for a, b in match:
                rules_dict[int(b)].add(int(a))  # Add X (a) to the set of Y (b)

    return rules_dict, updates


def validate_number_list(rules_dict, number_list):

    for i, current_number in enumerate(number_list):
        # If current_number has rules, check all upcoming numbers
        if current_number in rules_dict:
            required_preceding_numbers = rules_dict[current_number]
            for later_number in number_list[i + 1 :]:  # Check numbers that come later
                if later_number in required_preceding_numbers:
                    # Rule broken: a required preceding number appears after the current number
                    return None
    return number_list  # Return the list if all rules are satisfied


def filter_valid_updates(rules_dict, updates):
    valid_updates = []

    for update in updates:
        valid_update = validate_number_list(rules_dict, update)
        if valid_update is not None:  # Only save valid updates
            valid_updates.append(valid_update)

    return valid_updates


def sum_middle_numbers(updates):

    middle_sum = 0

    for update in updates:
        # Find the middle index
        middle_index = len(update) // 2
        # Add the middle number to the sum
        middle_sum += update[middle_index]

    return middle_sum


file_path = os.path.join(os.path.dirname(__file__), "data.txt")

rules, updates = load_rules_and_updates(file_path)


valid_updates = filter_valid_updates(rules, updates)


print(sum_middle_numbers(valid_updates))
