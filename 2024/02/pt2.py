import os


def is_valid_step(curr, prev, prev_direction):

    diff = curr - prev
    abs_diff = abs(diff)

    # Check if difference exceeds maximum allowed value
    if abs_diff > 3 or abs_diff == 0:
        return False, None

    # Determine direction
    new_direction = 1 if diff > 0 else -1

    # Check for direction consistency
    if prev_direction is not None and new_direction != prev_direction:
        return False, None

    return True, new_direction


def can_fix_by_removing(lst):
    """Check if removing one element makes the list valid."""
    for i in range(len(lst)):
        # Create a new list without the current level
        modified_list = lst[:i] + lst[i + 1 :]
        if no_invalid_indices(modified_list):
            return True  # The modified list is valid
    return False


def no_invalid_indices(lst):
    """Collect indices of invalid steps in the list."""
    prev_direction = None

    for i in range(1, len(lst)):
        is_valid, prev_direction = is_valid_step(lst[i], lst[i - 1], prev_direction)
        if not is_valid:
            return False

    return True


def process_file_and_count_trends(file_path):
    """Process the file and count safe rows using Problem Dampener logic."""
    true_count = 0  # Counter for rows with consistent trends

    with open(file_path) as file:
        for line in file:
            # Parse the line into a list of numbers
            line = line.strip()
            numbers = list(map(int, line.replace(",", " ").split()))

            # Check if the sequence is valid or can be fixed by removing one level
            if no_invalid_indices(numbers) or can_fix_by_removing(numbers):
                true_count += 1

    return true_count


file_path = os.path.join(os.path.dirname(__file__), "data.txt")

print(process_file_and_count_trends(file_path))
