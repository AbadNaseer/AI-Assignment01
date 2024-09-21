# helpers.py
import math

def is_valid_move(x, y, maze, energy):
    return 0 <= x < maze.size and 0 <= y < maze.size and maze.grid[x, y] != '-' and energy > 0

def calculate_energy_cost(x, y, maze):
    return 3 if maze.grid[x, y] == 'O' else 1

def heuristic(x, y, maze):
    goal_x, goal_y = maze.size - 1, maze.size - 1
    return abs(goal_x - x) + abs(goal_y - y)  # Manhattan distance
