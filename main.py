import tkinter as tk
from tkinter import ttk
import numpy as np
from queue import PriorityQueue
import threading
from time import sleep

prob_of_side = 0.7
maze = np.random.choice([0, 1], size=(34, 34), p=[prob_of_side, 1 - prob_of_side])

root = tk.Tk()
root.title("Maze Solver using A* Algorithm")

icon = tk.PhotoImage(file="icon.png")
root.iconphoto(False, icon)

window_size = 850
cell_size = 25

canvas = tk.Canvas(root, width=window_size, height=window_size)
canvas.pack()

clicked_cells = []
path = []
considered_cells = []

# colors
red = "#FF2E00"
green = "#6DCA63"
black = "#232b2b"
gray = "#D3D3D3"
yellow = "#EEFC57"
blue = "#003459"
white = "#FFFFFF"

def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            color = black if maze[row][col] == 1 else gray
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=black)

def update_cell(cell, color):
    row, col = cell
    x1 = col * cell_size
    y1 = row * cell_size
    x2 = x1 + cell_size
    y2 = y1 + cell_size
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#282C35")

def on_canvas_click(event):
    col = event.x // cell_size
    row = event.y // cell_size
    if 0 <= row < maze.shape[0] and 0 <= col < maze.shape[1]:
        cell = (row, col)
        if cell in clicked_cells:
            clicked_cells.remove(cell)
            update_cell(cell, gray if maze[row][col] == 0 else black)
        else:
            if len(clicked_cells) < 2:
                clicked_cells.append(cell)
            else:
                old_cell = clicked_cells.pop(0)
                update_cell(old_cell, gray if maze[old_cell[0]][old_cell[1]] == 0 else black)
                clicked_cells.append(cell)
            update_cell(cell, red if len(clicked_cells) == 1 else blue)

def get_neighbors(cell):
    row, col = cell
    neighbors = []
    for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
        if 0 <= r < maze.shape[0] and 0 <= c < maze.shape[1]:
            if maze[r][c] == 0:
                neighbors.append((r, c))
    return neighbors

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal):
    global considered_cells
    considered_cells = []

    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while not open_set.empty():
        current = open_set.get()[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        considered_cells.append(current)
        update_cell(current, yellow)
        root.update_idletasks()

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                open_set.put((f_score[neighbor], neighbor))
        sleep(0.1)
    return []

def find_path():
    global path
    if len(clicked_cells) < 2:
        popup = tk.Toplevel()
        popup.title("Popup Window")
        popup.geometry("300x110")
        center_popup(popup, 300, 110)
        label = ttk.Label(popup, text="Please select exactly two cells")
        label.pack(pady=20)
        close_button = ttk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)
        return

    start = clicked_cells[0]
    goal = clicked_cells[1]

    def run_algorithm():
        global path
        path = a_star(start, goal)
        for cell in path:
            update_cell(cell, green)
        root.update_idletasks()
    threading.Thread(target=run_algorithm).start()

def center_popup(popup, width, height):
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    popup.geometry(f"{width}x{height}+{x}+{y}")

# Button handlers
def start():
    find_path()

def reset():
    global clicked_cells, path, considered_cells
    clicked_cells = []
    path = []
    considered_cells = []
    draw_maze()

def new_maze():
    global maze
    maze = np.random.choice([0, 1], size=(34, 34), p=[prob_of_side, 1 - prob_of_side])
    reset()

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=10)

start_button = tk.Button(button_frame, text="Start", command=start)
start_button.grid(row=0, column=0, padx=10)

reset_button = tk.Button(button_frame, text="Reset", command=reset)
reset_button.grid(row=0, column=2, padx=10)

new_maze_button = tk.Button(button_frame, text="New Maze", command=new_maze)
new_maze_button.grid(row=0, column=3, padx=10)

canvas.bind("<Button-1>", on_canvas_click)

draw_maze()

root.mainloop()
