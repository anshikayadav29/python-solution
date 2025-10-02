from collections import deque

# Maze Solver using BFS
def solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    parent = {}

    # Possible moves (Up, Down, Left, Right)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # BFS queue
    q = deque([start])
    visited[start[0]][start[1]] = True

    while q:
        r, c = q.popleft()

        if (r, c) == end:
            # Reconstruct path
            path = []
            while (r, c) != start:
                path.append((r, c))
                r, c = parent[(r, c)]
            path.append(start)
            return path[::-1]

        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                parent[(nr, nc)] = (r, c)
                q.append((nr, nc))

    return None


# 0 = free path, 1 = wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path = solve_maze(maze, start, end)

print("Maze:")
for row in maze:
    print(row)

if path:
    print("\nShortest Path from", start, "to", end, ":")
    print(path)
else:
    print("No path found")
