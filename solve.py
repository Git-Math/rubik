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

def is_border_fu(border_position):
    if (
        border_position == ("f", 0, 1)
        or border_position == ("u", 2, 1)
    ):
        return True
    return False

def is_border_ru(border_position):
    if (
        border_position == ("r", 0, 1)
        or border_position == ("u", 1, 2)
    ):
        return True
    return False

def is_border_bu(border_position):
    if (
        border_position == ("b", 0, 1)
        or border_position == ("u", 0, 1)
    ):
        return True
    return False

def is_border_lu(border_position):
    if (
        border_position == ("l", 0, 1)
        or border_position == ("u", 1, 0)
    ):
        return True
    return False

def is_corner_fur(corner_position):
    if (
        corner_position == ("f", 0, 2)
        or corner_position == ("u", 2, 2)
        or corner_position == ("r", 0, 0)
        ):
        return True
    return False

def is_corner_rur(corner_position):
    if (
        corner_position == ("r", 0, 2)
        or corner_position == ("u", 0, 2)
        or corner_position == ("b", 0, 0)
    ):
        return True
    return False

def is_corner_bur(corner_position):
    if (
        corner_position == ("b", 0, 2)
        or corner_position == ("u", 0, 0)
        or corner_position == ("l", 0, 0)
    ):
        return True
    return False

def is_corner_lur(corner_position):
    if (
        corner_position == ("l", 0, 2)
        or corner_position == ("u", 2, 0)
        or corner_position == ("f", 0, 0)
    ):
        return True
    return False

def is_corner_fdr(corner_position):
    if (
        corner_position == ("f", 2, 2)
        or corner_position == ("d", 0, 2)
        or corner_position == ("r", 2, 0)
    ):
        return True
    return False

def prepare_two_layers_corner_border(rubiks_cube, corner_border):
    solution = []

    corner_position = rubiks_cube.where_is(corner_border[0][0], corner_border[0][1], corner_border[0][2])
    border_position = rubiks_cube.where_is(corner_border[1][0], corner_border[1][1])

    switch_border = {
        ("r", 1, 2): ["B", "U", "B'"] if not is_corner_rur(corner_position) else ["B", "U2", "B'"],
        ("b", 1, 0): ["B", "U2", "B'"] if not is_corner_bur(corner_position) else ["B", "U'", "B'"],

        ("b", 1, 2): ["B'", "U2", "B"] if not is_corner_fur(corner_position) else ["U", "B'", "U'", "B"],
        ("l", 1, 0): ["B'", "U", "B"] if not is_corner_lur(corner_position) else ["B'", "U'", "B"],

        ("l", 1, 2): ["L'", "U'", "L"] if not is_corner_lur(corner_position) else ["L'", "U2", "L"],
        ("f", 1, 0): ["L'", "U2", "L"] if not is_corner_rur(corner_position) else ["L'", "U", "L"],

        ("u", 2, 1): ["U'"] if is_corner_fdr(corner_position) else [],
        ("u", 0, 1): ["U"] if is_corner_fdr(corner_position) else [],
        ("u", 1, 0): ["U2"] if is_corner_fdr(corner_position) else [],

        ("r", 0, 1): ["U"] if is_corner_fdr(corner_position) else [],
        ("b", 0, 1): ["U2"] if is_corner_fdr(corner_position) else [],
        ("l", 0, 1): ["U'"] if is_corner_fdr(corner_position) else []
    }

    border_solution = switch_border.get(border_position)
    border_solution = border_solution if border_solution else []
    rubiks_cube.move_sequence(border_solution)
    solution += border_solution

    corner_position = rubiks_cube.where_is(corner_border[0][0], corner_border[0][1], corner_border[0][2])
    border_position = rubiks_cube.where_is(corner_border[1][0], corner_border[1][1])

    switch_corner = {
        ("d", 2, 2): (["U"] if is_border_lu(border_position) else []) + ["B", "U", "B'"],
        ("r", 2, 2): (["U"] if is_border_lu(border_position) else []) + ["B", "U", "B'"],
        ("b", 2, 0): (["U"] if is_border_lu(border_position) else []) + ["B", "U", "B'"],

        ("d", 2, 0): (["U"] if is_border_fu(border_position) else []) + ["B'", "U2", "B"],
        ("b", 2, 2): (["U"] if is_border_fu(border_position) else []) + ["B'", "U2", "B"],
        ("l", 2, 0): (["U"] if is_border_fu(border_position) else []) + ["B'", "U2", "B"],

        ("d", 0, 0): (["U"] if is_border_bu(border_position) else []) + ["L'", "U'", "L"],
        ("l", 2, 2): (["U"] if is_border_bu(border_position) else []) + ["L'", "U'", "L"],
        ("f", 2, 0): (["U"] if is_border_bu(border_position) else []) + ["L'", "U'", "L"],

        ("u", 0, 2): ["U"],
        ("r", 0, 2): ["U"],
        ("b", 0, 0): ["U"],

        ("u", 0, 0): ["U2"],
        ("b", 0, 2): ["U2"],
        ("l", 0, 0): ["U2"],

        ("u", 2, 0): ["U'"],
        ("l", 0, 2): ["U'"],
        ("f", 0, 0): ["U'"]
    }

    corner_solution = switch_corner.get(corner_position)
    corner_solution = corner_solution if corner_solution else []
    rubiks_cube.move_sequence(corner_solution)
    solution += corner_solution

    return solution

def place_two_layers_corner_border(rubiks_cube, corner_border):
    solution = prepare_two_layers_corner_border(rubiks_cube, corner_border)

    corner_position = rubiks_cube.where_is(corner_border[0][0], corner_border[0][1], corner_border[0][2])
    border_position = rubiks_cube.where_is(corner_border[1][0], corner_border[1][1])

    switch_corner_border = {
        (("r", 0, 0), ("u", 0, 1)): ["R", "U", "R'"],
        (("f", 0, 2), ("l", 0, 1)): ["F'", "U'", "F"],
        (("r", 0, 0), ("f", 0, 1)): ["U'", "F'", "U", "F"],
        (("f", 0, 2), ("u", 1, 2)): ["U", "R", "U'", "R'"],

        (("d", 0, 2), ("f", 0, 1)): ["U", "R", "U'", "R'", "U'", "F'", "U", "F"],
        (("d", 0, 2), ("u", 1, 2)): ["U'", "F'", "U", "F", "U", "R", "U'", "R'"],
        (("r", 2, 0), ("f", 0, 1)): ["F'", "U", "F", "U'", "F'", "U", "F"],
        (("r", 2, 0), ("u", 1, 2)): ["R", "U", "R'", "U'", "R", "U", "R'"],
        (("f", 2, 2), ("u", 1, 2)): ["R", "U'", "R'", "U", "R", "U'", "R'"],
        (("f", 2, 2), ("f", 0, 1)): ["F'", "U'", "F", "U", "F'", "U'", "F"],

        (("u", 2, 2), ("f", 1, 2)): ["R", "U", "R'", "U'", "R", "U", "R'", "U'", "R", "U", "R'"],
        (("u", 2, 2), ("r", 1, 0)): ["R", "U'", "R'", "U", "F'", "U", "F"],
        (("r", 0, 0), ("f", 1, 2)): ["U", "F'", "U", "F", "U", "F'", "U2", "F"],
        (("r", 0, 0), ("r", 1, 0)): ["U", "F'", "U'", "F", "U'", "R", "U", "R'"],
        (("f", 0, 2), ("f", 1, 2)): ["U'", "R", "U'", "R'", "U'", "R", "U2", "R'"],
        (("f", 0, 2), ("r", 1, 0)): ["U'", "R", "U", "R'", "U", "F'", "U'", "F"],

        (("r", 0, 0), ("r", 0, 1)): ["R", "U'", "R'", "U", "U", "F'", "U'", "F"],
        (("f", 0, 2), ("u", 2, 1)): ["F'", "U", "F", "U'", "U'", "R", "U", "R'"],
        (("r", 0, 0), ("b", 0, 1)): ["U", "F'", "U2", "F", "U", "F'", "U2", "F"],
        (("f", 0, 2), ("u", 1, 0)): ["U'", "R", "U2", "R'", "U'", "R", "U2", "R'"],
        (("r", 0, 0), ("l", 0, 1)): ["U", "F'", "U'", "F", "U", "F'", "U2", "F"],
        (("f", 0, 2), ("u", 0, 1)): ["U'", "R", "U", "R'", "U'", "R", "U2", "R'"],
        (("r", 0, 0), ("u", 1, 2)): ["U'", "R", "U'", "R'", "U", "R", "U", "R'"],
        (("f", 0, 2), ("f", 0, 1)): ["U", "F'", "U", "F", "U'", "F'", "U'", "F"],
        (("r", 0, 0), ("u", 1, 0)): ["U'", "R", "U", "R'", "U", "R", "U", "R'"],
        (("f", 0, 2), ("b", 0, 1)): ["U", "F'", "U'", "F", "U'", "F'", "U'", "F"],
        (("r", 0, 0), ("u", 2, 1)): ["U", "F'", "U2", "F", "U'", "R", "U", "R'"],
        (("f", 0, 2), ("r", 0, 1)): ["U'", "R", "U2", "R'", "U", "F'", "U'", "F"],

        (("u", 2, 2), ("u", 2, 1)): ["R", "U", "R'", "U2", "R", "U", "R'", "U'", "R", "U", "R'"],
        (("u", 2, 2), ("r", 0, 1)): ["F'", "U'", "F", "U2", "F'", "U'", "F", "U", "F'", "U'", "F"],
        (("u", 2, 2), ("u", 1, 0)): ["U2", "R", "U", "R'", "U", "R", "U'", "R'"],
        (("u", 2, 2), ("b", 0, 1)): ["U2", "F'", "U'", "F", "U'", "F'", "U", "F"],
        (("u", 2, 2), ("u", 0, 1)): ["U", "R", "U2", "R'", "U", "R", "U'", "R'"],
        (("u", 2, 2), ("l", 0, 1)): ["U'", "F'", "U2", "F", "U'", "F'", "U", "F"],
        (("u", 2, 2), ("u", 1, 2)): ["R", "U2", "R'", "U'", "R", "U", "R'"],
        (("u", 2, 2), ("f", 0, 1)): ["F'", "U2", "F", "U", "F'", "U'", "F"],

        (("d", 0, 2), ("r", 1, 0)): ["R", "U'", "R'", "U", "F'", "U2", "F", "U", "F'", "U2", "F"],
        (("r", 2, 0), ("f", 1, 2)): ["R", "U'", "R'", "U", "R", "U2", "R'", "U", "R", "U'", "R'"],
        (("f", 2, 2), ("f", 1, 2)): ["R", "U'", "R'", "U'", "R", "U", "R'", "U'", "R", "U2", "R'"],
        (("r", 2, 0), ("r", 1, 0)): ["R", "U", "R'", "U'", "R", "U'", "R'", "U", "U", "F'", "U'", "F"],
        (("f", 2, 2), ("r", 1, 0)): ["R", "U'", "R'", "U", "F'", "U'", "F", "U'", "F'", "U'", "F"]
    }

    corner_border_solution = switch_corner_border.get((corner_position, border_position))
    corner_border_solution = corner_border_solution if corner_border_solution else []
    rubiks_cube.move_sequence(corner_border_solution)
    solution += corner_border_solution

    return solution

def step_1(rubiks_cube):
    solution = []
    border_list = [
        (rubiks_cube.d.face[1][1].color, rubiks_cube.f.face[1][1].color),
        (rubiks_cube.d.face[1][1].color, rubiks_cube.r.face[1][1].color),
        (rubiks_cube.d.face[1][1].color, rubiks_cube.b.face[1][1].color),
        (rubiks_cube.d.face[1][1].color, rubiks_cube.l.face[1][1].color)
    ]

    for i, border in enumerate(border_list):
        border_position = rubiks_cube.where_is(border[0], border[1])
        cross_solution = place_cross_border(rubiks_cube, border_position, i == 0, i == 3)
        solution += [rubiks_cube.current_move_dict[x] for x in cross_solution]
        rubiks_cube.rotate_x()

    return solution

def step_2(rubiks_cube):
    solution =[]
    corner_border_list = [
        [
            (rubiks_cube.d.face[1][1].color, rubiks_cube.f.face[1][1].color, rubiks_cube.r.face[1][1].color),
            (rubiks_cube.f.face[1][1].color, rubiks_cube.r.face[1][1].color)
        ],
        [
            (rubiks_cube.d.face[1][1].color, rubiks_cube.r.face[1][1].color, rubiks_cube.b.face[1][1].color),
            (rubiks_cube.r.face[1][1].color, rubiks_cube.b.face[1][1].color)
        ],
        [
            (rubiks_cube.d.face[1][1].color, rubiks_cube.b.face[1][1].color, rubiks_cube.l.face[1][1].color),
            (rubiks_cube.b.face[1][1].color, rubiks_cube.l.face[1][1].color)
        ],
        [
            (rubiks_cube.d.face[1][1].color, rubiks_cube.l.face[1][1].color, rubiks_cube.f.face[1][1].color),
            (rubiks_cube.l.face[1][1].color, rubiks_cube.f.face[1][1].color)
        ]
    ]

    for corner_border in corner_border_list:
        two_layers_corner_border_solution = place_two_layers_corner_border(rubiks_cube, corner_border)
        solution += [rubiks_cube.current_move_dict[x] for x in two_layers_corner_border_solution]
        rubiks_cube.rotate_x()

    return solution

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
