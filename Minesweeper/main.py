from tkinter import *
from Minesweeper import settings
from Minesweeper import utils
from Minesweeper.cell import Cell

root = Tk()  # main function, a window
# Overriding settings of window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')  # witdhxheight
root.title("Minesweeper Python")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="black",  # Change later to black or color
    width=utils.width_percentage(100),
    height=utils.height_percentage(25)  # 180*4 = 720
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper',
    font=('Helvetica', 48)
)

game_title.place(
    x=utils.width_percentage(25),
    y=0
)

left_frame = Frame(
    root,
    bg="black",
    width=utils.width_percentage(25),
    height=utils.height_percentage(75)
)
left_frame.place(x=0, y=utils.height_percentage(25))

center_frame = Frame(
    root,
    bg="black",
    width=utils.width_percentage(75),
    height=utils.height_percentage(75)
)
center_frame.place(x=utils.width_percentage(25),
                   y=utils.height_percentage(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,
            row=y
        )
# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()

# Run the window
root.mainloop()
