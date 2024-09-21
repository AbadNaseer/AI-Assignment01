# metrics.py
def calculate_metrics(maze, path):
    return {
        "path_length": len(path),
        "energy_consumed": maze.energy - len(path),
        "nodes_explored": len(set(path)),
        "max_memory": len(path)  # Approximation based on path length
    }
