import cube

def place_cross_border_u(rubiks_cube, border_position, solution):
    switch_border_position = {
        ("u", 0, 1): ["U2", "F2"],
        ("u", 1, 2): ["U", "F2"],
        ("u", 2, 1): ["F2"],
        ("u", 1, 0): ["U'", "F2"]
    }
    border_solution = switch_border_position.get(border_position)
    rubiks_cube.move_sequence(border_solution)
    solution += border_solution

def place_cross_border_d(rubiks_cube, border_position, is_first, solution):
    switch_border_position = {
        ("d", 0, 1): [],
        ("d", 1, 2): ["D'"] if is_first else ["R2"],
        ("d", 2, 1): ["D2"] if is_first else ["B2"],
        ("d", 1, 0): ["D"] if is_first else ["L2"]
    }
    border_solution = switch_border_position.get(border_position)
    rubiks_cube.move_sequence(border_solution)
    solution += border_solution
    if not is_first and len(border_solution) > 0:
        place_cross_border_u(rubiks_cube, ("u", 0, 1) if border_solution[0] == "B2" else ("u", border_position[1], border_position[2]), solution)

def place_cross_border_xu(rubiks_cube, border_position, is_first, is_last, solution):
    switch_border_position = {
        ("f", 0, 1): ["U'", "R'", "F"] + (["R"] if is_last else []),
        ("r", 0, 1): ["R'", "F"] + (["R"] if is_last else []),
        ("b", 0, 1): ["U", "R'", "F"] + (["R"] if is_last else []),
        ("l", 0, 1): ["L", "F'"] + (["L'"] if not is_first else [])
    }
    border_solution = switch_border_position.get(border_position)
    rubiks_cube.move_sequence(border_solution)
    solution += border_solution

def place_cross_border_xm(rubiks_cube, border_position, is_first, solution):
    return

def place_cross_border_xd(rubiks_cube, border_position, is_first, solution):
    return

def place_cross_border(rubiks_cube, border_position, is_first, is_last):
    solution = []

    if border_position[0] == "u":
        place_cross_border_u(rubiks_cube, border_position, solution)
    elif border_position[0] == "d":
        place_cross_border_d(rubiks_cube, border_position, is_first, solution)
    elif border_position[1] == 0:
        place_cross_border_xu(rubiks_cube, border_position, is_first, is_last, solution)
    elif border_position[1] == 1:
        place_cross_border_xm(rubiks_cube, border_position, is_first, solution)
    elif border_position[1] == 2:
        place_cross_border_xd(rubiks_cube, border_position, is_first, solution)

    return solution

def step_1(rubiks_cube):
    solution = []
    border_list = [
        [rubiks_cube.d.face[1][1].color, rubiks_cube.f.face[1][1].color],
        [rubiks_cube.d.face[1][1].color, rubiks_cube.r.face[1][1].color],
        [rubiks_cube.d.face[1][1].color, rubiks_cube.b.face[1][1].color],
        [rubiks_cube.d.face[1][1].color, rubiks_cube.l.face[1][1].color]
    ]

    for i, border in enumerate(border_list):
        border_position = rubiks_cube.where_is(border[0], border[1])
        border_solution = place_cross_border(rubiks_cube, border_position, i == 0, i == 3)
        if i == 0:
            solution += border_solution
        elif i == 1:
            solution += [cube.x_move_dict[x] for x in border_solution]
        elif i == 2:
            solution += [cube.x2_move_dict[x] for x in border_solution]
        elif i == 3:
            solution += [cube.x_prime_move_dict[x] for x in border_solution]
        rubiks_cube.rotate_x()

    return solution

def step_2(rubiks_cube):
    return []

def step_3(rubiks_cube):
    return []

def step_4(rubiks_cube):
    return []

def solve(rubiks_cube):
    solution = []
    step = []
    step_func_list = [step_1, step_2, step_3, step_4]
    for step_func in step_func_list:
        solution += step_func(rubiks_cube)
        step.append(len(solution))

    return solution, step
