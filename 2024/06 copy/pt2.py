import os

import pt1
from pt1 import Direction, Position


def creates_loop(position_map, guard, blocked_position):
    """
    Check if blocking `blocked_position` creates a loop.
    """
    # Temporarily mark the position as an obstacle
    if blocked_position not in position_map:
        raise ValueError(
            f"Blocked position {blocked_position} not found in position_map"
        )

    original_shape = position_map[blocked_position].shape
    position_map[blocked_position].shape = "obstacle"

    rows = max(pos.x for pos in position_map.keys()) + 1
    cols = max(pos.y for pos in position_map.keys()) + 1

    def is_within_bounds(pos):
        return 0 <= pos.x < rows and 0 <= pos.y < cols

    def is_obstacle(pos):
        return (
            position_map.get(pos, Position(pos.x, pos.y, shape="out_of_bounds")).shape
            == "obstacle"
        )

    # Define movement deltas for each direction
    direction_deltas = {
        Direction.UP: (-1, 0),
        Direction.DOWN: (1, 0),
        Direction.LEFT: (0, -1),
        Direction.RIGHT: (0, 1),
    }

    # Start simulation
    guard_state = (guard.position.x, guard.position.y, guard.direction)
    visited_in_simulation = {guard_state}  # Track visited states during this simulation

    is_loop = False

    while True:
        # Determine the next position
        delta_x, delta_y = direction_deltas[guard.direction]
        next_position = Position(guard.position.x + delta_x, guard.position.y + delta_y)

        # Stop if the guard leaves the mapped area
        if not is_within_bounds(next_position):
            break

        # Check if the next position is out of bounds or an obstacle
        if is_obstacle(next_position):
            guard.turn_clockwise()
        else:
            # Move forward if the path is clear
            guard.position = next_position
            guard_state = (guard.position.x, guard.position.y, guard.direction)

            # Check if the guard revisits a state already recorded
            if guard_state in visited_in_simulation:
                is_loop = True  # A loop is created
                break

            # Mark the current state in the simulation
            visited_in_simulation.add(guard_state)

    # Restore the original state of the blocked position
    position_map[blocked_position].shape = original_shape
    return is_loop


def count_loops(position_map, guard, visited_positions, visit_order):
    loops = 0

    # Skip the first position in `visit_order` (the guard's starting position)
    for blocked_position in visit_order[1:]:
        # Find the index of the blocked position in the visit order
        blocker_index = visit_order.index(blocked_position)

        # Get the position just before the blocked position
        if blocker_index > 0:
            start_position = visit_order[blocker_index - 1]

            # Ensure guard.position is set correctly and access `visited_positions` using tuples
            guard.position = start_position  # Convert tuple to Position
            guard.direction = visited_positions[start_position]["direction"]

        # Check if blocking this position creates a loop
        if creates_loop(position_map, guard, blocked_position):
            loops += 1

    return loops


# Example usage
file_path = os.path.join(os.path.dirname(__file__), "data_06.txt")
print(f"Processing file at: {file_path}")
print(f"Processing file at: {os.path.abspath(file_path)}")

position_map, guard = pt1.process_matrix(file_path)
visited_positions, visit_order = pt1.simulate_guard_patrol(position_map, guard)
loop_count = count_loops(position_map, guard, visited_positions, visit_order)

print(loop_count)


# Print the results
