from cell import *
from time import sleep

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self.cells = list()

        self._create_cells()

    def _create_cells(self):

        for col in range(0, self.num_cols):
            self.cells.append(list())
            for row in range(0, self.num_rows):
                x1 = self.x1+(col*self.cell_size_x)
                y1 = self.y1+(row*self.cell_size_y)
                x2 = self.x1+((col+1)*self.cell_size_x)
                y2 = self.y1+((row+1)*self.cell_size_y)
                self.cells[col].append(Cell(x1, y1, x2, y2, self._win))
        if self._win != None:
            self._draw_cells()
        
    def _draw_cells(self):
        for col in self.cells:
            for cell in col:
                cell.draw()
                self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.05)