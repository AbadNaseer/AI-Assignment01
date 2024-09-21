# iddfs.py
from utils.helpers import is_valid_move, calculate_energy_cost

def iddfs(maze, max_depth):
    def dfs(x, y, depth, path, energy):
        if (x, y) == (maze.size - 1, maze.size - 1):  # Goal reached
            return path
        if depth == 0 or energy <= 0:
            return None

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, maze, energy):
                energy_cost = calculate_energy_cost(nx, ny, maze)
                result = dfs(nx, ny, depth - 1, path + [(nx, ny)], energy - energy_cost)
                if result:
                    return result
        return None

    for depth in range(max_depth):
        result = dfs(0, 0, depth, [(0, 0)], maze.energy)
        if result:
            return result
    return None
