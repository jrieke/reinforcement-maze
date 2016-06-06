# From http://code.activestate.com/recipes/578356-random-maze-generator/
# Modified to use numpy and return maze instead of saving it as an image.

# Random Maze Generator using Depth-first Search
# http://en.wikipedia.org/wiki/Maze_generation_algorithm
# FB - 20121214


import random
import numpy as np

def make_maze(mx, my):
	maze = np.zeros((my, mx))
	dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0] # 4 directions to move in the maze
	# start the maze from (0, 0)
	stack = [(0, 0)]#[(random.randint(0, mx - 1), random.randint(0, my - 1))]

	while len(stack) > 0:
	    (cx, cy) = stack[-1]
	    maze[cy][cx] = 1
	    # find a new cell to add
	    nlst = [] # list of available neighbors
	    for i in range(4):
	        nx = cx + dx[i]; ny = cy + dy[i]
	        if nx >= 0 and nx < mx and ny >= 0 and ny < my:
	            if maze[ny][nx] == 0:
	                # of occupied neighbors must be 1
	                ctr = 0
	                for j in range(4):
	                    ex = nx + dx[j]; ey = ny + dy[j]
	                    if ex >= 0 and ex < mx and ey >= 0 and ey < my:
	                        if maze[ey][ex] == 1: ctr += 1
	                if ctr == 1: nlst.append(i)
	    # if 1 or more neighbors available then randomly select one and move
	    if len(nlst) > 0:
	        ir = np.random.choice(nlst)
	        cx += dx[ir]; cy += dy[ir]
	        stack.append((cx, cy))
	    else: stack.pop()

	return np.abs(maze.T - 1)  # transpose and invert 0s and 1s

if __name__ == '__main__':
	print make_maze(10, 10)
