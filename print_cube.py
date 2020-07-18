from tkinter import *
import cube

WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 1000

#def print_plane_cube(rubiks_cube):


def print_cube(rubiks_cube, solution):
    window = Tk()
    window.title("Rubik's Cube")

    window.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
    window.resizable(0,0)

    canvas = Canvas(window, width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
    canvas.pack()

 #   print_plane_cube(rubiks_cube)

    window.mainloop()
