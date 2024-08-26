from cell import *
from time import sleep
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = list()

        self._create_cells()
        self._break_entrance_and_exit()

        if seed != None:
            random.seed(seed)
        self._break_walls_r(1, 1)

    def _create_cells(self):
        for col in range(0, self.num_cols):
            self._cells.append(list())
            for row in range(0, self.num_rows):
                x1 = self.x1+(col*self.cell_size_x)
                y1 = self.y1+(row*self.cell_size_y)
                x2 = self.x1+((col+1)*self.cell_size_x)
                y2 = self.y1+((row+1)*self.cell_size_y)
                self._cells[col].append(Cell(x1, y1, x2, y2, self._win))
                if self._win != None:
                    self._draw_cell(col,row)
        
    def _draw_cell(self, col, row):
        self._cells[col][row].draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
            self._cells[0][0].has_top_wall = False
            self._draw_cell(0, 0)
            self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
            self._draw_cell(self.num_cols - 1, self.num_rows - 1)
    
    def _break_walls_r(self, col, row):
        self._cells[col][row].visited = True
        while True:
            pending_indexes = list()
            
            if col > 0 and not self._cells[col - 1][row].visited:
                pending_indexes.append((col - 1, row))
            
            if col < self.num_cols -1 and not self._cells[col + 1][row].visited:
                pending_indexes.append((col + 1, row))
            
            if row > 0 and not self._cells[col][row - 1].visited:
                pending_indexes.append((col, row - 1))

            if row < self.num_rows - 1 and not self._cells[col][row + 1].visited:
                pending_indexes.append((col, row + 1))

            if len(pending_indexes) == 0:
                self._draw_cell(col, row)
                return

            direction_index = random.randrange(len(pending_indexes))
            next_index = pending_indexes[direction_index]

            if next_index[0] == col + 1:
                self._cells[col][row].has_right_wall = False
                self._cells[col + 1][row].has_left_wall = False

            if next_index[0] == col - 1:
                self._cells[col][row].has_left_wall = False
                self._cells[col - 1][row].has_right_wall = False

            if next_index[1] == row + 1:
                self._cells[col][row].has_bottom_wall = False
                self._cells[col][row + 1].has_top_wall = False

            if next_index[1] == row - 1:
                self._cells[col][row].has_top_wall = False
                self._cells[col][row - 1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])