from tkinter import *
from rubik3000 import cube

WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 1000
SQUARE_SIZE = 70
FACE_SIZE = 3 * SQUARE_SIZE
START_UP_FACE_X = WINDOW_WIDTH / 2 - FACE_SIZE
START_UP_FACE_Y = WINDOW_HEIGHT / 10
FACE_BORDER_WIDTH = 3
START_SOLUTION_TEXT_X = WINDOW_WIDTH / 2
START_SOLUTION_TEXT_Y = WINDOW_HEIGHT - WINDOW_HEIGHT / 12
TEXT_FONT = "Helvetica"
TEXT_SIZE = 16
TEXT_WEIGHT = "bold"
TEXT_WIDTH = WINDOW_WIDTH - WINDOW_WIDTH / 10
START_STEP_TEXT_X = WINDOW_WIDTH / 2
START_STEP_TEXT_Y = WINDOW_HEIGHT - WINDOW_HEIGHT / 6
START_LEFT_ARROW_X = WINDOW_WIDTH / 2 - 2 * FACE_SIZE - 100
START_LEFT_ARROW_Y = START_UP_FACE_Y + FACE_SIZE * 1.5
START_RIGHT_ARROW_X = WINDOW_WIDTH / 2 + 2 * FACE_SIZE + 100
START_RIGHT_ARROW_Y = START_LEFT_ARROW_Y

color_dict = {
    "y": "yellow",
    "w": "white",
    "g": "green",
    "b": "blue",
    "r": "red",
    "o": "orange"
}

canvas = None
rubiks_cube = None
step = None
solution = None
solution_i = None
rectangle_list_dict = None
step_text = None
solution_text = None

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

def update_face(canvas, face, rectangle_list):
    for y, line in enumerate(face.face):
        for x, square in enumerate(line):
            canvas.itemconfig(rectangle_list[y][x], fill=color_dict[square.color])

def update_plane_cube(canvas, cube, rectangle_list_dict):
    update_face(canvas, cube.u, rectangle_list_dict["U"])
    update_face(canvas, cube.d, rectangle_list_dict["D"])
    update_face(canvas, cube.r, rectangle_list_dict["R"])
    update_face(canvas, cube.l, rectangle_list_dict["L"])
    update_face(canvas, cube.f, rectangle_list_dict["F"])
    update_face(canvas, cube.b, rectangle_list_dict["B"])

def solution_to_string(solution, solution_i):
    solution_string = ""
    if solution_i == 0:
        solution_string += "[start]"
    else:
        solution_string += "start"
    for i, move in enumerate(solution):
        if i + 1 == solution_i:
            solution_string += " [" + move + "]"
        else:
            solution_string += " " + move
    return solution_string

def print_step(canvas, step, solution_i, old_step_text):
    if old_step_text:
        canvas.delete(old_step_text)

    step_string = ""
    if not step:
        step_string = "Short solution"
    elif solution_i < step[0]:
        step_string = "Step 1:"
    elif solution_i < step[1]:
        step_string = "Step 2:"
    elif solution_i < step[2]:
        step_string = "Step 3:"
    else:
        step_string = "Step 4:"

    return canvas.create_text(START_STEP_TEXT_X, START_STEP_TEXT_Y, anchor=CENTER, font=(TEXT_FONT, TEXT_SIZE, TEXT_WEIGHT), width=TEXT_WIDTH, text=step_string)

def print_solution(canvas, solution, solution_i, old_solution_text):
    if old_solution_text:
        canvas.delete(old_solution_text)

    return canvas.create_text(START_SOLUTION_TEXT_X, START_SOLUTION_TEXT_Y, anchor=CENTER, font=(TEXT_FONT, TEXT_SIZE, TEXT_WEIGHT), width=TEXT_WIDTH, text=solution_to_string(solution, solution_i))

def left_click(event):
    global canvas, rubiks_cube, step, solution, solution_i, rectangle_list_dict, step_text, solution_text

    current = canvas.gettags(event.widget.find_withtag("current"))

    if current == ():
        return
    elif current[0] == "left_arrow":
        if solution_i == 0:
            return
        solution_i -= 1
        rubiks_cube.move(cube.reverse_move_dict[solution[solution_i]])
        update_plane_cube(canvas, rubiks_cube, rectangle_list_dict)
        step_text = print_step(canvas, step, solution_i, step_text)
        solution_text = print_solution(canvas, solution, solution_i, solution_text)
    elif current[0] == "right_arrow":
        if solution_i >= len(solution):
            return
        rubiks_cube.move(solution[solution_i])
        update_plane_cube(canvas, rubiks_cube, rectangle_list_dict)
        solution_i += 1
        step_text = print_step(canvas, step, solution_i, step_text)
        solution_text = print_solution(canvas, solution, solution_i, solution_text)

def print_arrow(canvas):
    canvas.create_text(START_LEFT_ARROW_X, START_LEFT_ARROW_Y, anchor=CENTER, font=(TEXT_FONT, TEXT_SIZE * 5, TEXT_WEIGHT), width=TEXT_WIDTH, text="<", tags="left_arrow")
    canvas.create_text(START_RIGHT_ARROW_X, START_RIGHT_ARROW_Y, anchor=CENTER, font=(TEXT_FONT, TEXT_SIZE * 5, TEXT_WEIGHT), width=TEXT_WIDTH, text=">", tags="right_arrow")

    canvas.bind("<Button-1>", left_click)

def print_cube(rc, sol, st):
    global canvas, rubiks_cube, step, solution, solution_i, rectangle_list_dict, step_text, solution_text

    rubiks_cube = rc
    solution = sol
    step = st

    window = Tk()
    window.title("Rubik's Cube")

    window.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
    #window.resizable(0,0)

    canvas = Canvas(window, width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
    canvas.pack()

    rectangle_list_dict = print_plane_cube(canvas, rubiks_cube)

    solution_i = 0
    step_text = print_step(canvas, step, solution_i, None)

    solution_text = print_solution(canvas, solution, solution_i, None)

    print_arrow(canvas)

    window.mainloop()
