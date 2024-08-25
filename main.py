from tkinter import Tk, BOTH, Canvas
from window import *

win = Window(800, 600)

line1 = Line(Point(10,10), Point(200,200))
line2 = Line(Point(10,200), Point(200, 10))

win.draw_line(line1, "red")
win.draw_line(line2, "black")

win.wait_for_close()