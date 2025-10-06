import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Grid size
N = 50

# Random initial state (0 = dead, 1 = alive)
grid = np.random.choice([0, 1], size=(N, N))

def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Count alive neighbors
            total = int((
                grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]
            ))
            # Apply Conway’s rules
            if grid[i, j] == 1 and (total < 2 or total > 3):
                newGrid[i, j] = 0
            elif grid[i, j] == 0 and total == 3:
                newGrid[i, j] = 1
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img

# Set up plot
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='binary')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N), frames=200, interval=100, save_count=50)

plt.show()
