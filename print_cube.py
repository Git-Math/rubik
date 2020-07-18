from tkinter import *
import cube

WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 1000
SQUARE_SIZE = 70
FACE_SIZE = 3 * SQUARE_SIZE
START_UP_FACE_X = WINDOW_WIDTH / 2 - FACE_SIZE
START_UP_FACE_Y = WINDOW_HEIGHT / 10
FACE_BORDER_WIDTH = 3

color_dict = {
    "y": "yellow",
    "w": "white",
    "g": "green",
    "b": "blue",
    "r": "red",
    "o": "orange"
}

def print_face(canvas, start_x, start_y, face):
    face_rectangle_list = []
    y = start_y
    for line in face.face:
        line_rectangle_list = []
        x = start_x
        for square in line:
            line_rectangle_list.append(canvas.create_rectangle(x, y, x + SQUARE_SIZE, y + SQUARE_SIZE, fill=color_dict[square.color]))
            x += SQUARE_SIZE
        face_rectangle_list.append(line_rectangle_list)
        y += SQUARE_SIZE
    canvas.create_rectangle(start_x, start_y, start_x + FACE_SIZE, start_y + FACE_SIZE, width=FACE_BORDER_WIDTH)
    return face_rectangle_list

def print_plane_cube(canvas, rubiks_cube):
    rectangle_list_dict = {}
    start_x = START_UP_FACE_X
    start_y = START_UP_FACE_Y
    rectangle_list_dict["U"] = print_face(canvas, start_x, start_y, rubiks_cube.u)
    start_y += FACE_SIZE * 2
    rectangle_list_dict["D"] = print_face(canvas, start_x, start_y, rubiks_cube.d)
    start_x -= FACE_SIZE
    start_y -= FACE_SIZE
    rectangle_list_dict["L"] = print_face(canvas, start_x, start_y, rubiks_cube.l)
    start_x += FACE_SIZE
    rectangle_list_dict["F"] = print_face(canvas, start_x, start_y, rubiks_cube.f)
    start_x += FACE_SIZE
    rectangle_list_dict["R"] = print_face(canvas, start_x, start_y, rubiks_cube.r)
    start_x += FACE_SIZE
    rectangle_list_dict["B"] = print_face(canvas, start_x, start_y, rubiks_cube.b)
    return rectangle_list_dict


def print_cube(rubiks_cube, solution):
    window = Tk()
    window.title("Rubik's Cube")

    window.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
    #window.resizable(0,0)

    canvas = Canvas(window, width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
    canvas.pack()

    rectangle_list_dict = print_plane_cube(canvas, rubiks_cube)

    window.mainloop()

