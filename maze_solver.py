import os
import time
from collections import deque

# Function to load the maze from a text file
def loadMaze(filename):
    maze = []
    with open(filename, 'r') as f:
        for line in f:
            maze.append(list(line.strip()))
    return maze

# Function to print the maze in a readable format
def printMaze(maze):
    for row in maze:
        print(''.join(row))

# Function to find the starting point 'S' in the maze
def findStart(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                return x, y
    return None

# Function to solve the maze using Breadth-First Search (BFS)
def bfs(maze, start):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    queue = deque([(start, [], 0)])  # Queue to manage nodes to be explored
    visited = set()  # Set to track visited nodes
    visited.add(start)

    while queue:
        (x, y), path, coins = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):
                if (nx, ny) not in visited and maze[ny][nx] != 'X':
                    new_coins = coins + (int(maze[ny][nx]) if maze[ny][nx].isdigit() else 0)
                    if maze[ny][nx] == 'G':  # Goal
                        return path + [(nx, ny)], new_coins
                    queue.append(((nx, ny), path + [(nx, ny)], new_coins))
                    visited.add((nx, ny))
    return None, 0

# Function to solve the maze using Depth-First Search (DFS)
def dfs(maze, start):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    stack = [(start, [], 0)]  # Stack to manage nodes to be explored
    visited = set()  # Set to track visited nodes
    visited.add(start)

    while stack:
        (x, y), path, coins = stack.pop()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):
                if (nx, ny) not in visited and maze[ny][nx] != 'X':
                    new_coins = coins + (int(maze[ny][nx]) if maze[ny][nx].isdigit() else 0)
                    if maze[ny][nx] == 'G':  # Goal
                        return path + [(nx, ny)], new_coins
                    stack.append(((nx, ny), path + [(nx, ny)], new_coins))
                    visited.add((nx, ny))
    return None, 0

def solveMaze(maze, method):
    # Function to solve the maze using the specified method ('bfs' or 'dfs')
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
