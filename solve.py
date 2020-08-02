import cube


# STEP 1
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


# STEP 2
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
    solution = []

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

        (("r", 0, 0), ("r", 0, 1)): ["R", "U'", "R'", "U2", "F'", "U'", "F"],
        (("f", 0, 2), ("u", 2, 1)): ["F'", "U", "F", "U2", "R", "U", "R'"],
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
        (("r", 2, 0), ("r", 1, 0)): ["R", "U", "R'", "U'", "R", "U'", "R'", "U2", "F'", "U'", "F"],
        (("f", 2, 2), ("r", 1, 0)): ["R", "U'", "R'", "U", "F'", "U'", "F", "U'", "F'", "U'", "F"]
    }

    corner_border_solution = switch_corner_border.get((corner_position, border_position))
    corner_border_solution = corner_border_solution if corner_border_solution else []
    rubiks_cube.move_sequence(corner_border_solution)
    solution += corner_border_solution

    return solution


def step_2(rubiks_cube):
    solution = []
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

    corner_border_found = True
    while corner_border_found:
        corner_border_found = False
        for corner_border in corner_border_list:
            two_layers_corner_border_solution = place_two_layers_corner_border(rubiks_cube, corner_border)
            if two_layers_corner_border_solution:
                corner_border_found = True
            solution += [rubiks_cube.current_move_dict[x] for x in two_layers_corner_border_solution]
            rubiks_cube.rotate_x()
        if not corner_border_found:
            for corner_border in corner_border_list:
                if not corner_border_found:
                    two_layers_corner_border_solution = prepare_two_layers_corner_border(rubiks_cube, corner_border)
                    two_layers_corner_border_solution += place_two_layers_corner_border(rubiks_cube, corner_border)
                    if two_layers_corner_border_solution:
                        corner_border_found = True
                    solution += [rubiks_cube.current_move_dict[x] for x in two_layers_corner_border_solution]
                rubiks_cube.rotate_x()

    return solution


# STEP 3
def step_3(rubiks_cube):
    algo_dic = {
        # DOT
        """
  X O X
  - - -
O|X X X|O
O|X O X|O
O|X X X|O
  - - -
  X O X""": ["R", "U", "B'", "R", "B", "R2", "U'", "R'", "F", "R", "F'"],

        """
  X O X
  - - -
O|X X X|O
O|X O X|O
X|X X X|X
  - - -
  O O O""": ["R'", "F", "R", "F'", "U2", "R'", "F", "R", "F2", "U2", "F"],

        """
  O O X
  - - -
X|X X X|O
O|X O X|O
O|X X O|X
  - - -
  X O X""": ["F'", "B2", "L", "B'", "L", "F", "U2", "F'", "L", "B'", "F"],

        """
  X O X
  - - -
O|X X O|X
O|X O X|O
X|X X X|O
  - - -
  O O X""": ["R'", "U2", "R'", "F", "R", "F'", "U'", "F'", "U'", "F", "U'", "R"],

        """
  X O O
  - - -
X|O X X|X
O|X O X|O
O|X X O|X
  - - -
  X O X""": ["R", "U", "R'", "U", "R'", "F", "R", "F'", "U2", "R'", "F", "R", "F'"],

        """
  X O X
  - - -
X|O X O|X
O|X O X|O
X|O X O|X
  - - -
  X O X""": ["R'", "L", "F2", "R", "L'", "U2", "R'", "L", "F", "R", "L'", "U2", "R'", "L", "F2", "R", "L'"],

        """
  X O X
  - - -
X|O X O|X
O|X O X|O
O|X X X|O
  - - -
  X O X""": ["R'", "U2", "F", "R", "U", "R'", "U'", "F2", "U2", "F", "R"],

        """
  O O O
  - - -
X|X X X|X
O|X O X|O
X|O X O|X
  - - -
  X O X""": ["F", "R", "U", "R'", "U", "F'", "U2", "F'", "L", "F", "L'"],

        # LINE
        """
  O X X
  - - -
X|X O X|O
O|X O X|O
X|X O X|O
  - - -
  O X X""": ["R'", "U'", "F'", "U", "F'", "L", "F", "L'", "F", "R"],

        """
  X X X
  - - -
O|X O X|O
O|X O X|O
O|X O X|O
  - - -
  X X X""": ["R", "U'", "B2", "D", "B'", "U2", "B", "D'", "B2", "U", "R'"],

        """
  O O X
  - - -
X|X X X|O
X|O O O|X
X|X X X|O
  - - -
  O O X""": ["F", "U", "R", "U'", "R'", "U", "R", "U'", "R'", "F'"],

        """
  X O X
  - - -
O|X X X|O
X|O O O|X
O|X X X|O
  - - -
  X O X""": ["L'", "B'", "L", "U'", "R'", "U", "R", "U'", "R'", "U", "R", "L'", "B", "L"],

        # CROSS
        """
  O X X
  - - -
X|X O X|O
X|O O O|X
X|X O X|O
  - - -
  O X X""": ["L", "U'", "R'", "U", "L'", "U", "R", "U", "R'", "U", "R"],

        """
  X X X
  - - -
O|X O X|O
X|O O O|X
O|X O X|O
  - - -
  X X X""": ["R", "U", "R'", "U", "R", "U'", "R'", "U", "R", "U2", "R'"],

        """
  X X O
  - - -
O|X O X|X
X|O O O|X
X|X O O|X
  - - -
  O X X""": ["L'", "U", "R", "U'", "L", "U", "R'"],

        """
  O X X
  - - -
X|X O X|O
X|O O O|X
O|X O O|X
  - - -
  X X X""": ["R'", "U2", "R", "U", "R'", "U", "R"],

        """
  X X O
  - - -
X|O O X|X
X|O O O|X
X|O O X|X
  - - -
  X X O""": ["R'", "F'", "L", "F", "R", "F'", "L'", "F"],

        """
  X X X
  - - -
X|O O O|X
X|O O O|X
X|X O X|X
  - - -
  O X O""": ["R2", "D", "R'", "U2", "R", "D'", "R'", "U2", "R'"],

        """
  X X O
  - - -
X|O O X|X
X|O O O|X
O|X O O|X
  - - -
  X X X""": ["R'", "F'", "L'", "F", "R", "F'", "L", "F"],

        # 4 CORNERS
        """
  X O X
  - - -
X|O X O|X
X|O O X|O
X|O O O|X
  - - -
  X X X""": ["R'", "L", "F'", "R", "L'", "U2", "R'", "L", "F'", "R", "L'"],

        """
  X O X
  - - -
X|O X O|X
X|O O O|X
X|O X O|X
  - - -
  X O X""": ["L'", "R", "U", "R'", "U'", "L", "R'", "F", "R", "F'"],

        # SHAPE _|
        """
  O X X
  - - -
X|X O X|O
X|O O X|O
X|O X X|X
  - - -
  X O O""": ["L", "F", "R'", "F", "R", "F2", "L'"],

        """
  X X X
  - - -
X|O O X|O
X|O O X|O
X|X X O|X
  - - -
  O O X""": ["F", "R'", "F'", "R", "U", "R", "U'", "R'"],

        """
  X X O
  - - -
O|X O X|X
X|O O X|O
X|X X O|X
  - - -
  O O X""": ["R'", "U'", "R", "F", "R'", "F'", "U", "F", "R", "F'"],

        """
  O X O
  - - -
X|X O X|X
X|O O X|O
X|O X O|X
  - - -
  X O X""": ["U'", "R", "U2", "R'", "U'", "R", "U'", "R2", "F'", "U'", "F", "U", "R"],

        """
  X X O
  - - -
O|X O X|X
X|O O X|O
O|X X X|X
  - - -
  X O O""": ["F", "R", "U", "R'", "U'", "R", "U", "R'", "U'", "F'"],

        """
  O X O
  - - -
X|X O X|X
X|O O X|O
X|X X X|X
  - - -
  O O O""": ["L", "F'", "L'", "F", "U2", "L2", "B", "L", "B'", "L"],

        # SHAPE |_
        """
  O X O
  - - -
X|X O X|X
O|X O O|X
X|O X O|X
  - - -
  X O X""": ["U'", "R'", "U2", "R", "U", "R'", "U", "R2", "B", "U", "B'", "U'", "R'"],

        """
  X X X
  - - -
O|X O O|X
O|X O O|X
X|X X X|O
  - - -
  O O X""": ["L", "F2", "R'", "F'", "R", "F'", "L'"],

        """
  O X X
  - - -
X|X O O|X
O|X O O|X
X|O X X|O
  - - -
  X O X""": ["R'", "U2", "R2", "B'", "R'", "B", "R'", "U2", "R"],

        """
  O X X
  - - -
X|X O X|O
O|X O O|X
X|X X X|O
  - - -
  O O X""": ["F'", "L'", "U'", "L", "U", "L'", "U'", "L", "U", "F"],

        """
  X X O
  - - -
O|X O X|X
O|X O O|X
O|X X X|X
  - - -
  X O O""": ["R'", "F", "R'", "F'", "R2", "U2", "B'", "R", "B", "R'"],

        """
  O X O
  - - -
X|X O X|X
O|X O O|X
X|X X X|X
  - - -
  O O O""": ["R'", "F", "R", "F'", "U2", "R2", "B'", "R'", "B", "R'"],

        # SHAPE ¯|
        """
  O O X
  - - -
X|X X O|X
X|O O X|O
O|X O X|X
  - - -
  X X O""": ["R", "U", "R'", "B'", "R", "B", "U'", "B'", "R'", "B"],

        """
  X O O
  - - -
X|O X X|X
X|O O X|O
X|X O X|O
  - - -
  O X X""": ["L'", "B'", "L", "U'", "R'", "U", "R", "L'", "B", "L"],

        """
  X O O
  - - -
O|X X X|X
X|O O X|O
X|X O O|X
  - - -
  O X X""": ["U2", "L", "R2", "F'", "R", "F'", "R'", "F2", "R", "F'", "R", "L'"],

        """
  X O X
  - - -
X|O X O|X
X|O O X|O
O|X O X|O
  - - -
  X X X""": ["B'", "R", "B'", "R2", "U", "R", "U", "R'", "U'", "R", "B2"],

        # SHAPE |¯
        """
  X O O
  - - -
O|X X X|X
O|X O O|X
O|X O X|X
  - - -
  X X O""": ["L", "U'", "F'", "U2", "F'", "U", "F", "U'", "F", "U2", "F", "U'", "L'"],

        """
  O O X
  - - -
X|X X X|O
O|X O O|X
X|O O X|X
  - - -
  X X O""": ["U2", "R'", "L2", "F", "L'", "F", "L", "F2", "L'", "F", "R", "L'"],

        """
  X O X
  - - -
X|O X O|X
O|X O O|X
O|X O X|O
  - - -
  X X X""": ["R2", "U", "R'", "B'", "R", "U'", "R2", "U", "R", "B", "R'"],

        """
  O O X
  - - -
X|X X X|O
O|X O O|X
O|X O O|X
  - - -
  X X X""": ["L'", "B2", "R", "B", "R'", "B", "L"],

        # C
        """
  X X X
  - - -
X|O O X|O
O|X O X|O
X|O O X|O
  - - -
  X X X""": ["R", "U", "R", "B'", "R'", "B", "U'", "R'"],

        """
  X O X
  - - -
O|X X X|O
X|O O O|X
X|O X O|X
  - - -
  X O X""": ["R", "U", "R'", "U'", "B'", "R'", "F", "R", "F'", "B"],


        # L
        """
  X O O
  - - -
O|X X X|X
X|O O O|X
X|X X O|X
  - - -
  O O X""": ["R'", "F", "R", "U", "R'", "F'", "R", "F", "U'", "F'"],

        """
  O O X
  - - -
X|X X X|O
X|O O O|X
X|O X X|X
  - - -
  X O O""": ["L", "F'", "L'", "U'", "L", "F", "L'", "F'", "U", "F"],

        """
  O O X
  - - -
X|X X X|O
X|O O O|X
O|X X O|X
  - - -
  X O X""": ["L'", "B'", "L", "R'", "U'", "R", "U", "L'", "B", "L"],

        """
  X O O
  - - -
O|X X X|X
X|O O O|X
X|O X X|O
  - - -
  X O X""": ["R", "B", "R'", "L", "U", "L'", "U'", "R", "B'", "R'"],

        # P
        """
  X X X
  - - -
X|O O X|O
X|O O X|O
X|O X X|O
  - - -
  X O X""": ["F", "U", "R", "U'", "R'", "F'"],

        """
  O X X
  - - -
X|X O O|X
O|X O O|X
X|X X O|X
  - - -
  O O X""": ["R'", "U'", "F", "U", "R", "U'", "R'", "F'", "R"],

        """
  X X O
  - - -
X|O O X|X
X|O O X|O
X|O X X|X
  - - -
  X O O""": ["L", "U", "F'", "U'", "L'", "U", "L", "F", "L'"],

        """
  X X X
  - - -
O|X O O|X
O|X O O|X
O|X X O|X
  - - -
  X O X""": ["F'", "U'", "L'", "U", "L", "F"],

        # T
        """
  X O X
  - - -
O|X X O|X
X|O O O|X
O|X X O|X
  - - -
  X O X""": ["F", "R", "U", "R'", "U'", "F'"],

        """
  O O X
  - - -
X|X X O|X
X|O O O|X
X|X X O|X
  - - -
  O O X""": ["R", "U", "R'", "U'", "R'", "F", "R", "F'"],


        # W
        """
  X O X
  - - -
O|X X O|X
O|X O O|X
X|O O X|X
  - - -
  X X O""": ["L", "U", "L'", "U", "L", "U'", "L'", "U'", "L'", "B", "L", "B'"],

        """
  X O X
  - - -
X|O X X|O
X|O O X|O
X|X O O|X
  - - -
  O X X""": ["R'", "U'", "R", "U'", "R'", "U", "R", "U", "R", "B'", "R'", "B"],

        # Z
        """
  X O O
  - - -
X|O X X|X
X|O O O|X
O|X X O|X
  - - -
  X O X""": ["R'", "F", "R", "U", "R'", "U'", "F'", "U", "R"],

        """
  O O X
  - - -
X|X X O|X
X|O O O|X
X|O X X|O
  - - -
  X O X""": ["L", "F'", "L'", "U'", "L", "U", "F", "U'", "L'"],
    }

    solution = []
    up_color = rubiks_cube.u.face[1][1].color
    for i in range(4):
        if not solution:
            cube_repr = f"\n{rubiks_cube.u}"
            for color in "ywrogb":
                if color == up_color:
                    continue
                cube_repr = cube_repr.replace(color, "X")
            cube_repr = cube_repr.replace(up_color, "O")
            algo_dic_solution = algo_dic.get(cube_repr)
            algo_dic_solution = algo_dic_solution if algo_dic_solution else []
            rubiks_cube.move_sequence(algo_dic_solution)
            solution = [rubiks_cube.current_move_dict[x] for x in algo_dic_solution]
        rubiks_cube.rotate_x()

    return solution

# STEP 4
def position_tuple_list_to_0_7_tuple(position_list):
    u_0_7_position_list = []
    for position in position_list:
        if position[0] != "u":
            raise ValueError("Position {position} not on the up face.")
        u_0_7_position = position[1] * 3 + position[2]
        if u_0_7_position > 4:
            u_0_7_position -= 1
        u_0_7_position_list.append(u_0_7_position)

    return tuple(u_0_7_position_list)


def solve_u_edge(rubiks_cube, u_0_7_position_tuple):
    switch_u_0_7_tuple = {
        # A
        (7, 1, 0,
         3,    4,
         5, 6, 2): ["R'", "F", "R'", "B2", "R", "F'", "R'", "B2", "R2"],

        (0, 1, 7,
         3,    4,
         2, 6, 5): ["R", "B'", "R", "F2", "R'", "B", "R", "F2", "R2"],

        # U
        (0, 1, 2,
         6,    3,
         5, 4, 7): ["R2", "U", "R", "U", "R'", "U'", "R'", "U'", "R'", "U", "R'"],

        (0, 1, 2,
         4,    6,
         5, 3, 7): ["R", "U'", "R", "U", "R", "U", "R", "U'", "R'", "U'", "R2"],

        # H
        (0, 6, 2,
         4,    3,
         5, 1, 7): ["R2", "L2", "D", "R2", "L2", "U2", "R2", "L2", "D", "R2", "L2"],

        # T
        (0, 1, 7,
         4,    3,
         5, 6, 2): ["R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U", "R'", "F'"],

        # J
        (2, 3, 0,
         1,    4,
         5, 6, 7): ["R'", "U", "L'", "U2", "R", "U'", "R'", "U2", "R", "L", "U'"],

        (0, 1, 7,
         3,    6,
         5, 4, 2): ["R", "U", "R'", "F'", "R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'"],

        # R
        (2, 1, 0,
         6,    4,
         5, 3, 7): ["L", "U2", "L'", "U2", "L", "F'", "L'", "U'", "L", "U", "L", "F", "L2", "U"],

        (2, 1, 0,
         3,    6,
         5, 4, 7): ["R'", "U2", "R", "U2", "R'", "F", "R", "U", "R'", "U'", "R'", "F'", "R2", "U'"],

        # V
        (7, 4, 2,
         3,    1,
         5, 6, 0): ["R'", "U", "R'", "U'", "B'", "R'", "B2", "U'", "B'", "U", "B'", "R", "B", "R"],

        # G
        (5, 4, 0,
         1,    3,
         2, 6, 7): ["R2", "D", "B'", "U", "B'", "U'", "B", "D'", "R2", "F'", "U", "F"],

        (7, 3, 2,
         6,    4,
         0, 1, 5): ["R'", "U'", "R", "B2", "D", "L'", "U", "L", "U'", "L", "D'", "B2"],

        (7, 1, 2,
         6,    3,
         0, 4, 5): ["R2", "D'", "F", "U'", "F", "U", "F'", "D", "R2", "B", "U'", "B'"],

        (5, 6, 0,
         1,    4,
         2, 3, 7): ["R", "U", "R'", "F2", "D'", "L", "U'", "L'", "U", "L'", "D", "F2"],

        # F
        (0, 1, 2,
         4,    3,
         7, 6, 5): ["R'", "U2", "R'", "U'", "B'", "R'", "B2", "U'", "B'", "U", "B'", "R", "B", "U'", "R"],

        # Z
        (0, 3, 2,
         1,    6,
         5, 4, 7): ["R2", "L2", "D", "R2", "L2", "U", "R'", "L", "F2", "R2", "L2", "B2", "R'", "L", "U2"],

        # Y
        (7, 3, 2,
         1,    4,
         5, 6, 0): ["F", "R", "U'", "R'", "U'", "R", "U", "R'", "F'", "R", "U", "R'", "U'", "R'", "F", "R", "F'"],

        # N
        (7, 6, 2,
         3,    4,
         5, 1, 0): ["L", "U'", "R" ,"U2", "L'", "U", "R'", "L", "U'", "R", "U2", "L'", "U", "R'", "U"],

        (0, 6, 5,
         3,    4,
         2, 1, 7): ["R'", "U", "L'", "U2", "R", "U'", "L", "R'", "U", "L'", "U2", "R", "U'", "L", "U'"],

        # E
        (5, 1, 7,
         3,    4,
         0, 6, 2): ["R", "B'", "R'", "F", "R", "B", "R'", "F2", "L'", "B", "L", "F", "L'", "B'", "L"]
    }
    solution = switch_u_0_7_tuple.get(u_0_7_position_tuple)
    solution = solution if solution else []
    rubiks_cube.move_sequence(solution)

    return solution


def step_4(rubiks_cube):
    solution = []
    u_corner_border_list = [
        (rubiks_cube.u.face[1][1].color, rubiks_cube.l.face[1][1].color, rubiks_cube.b.face[1][1].color),
        (rubiks_cube.u.face[1][1].color, rubiks_cube.b.face[1][1].color),
        (rubiks_cube.u.face[1][1].color, rubiks_cube.b.face[1][1].color, rubiks_cube.r.face[1][1].color),
        (rubiks_cube.u.face[1][1].color, rubiks_cube.l.face[1][1].color),
        (rubiks_cube.u.face[1][1].color, rubiks_cube.r.face[1][1].color),
        (rubiks_cube.u.face[1][1].color, rubiks_cube.f.face[1][1].color, rubiks_cube.l.face[1][1].color),
        (rubiks_cube.u.face[1][1].color, rubiks_cube.f.face[1][1].color),
        (rubiks_cube.u.face[1][1].color, rubiks_cube.r.face[1][1].color, rubiks_cube.f.face[1][1].color)
    ]

    for i in range(4):
        if not solution:
            u_corner_border_list = [
                (rubiks_cube.u.face[1][1].color, rubiks_cube.l.face[1][1].color, rubiks_cube.b.face[1][1].color),
                (rubiks_cube.u.face[1][1].color, rubiks_cube.b.face[1][1].color),
                (rubiks_cube.u.face[1][1].color, rubiks_cube.b.face[1][1].color, rubiks_cube.r.face[1][1].color),
                (rubiks_cube.u.face[1][1].color, rubiks_cube.l.face[1][1].color),
                (rubiks_cube.u.face[1][1].color, rubiks_cube.r.face[1][1].color),
                (rubiks_cube.u.face[1][1].color, rubiks_cube.f.face[1][1].color, rubiks_cube.l.face[1][1].color),
                (rubiks_cube.u.face[1][1].color, rubiks_cube.f.face[1][1].color),
                (rubiks_cube.u.face[1][1].color, rubiks_cube.r.face[1][1].color, rubiks_cube.f.face[1][1].color)
            ]

            u_position_list = []
            for corner_border in u_corner_border_list:
                u_position_list.append(rubiks_cube.where_is(*corner_border))
            # u_0_7_position_tuple is the up face positions from 0 to 7 (see cube below)
            # the index of the tuple is the position where the corresponding value is supposed to be
            # the value is the actual position from 0 to 7
            #
            #               0 1 2
            #               3 X 4
            #               5 6 7
            #
            u_0_7_position_tuple = position_tuple_list_to_0_7_tuple(u_position_list)
            u_edge_solution = solve_u_edge(rubiks_cube, u_0_7_position_tuple)
            solution += [rubiks_cube.current_move_dict[x] for x in u_edge_solution]
        rubiks_cube.rotate_x()
        i += 1

    return solution


# SOLVE ENTRY POINT
def solve(rubiks_cube):
    solution = []
    step = []
    step_func_list = [step_1, step_2, step_3, step_4]
    for step_func in step_func_list:
        solution += step_func(rubiks_cube)
        step.append(len(solution))

    return solution, step
