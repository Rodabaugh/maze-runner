from sys import setrecursionlimit
from graphics import Window
from maze import Maze
from constraints import *

def main():
    win = Window(screen_x, screen_y)
    setrecursionlimit(10000)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    if maze.solve():
        print("The maze was solved!")
    else:
        print("We faild to solve the maze")

    win.wait_for_close()

main()