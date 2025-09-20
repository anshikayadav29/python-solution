from collections import deque

def print_maze(maze):
    for row in maze:
        print(" ".join(str(cell) for cell in row))
    print()

def is_valid(maze, x, y, visited):
    return (0 <= x < len(maze) and 
            0 <= y < len(maze[0]) and 
            maze[x][y] == 0 and 
            not visited[x][y])

def bfs_shortest_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start, [start])])  # (current position, path)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path  # shortest path found

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_x, new_y = x + dx, y + dy
            if is_valid(maze, new_x, new_y, visited):
                visited[new_x][new_y] = True
                queue.append(((new_x, new_y), path + [(new_x, new_y)]))

    return None  # no path

# Example Maze (0 = open, 1 = wall)
maze = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0]
]

start = (0, 0)   # top-left
end = (4, 5)     # bottom-right

print("Maze:")
print_maze(maze)

path = bfs_shortest_path(maze, start, end)

if path:
    print("Shortest Path:", path)
else:
    print("No path found!")
