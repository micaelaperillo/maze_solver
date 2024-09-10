# Maze Solver using A* Algorithm 
## Overview
This Python application demonstrates a maze-solving algorithm using the A* (A-Star) pathfinding algorithm, implemented in a graphical interface built with tkinter. The maze is randomly generated, and the user can interact with the grid by selecting start and goal points, triggering the A* algorithm to find and visualize the optimal path between the two points.

## Features
- Random Maze Generation: Each time you run the application or reset the maze, a new random maze is generated.
- Interactive GUI: Users can click on the grid to set start and goal points.
- A Algorithm Visualization*: The algorithm runs in real-time, showing cells as they are considered and the final path.

- Buttons for Control:
    - Start: Runs the A* algorithm to find the shortest path between selected points.
    - Reset: Clears the maze and removes the start, goal, and path cells.
    - New Maze: Generates a completely new maze.

## Getting Started
### Prerequisites
Ensure you have the following libraries installed:

`tkinter` (usually included in standard Python installations)
`numpy`
You can install numpy using pip if needed:
```bash
pip install numpy
```

## Running the Program
Clone or download the project files.

Run the Python script
```bash
python maze_solver.py
```
The main window will open, displaying a randomly generated maze.


## How to Use
Select Start and Goal:

- Left-click on any cell in the grid to select the start point (cell turns red).
- Left-click on another cell to set the goal point (cell turns blue).
- If you select more than two cells, the first selection will be cleared.

Run the Algorithm:

- Press the Start button to begin the A* algorithm, which will find the shortest path from the start to the goal.
- The considered cells will be highlighted in yellow, and the final path will be highlighted in green.

Reset the Maze:

- Click the Reset button to clear the selections and path, keeping the current maze.
Generate a New Maze:

- Click the New Maze button to generate a new maze and reset the grid.

**Pathfinding**: The A* algorithm works by exploring the shortest possible path using a heuristic based on Manhattan distance. Cells are explored based on their distance from the start point, with priority given to those that appear closer to the goal.

## License
This project is open source and available under the MIT License.