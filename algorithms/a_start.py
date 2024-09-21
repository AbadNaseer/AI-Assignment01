# a_star.py
import heapq
from utils.helpers import is_valid_move, calculate_energy_cost, heuristic

def a_star(maze):
    queue = [(0, 0, 0, maze.energy, [(0, 0)])]  # (f_cost, x, y, energy, path)
    visited = set()

    while queue:
        f_cost, x, y, energy, path = heapq.heappop(queue)
        if (x, y) in visited or energy <= 0:
            continue
        visited.add((x, y))
        
        if (x, y) == (maze.size - 1, maze.size - 1):  # Goal reached
            return path
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, maze, energy):
                energy_cost = calculate_energy_cost(nx, ny, maze)
                h_cost = heuristic(nx, ny, maze)
                f_cost = energy_cost + h_cost
                heapq.heappush(queue, (f_cost, nx, ny, energy - energy_cost, path + [(nx, ny)]))
    return None
