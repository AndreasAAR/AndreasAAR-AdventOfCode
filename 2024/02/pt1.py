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


def is_consistent_trend(lst):

    prev_direction = None  # Initialize direction as unset
    faulty_steps = 0

    for i in range(1, len(lst)):
        is_valid, new_direction = is_valid_step(lst[i], lst[i - 1], prev_direction)

        if not is_valid:
            faulty_steps += 1  # Invalid step found
        prev_direction = new_direction  # Update direction for the next iteration

    return True


def process_file_and_count_trends(file_path):

    true_count = 0  # Counter for rows with consistent trends

    with open(file_path) as file:
        for line in file:
            # Parse the line into a list of numbers
            line = line.strip()

            numbers = list(map(int, line.replace(",", " ").split()))

            # Apply the trend check function
            if is_consistent_trend(numbers):
                true_count += 1

    return true_count


file_path = os.path.join(os.path.dirname(__file__), "data.txt")

print(process_file_and_count_trends(file_path))
