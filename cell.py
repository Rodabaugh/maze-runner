from graphics import *

class Cell():
    def __init__(self, x1, y1, x2, y2, win=None):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.center = Point((x1+x2)//2, (y1+y2)//2)
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
    
    def draw(self):
        if self._win is None:
            return
        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        if self.has_left_wall == True:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")

        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        if self.has_right_wall == True:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")

        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        if self.has_top_wall == True:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")

        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.has_bottom_wall == True:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        line = Line(self.center, to_cell.center)
        fill_color = "red"
        if undo == True:
            fill_color = "gray"
        self._win.draw_line(line, fill_color)