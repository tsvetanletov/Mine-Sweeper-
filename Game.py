
from tkinter import *
from Cell import Cell
import Settings
import Utils

root = Tk()
#Override the settings of teh window
root.configure(bg="black")
root.geometry(f"{Settings.WIDTH}x{Settings.HEIGHT}")
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="black" ,
    width=Settings.WIDTH,
    height=Utils.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg="black",
    fg="white",
    text="MInesweeper Game",
    font=("", 48)
)

game_title.place(
    x=Utils.width_prct(25), y=0
)
left_frame = Frame(
    root,
    bg="black" ,
    width=Utils.width_prct(25),
    height=Utils.height_prct(75)

)
left_frame.place(x=0, y=Utils.height_prct(25))

center_frame = Frame(
    root,
    bg="black",
    width=Utils.width_prct(75),
    height=Utils.height_prct(75)

)
center_frame.place(
    x=Utils.width_prct(25),
    y=Utils.height_prct(25)
)

for x in range(Settings.GRID_SIZE):
    for y in range(Settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )
#Call the label from teh Cell class

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)


Cell.randomize_mines()



#Rund the window
root.mainloop()