from tkinter import Tk, BOTH, Canvas
from graphics import *
from cell import *
from maze import *

def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 10, 10, 50, 50, win, 10)

    win.wait_for_close()

main()