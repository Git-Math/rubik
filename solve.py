import cube

def place_cross_border(rubiks_cube, border_position, is_first, is_last):
    switch_border_position = {
        ("u", 0, 1): ["U2", "F2"],
        ("u", 1, 2): ["U", "F2"],
        ("u", 2, 1): ["F2"],
        ("u", 1, 0): ["U'", "F2"],

        ("d", 0, 1): [],
        ("d", 1, 2): ["D'"] if is_first else ["R2", "U", "F2"],
        ("d", 2, 1): ["D2"] if is_first else ["B2", "U2", "F2"],
        ("d", 1, 0): ["D"] if is_first else ["L2", "U'", "F2"],

        ("f", 0, 1): ["U'", "R'", "F"] + (["R"] if is_last else []),
        ("r", 0, 1): ["R'", "F"] + (["R"] if is_last else []),
        ("b", 0, 1): ["U", "R'", "F"] + (["R"] if is_last else []),
        ("l", 0, 1): ["L", "F'"] + (["L'"] if not is_first else []),

        ("f", 2, 1): ["F"] + ([] if is_first else ["D'"]) + ["L", "D"],
        ("r", 2, 1): ["R", "F"],
        ("b", 2, 1): ["B"] + ([] if is_first else ["D"]) + ["R", "D'"],
        ("l", 2, 1): ["L'", "F'"],

        ("f", 1, 2): ([] if is_first else ["D"]) + ["R'", "D'"],
        ("r", 1, 2): ([] if is_first else ["D2"]) + ["B'", "D2"],
        ("b", 1, 2): ([] if is_first else ["D'"]) + ["L'", "D"],
        ("l", 1, 2): ["F'"],

        ("f", 1, 0): ([] if is_first else ["D'"]) + ["L", "D"],
        ("r", 1, 0): ["F"],
        ("b", 1, 0): ([] if is_first else ["D"]) + ["R", "D'"],
        ("l", 1, 0): ([] if is_first else ["D2"]) + ["B", "D2"]
    }
    solution = switch_border_position.get(border_position)
    rubiks_cube.move_sequence(solution)

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
        solution += [rubiks_cube.current_move_dict[x] for x in border_solution]
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
