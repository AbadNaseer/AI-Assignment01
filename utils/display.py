# display.py
def display_path(maze, path):
    display_grid = maze.grid.copy()
    for x, y in path:
        if display_grid[x, y] not in ['A', 'G']:
            display_grid[x, y] = '*'
    for row in display_grid:
        print(' '.join(row))
