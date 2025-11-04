from collections import deque

def is_valid_move(maze, visited, x, y):
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 1 and not visited[x][y]

def shortest_path(maze, start, end):
    moves = [(1,0), (-1,0), (0,1), (0,-1)]  # Down, Up, Right, Left
    visited = [[False]*len(maze[0]) for _ in maze]
    queue = deque([(start[0], start[1], 0)])  # (x, y, distance)
    visited[start[0]][start[1]] = True

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == end:
            return dist

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(maze, visited, new_x, new_y):
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, dist + 1))

    return -1  # No path found

# Maze representation: 1 = path, 0 = wall
maze = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1]
]

start = (0, 0)
end = (3, 4)

path_length = shortest_path(maze, start, end)
print("Shortest Path Length:", path_length)
