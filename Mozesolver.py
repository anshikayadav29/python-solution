from collections import deque

def is_valid_move(maze, visited, row, col):
    return (0 <= row < len(maze)) and (0 <= col < len(maze[0])) and (maze[row][col] == 1) and (not visited[row][col])

def bfs_shortest_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start, [start])])  # (current_position, path)

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        (row, col), path = queue.popleft()

        if (row, col) == end:
            return path

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(maze, visited, new_row, new_col):
                visited[new_row][new_col] = True
                queue.append(((new_row, new_col), path + [(new_row, new_col)]))

    return None

# Maze: 1 = open path, 0 = wall
maze = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1]
]

start = (0, 0)
end = (4, 4)
path = bfs_shortest_path(maze, start, end)

if path:
    print("Shortest Path Found 🧩:")
    for step in path:
        print(step)
else:
    print("No Path Found 🚫")
