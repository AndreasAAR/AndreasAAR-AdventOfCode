from collections import defaultdict
import re
import os
import time

import pt1


from enum import Enum


class Position:
    def __init__(self, x, y, shape=None):
        self.x = x  # X-coordinate of the position
        self.y = y  # Y-coordinate of the position
        self.shape = shape  # Optional attribute to represent the shape or type of position (e.g., obstacle, open space)

    def __repr__(self):
        return f"Position(x={self.x}, y={self.y}, shape={self.shape})"

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))


class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class Guard:
    def __init__(self, position, direction):
        self.position = position  # (row, col) tuple for the guard's position
        self.direction = direction  # Enum value for the guard's current direction
        self.unique_visited = set()  # Set to store unique visited positions
        self.path_positions = []  # List to keep track of all positions visited

    def move(self):
        # Update position based on the current direction
        row, col = self.position

        if self.direction == Direction.UP:
            self.position = (row - 1, col)
        elif self.direction == Direction.DOWN:
            self.position = (row + 1, col)
        elif self.direction == Direction.LEFT:
            self.position = (row, col - 1)
        elif self.direction == Direction.RIGHT:
            self.position = (row, col + 1)

    def turn_clockwise(self):
        # Rotate the direction clockwise
        direction_order = [
            Direction.UP,
            Direction.RIGHT,
            Direction.DOWN,
            Direction.LEFT,
        ]

        current_index = direction_order.index(self.direction)
        self.direction = direction_order[(current_index + 1) % len(direction_order)]


def process_matrix(file_path):
    position_map = {}
    guard = None

    with open(file_path, "r") as file:

        for x, line in enumerate(file):
            line = line.strip()  # Remove leading/trailing whitespaces
            if not line:  # Skip empty lines
                continue
            # print(f"Processing line {x}: {line}")
            # print(f"Line {x}: {repr(line)}")  # Print the raw content
            for y, char in enumerate(line):
                position = Position(x, y)
                if char == "^":
                    # Create guard at the initial position
                    position.shape = "guard_start"
                    guard = Guard(position, direction=Direction.UP)
                    position_map[position] = position
                elif char == "#":
                    # Obstacle
                    position.shape = "obstacle"
                    position_map[position] = position
                elif char == ".":
                    # Open space
                    position.shape = "open_space"
                    position_map[position] = position

    if guard is None:
        raise ValueError(
            f"Guard start position (^) not found in the matrix! Double-check the input format."
        )

    print(f"Guard initialized at position: {guard.position}")
    return position_map, guard


def simulate_guard_patrol(position_map, guard):
    rows = max(pos.x for pos in position_map.keys()) + 1
    cols = max(pos.y for pos in position_map.keys()) + 1

    # Store visited positions as a dictionary with direction and visit order information
    visited_positions = {guard.position: {"direction": guard.direction, "step": 0}}
    visit_order = [guard.position]  # Store `Position` objects
    step_count = 0

    def is_within_bounds(pos):
        return 0 <= pos.x < rows and 0 <= pos.y < cols

    def is_obstacle(pos):
        return (
            position_map.get(pos, Position(pos.x, pos.y, shape="out_of_bounds")).shape
            == "obstacle"
        )

    while True:
        # Mark the current position with its direction and step count
        current_position = guard.position
        if current_position not in visited_positions:
            visited_positions[current_position] = {
                "direction": guard.direction,
                "step": step_count,
            }
            visit_order.append(current_position)

        # Determine the next position based on the current direction
        if guard.direction == Direction.UP:
            next_position = Position(guard.position.x - 1, guard.position.y)
        elif guard.direction == Direction.DOWN:
            next_position = Position(guard.position.x + 1, guard.position.y)
        elif guard.direction == Direction.LEFT:
            next_position = Position(guard.position.x, guard.position.y - 1)
        elif guard.direction == Direction.RIGHT:
            next_position = Position(guard.position.x, guard.position.y + 1)

        # Check if the next position is out of bounds or an obstacle
        if is_obstacle(next_position):
            # Turn right (clockwise) if there's an obstacle or it's out of bounds
            guard.turn_clockwise()
        else:
            # Move forward if the path is clear
            guard.position = next_position
            guard.path_positions.append((next_position.x, next_position.y))

        step_count += 1

        # Stop if the guard leaves the mapped area
        if not is_within_bounds(guard.position):
            break

    # Return visited positions with order and directions, and the visit order
    return visited_positions, visit_order


# Example usage
file_path = os.path.join(os.path.dirname(__file__), "data_06.txt")
print(f"Processing file at: {file_path}")
print(f"Processing file at: {os.path.abspath(file_path)}")

position_map, guard = process_matrix(file_path)
visited_positions, visit_order = simulate_guard_patrol(position_map, guard)
print(len(visited_positions))
# Print the results
