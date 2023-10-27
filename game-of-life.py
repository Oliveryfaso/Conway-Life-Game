# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frameNum, img, grid, N):
    # copy grid to apply the rules
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # compute 8-neighbor sum
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]) / 255)
            # apply Conway's rules
            if grid[i, j] == ON:  # if cell is ON
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF  # cell dies
            else:  # if cell is OFF
                if total == 3:
                    newGrid[i, j] = ON  # cell lives
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img

# grid size
N = 100

# animation speed
speed = 200

# ON/OFF - 1/0 values
ON = 255  # alive
OFF = 0  # dead

# populate grid with random ON/OFF - more OFF than ON
grid = np.random.choice([ON, OFF], N*N, p=[0.2, 0.8]).reshape(N, N)

# create figure and axes
fig, ax = plt.subplots()

# display grid
img = ax.imshow(grid, interpolation='nearest')

# set up animation
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N),
                              frames=10, interval=speed, save_count=50)

plt.show()
