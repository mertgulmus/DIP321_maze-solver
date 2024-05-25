# Team members:
# - Mert Gulmus (211ADB070)
# - Rustam Rahimov (211ADB058)
# - Pavlo Nikolaiev (201ADB090)

import os
import time

# Load from the text file
def loadMaze(filename):
    maze = []
    with open(filename, 'r') as f:
        for line in f:
            maze.append(list(line.strip())) # Append each line as a list of characters
    return maze

# Print the maze in text format
def printMaze(maze):
    for row in maze:
        print(''.join(row))

# Find the starting point 'S' in the maze
def findStart(maze):
    for y, row in enumerate(maze): # Loop through the rows, enumerate returns the index and the value
        for x, cell in enumerate(row): # Cells
            if cell == 'S':
                return x, y # Starting point found
    return None # Starting point not found

# Breadth-First Search (BFS) to solve the maze
def bfs(maze, start):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # 8 directions, including diagonals
    queue = [(start, [], 0)]  # Queue for nodes to be explored
    visited = set()  # Nodes that have been visited
    visited.add(start) # Add the starting point to the visited set

    while queue:
        (x, y), path, coins = queue.pop(0)  # Remove the first element from the queue

        for dx, dy in directions: # Check all 8 directions
            nx, ny = x + dx, y + dy # New coordinates

            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze): # Check if the new coordinates are within the maze
                if (nx, ny) not in visited and maze[ny][nx] != 'X': # Check if the new coordinates have not been visited and are not walls
                    new_coins = coins + (int(maze[ny][nx]) if maze[ny][nx].isdigit() else 0) # Add coins if there are any
                    if maze[ny][nx] == 'G':  # Goal reached
                        return path + [(nx, ny)], new_coins # Return the path and coins collected
                    queue.append(((nx, ny), path + [(nx, ny)], new_coins)) # Add the new coordinates to the queue
                    visited.add((nx, ny)) # Add the new coordinates to the visited set
    return None, 0

# Depth-First Search (DFS) to solve the maze
def dfs(maze, start):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    stack = [(start, [], 0)]  # Stack for nodes to be explored
    visited = set()
    visited.add(start)

    while stack:
        (x, y), path, coins = stack.pop() # Remove the last element from the stack

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):
                if (nx, ny) not in visited and maze[ny][nx] != 'X':
                    new_coins = coins + (int(maze[ny][nx]) if maze[ny][nx].isdigit() else 0) # Add coins
                    if maze[ny][nx] == 'G':  # Goal reached
                        return path + [(nx, ny)], new_coins
                    stack.append(((nx, ny), path + [(nx, ny)], new_coins))
                    visited.add((nx, ny))
    return None, 0

# Solve the maze using the specified method
def solveMaze(maze, method):
    start = findStart(maze)
    if not start:
        return None, 0  # No starting point found
    if method == 'bfs':
        return bfs(maze, start)
    elif method == 'dfs':
        return dfs(maze, start)
    else:
        raise ValueError("Invalid method. Use 'bfs' or 'dfs'.")

if __name__ == '__main__':
    mazes_folder = os.path.join(os.getcwd(), 'mazes')  # Folder containing maze files
    maze_files = [f for f in os.listdir(mazes_folder) if f.endswith('.txt')]

    for maze_file in maze_files:
        print(f"\nProcessing maze file: {maze_file}")
        maze = loadMaze(os.path.join(mazes_folder, maze_file))  # Load the maze

        start_time = time.time()  # Start timing
        path, coins = solveMaze(maze, 'bfs')  # Solve the maze using BFS
        end_time = time.time()  # End timing

        # Output the results
        if path:
            print(f"Path: {path}")
            print(f"Coins collected: {coins}")
        else:
            print("No solution found.")
        print(f"Execution time: {end_time - start_time} seconds")
