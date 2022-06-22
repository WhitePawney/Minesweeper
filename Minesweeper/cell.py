from tkinter import Button, Label
import random
from Minesweeper import settings
import ctypes                   # for throwing generic messages
import sys

class Cell:
    # Init the list of cells
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    # CALL CONSTRUCTOR
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_open = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        # setOnClickListener kind of function
        btn.bind('<Button-1>',
                 self.left_click_actions)  # Convention of saying left click, and just passing reference to function
        btn.bind('<Button-3>', self.right_click_actions)  # Button3 is right click
        self.cell_btn_object = btn

    @staticmethod  # method just for usecase of class and not for usecase of the instance
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells left: {Cell.cell_count}",
            font=("Helvetica", 20)
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # IF mines count == cells_left count, player wins
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(
                    0,
                    'Congratulations! You Won',  # body of msg box
                    'Game Over',  # title of msg box
                    0  # only 1 option for button to click which is "OK"
                )

        # DISABLE LEFT AND RIGHT CLICK EVENTS IF CELL IS ALREADY OPENED
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')


    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'   # gray85 for Linux
            )
            self.is_mine_candidate = False

    def get_cell_by_axis(self, x, y):
        # RETURN A CELL OBJECT BASED ON THE VALUES OF X and Y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [
            cell for cell in cells if cell is not None  # list comprehension
        ]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        # print(self.surrounded_cells_mines_length)
        if not self.is_open:
            Cell.cell_count -=1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # Replace the text of cell count label with the newer value
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Cells left: {Cell.cell_count}")
            # If this was a mine candidate, then for safety we should
            # configure the background colour to default
            self.cell_btn_object.configure(bg='SystemButtonFace')

        # Mark the cell is opened (Use is as the last line of this method)
        self.is_open = True

    def show_mine(self):
        # A logic to interrupt game and display message of losing
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(
            0,
            'You clicked on a mine',    # body of msg box
            'Game Over',    # title of msg box
            0   # only 1 option for button to click which is "OK"
        )
        sys.exit()

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        for picked_cells in picked_cells:
            picked_cells.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
