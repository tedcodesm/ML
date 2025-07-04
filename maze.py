from collections import deque

# Define the maze (0 = empty space, 1 = wall)
maze = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
]

start = (0, 0)
goal = (4, 4)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS for shortest path
def bfs(maze, start, goal):
    queue = deque()     
    queue.append((start, [start]))
    visited = set()
    explored_states = []  # To keep track of explored states

    while queue:
        current, path = queue.popleft()
        explored_states.append(current)  # Record explored state

        if current == goal:
            return path, explored_states

        visited.add(current)

        for move in moves:
            r, c = current[0] + move[0], current[1] + move[1]
            next_pos = (r, c)

            if (0 <= r < len(maze) and 0 <= c < len(maze[0]) and
                maze[r][c] == 0 and next_pos not in visited):
                
                queue.append((next_pos, path + [next_pos]))
                visited.add(next_pos)

    return None, explored_states

# Find path and explored states
path, explored = bfs(maze, start, goal)

# Visualize maze
def print_maze(maze, path):
    for r in range(len(maze)):
        row = ""
        for c in range(len(maze[0])):
            if (r, c) == start:
                row += "S"
            elif (r, c) == goal:
                row += "G"
            elif maze[r][c] == 1:
                row += "#"
            elif path and (r, c) in path:
                row += "*"
            else:
                row += "."
        print(row)

# Show results
# Show results
if path:
    print("\n✅ Simplest Path Found:\n")
    print_maze(maze, path)
    print("\n📍 States Explored (x, y format):")
    for state in explored:
        print(f"({state[1]}, {state[0]})")  # Swap row and col to (x, y)
    print(f"\nTotal States Explored: {len(explored)}")
else:
    print("❌ No path found.")
    print("\n📍 States Explored (x, y format):")
    for state in explored:
        print(f"({state[1]}, {state[0]})")
    print(f"\nTotal States Explored: {len(explored)}")
