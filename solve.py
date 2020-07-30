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

    corner_border_placed = 0
    while corner_border_placed < 4:
        corner_border_found = False
        for corner_border in corner_border_list:
            two_layers_corner_border_solution = place_two_layers_corner_border(rubiks_cube, corner_border)
            if two_layers_corner_border_solution:
                corner_border_placed += 1
                corner_border_found = True
            solution += [rubiks_cube.current_move_dict[x] for x in two_layers_corner_border_solution]
            rubiks_cube.rotate_x()
        if not corner_border_found:
            for corner_border in corner_border_list:
                if not corner_border_found:
                    two_layers_corner_border_solution = prepare_two_layers_corner_border(rubiks_cube, corner_border)
                    two_layers_corner_border_solution += place_two_layers_corner_border(rubiks_cube, corner_border)
                    if two_layers_corner_border_solution:
                        corner_border_placed += 1
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
  X O X""": ["R", "U", "B'", "l", "U", "l2'", "x'", "U'", "R'", "F", "R", "F'"],

        """
  X O X
  - - -
O|X X X|O
O|X O X|O
X|X X X|X
  - - -
  O O O""": ["R'", "F", "R", "F'", "U2", "R'", "F", "R", "y'", "R2", "U2", "R"],

        """
  O O X
  - - -
X|X X X|O
O|X O X|O
O|X X O|X
  - - -
  X O X""": ["y", "L'", "R2", "B", "R'", "B", "L", "U2'", "L'", "B", "M'"],

        """
  X O X
  - - -
O|X X O|X
O|X O X|O
X|X X X|O
  - - -
  O O X""": ["R'", "U2", "x", "R'", "U", "R", "U'", "y", "R'", "U'", "R'", "U", "R'", "F"],

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
  X O X""": ["M'", "U2", "M", "U2", "M'", "U", "M", "U2", "M'", "U2", "M"],

        """
  X O X
  - - -
X|O X O|X
O|X O X|O
O|X X X|O
  - - -
  X O X""": ["R'", "U2", "F", "R", "U", "R'", "U'", "y'", "R2", "U2", "x'", "R", "U"],

        """
  O O O
  - - -
X|X X X|X
O|X O X|O
X|O X O|X
  - - -
  X O X""": ["F", "R", "U", "R'", "U", "y'", "R'", "U2", "R'", "F", "R", "F'"],

        # LINE
        """
  O X X
  - - -
X|X O X|O
O|X O X|O
X|X O X|O
  - - -
  O X X""": ["R'", "U'", "y", "L'", "U", "L'", "y'", "L", "F", "L'", "F", "R"],

        """
  X X X
  - - -
O|X O X|O
O|X O X|O
O|X O X|O
  - - -
  X X X""": ["R", "U'", "y", "R2", "D", "R'", "U2", "R", "D'", "R2", "d", "R'"],

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
  X X X""": ["M'", "U'", "M", "U2'", "M'", "U'", "M"],

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
  O O X""": ["R'", "U'", "R", "y'", "x'", "R", "U'", "R'", "F", "R", "U", "R'"],

        """
  O X O
  - - -
X|X O X|X
X|O O X|O
X|O X O|X
  - - -
  X O X""": ["U'", "R", "U2'", "R'", "U'", "R", "U'", "R2", "y'", "R'", "U'", "R", "U", "B"],

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
  O O O""": ["L", "F'", "L'", "F", "U2", "L2", "y'", "L", "F", "L'", "F"],

        # SHAPE |_
        """
  O X O
  - - -
X|X O X|X
O|X O O|X
X|O X O|X
  - - -
  X O X""": ["U'", "R'", "U2", "R", "U", "R'", "U", "R2", "y", "R", "U", "R'", "U'", "F'"],

        """
  X X X
  - - -
O|X O O|X
O|X O O|X
X|X X X|O
  - - -
  O O X""": ["r", "U2", "R'", "U'", "R", "U'", "r'"],

        """
  O X X
  - - -
X|X O O|X
O|X O O|X
X|O X X|O
  - - -
  X O X""": ["R'", "U2", "l", "R", "U'", "R'", "U", "l'", "U2", "R"],

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
  X O O""": ["R'", "F", "R'", "F'", "R2", "U2", "x'", "U'", "R", "U", "R'"],

        """
  O X O
  - - -
X|X O X|X
O|X O O|X
X|X X X|X
  - - -
  O O O""": ["R'", "F", "R", "F'", "U2", "R2", "y", "R'", "F'", "R", "F'"],

        # SHAPE ¯|
        """
  O O X
  - - -
X|X X O|X
X|O O X|O
O|X O X|X
  - - -
  X X O""": ["R", "U", "R'", "y", "R'", "F", "R", "U'", "R'", "F'", "R"],

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
  O X X""": ["U2", "r", "R2'", "U'", "R", "U'", "R'", "U2", "R", "U'", "M"],

        """
  X O X
  - - -
X|O X O|X
X|O O X|O
O|X O X|O
  - - -
  X X X""": ["x'", "U'", "R", "U'", "R2'", "F", "x", "R", "U", "R'", "U'", "R", "B2"],

        # SHAPE |¯
        """
  X O O
  - - -
O|X X X|X
O|X O O|X
O|X O X|X
  - - -
  X X O""": ["L", "U'", "y'", "R'", "U2'", "R'", "U", "R", "U'", "R", "U2", "R", "d'", "L'"],

        """
  O O X
  - - -
X|X X X|O
O|X O O|X
X|O O X|X
  - - -
  X X O""": ["U2", "l'", "L2", "U", "L'", "U", "L", "U2", "L'", "U", "M"],

        """
  X O X
  - - -
X|O X O|X
O|X O O|X
O|X O X|O
  - - -
  X X X""": ["R2'", "U", "R'", "B'", "R", "U'", "R2'", "U", "l", "U", "l'"],

        """
  O O X
  - - -
X|X X X|O
O|X O O|X
O|X O O|X
  - - -
  X X X""": ["r'", "U2", "R", "U", "R'", "U", "r"],

        # C
        """
  X X X
  - - -
X|O O X|O
O|X O X|O
X|O O X|O
  - - -
  X X X""": ["R", "U", "x'", "R", "U'", "R'", "U", "x", "U'", "R'"],

        """
  X O X
  - - -
O|X X X|O
X|O O O|X
X|O X O|X
  - - -
  X O X""": ["R", "U", "R'", "U'", "x", "D'", "R'", "U", "R", "E'"],


        # L
        """
  X O O
  - - -
O|X X X|X
X|O O O|X
X|X X O|X
  - - -
  O O X""": ["R'", "F", "R", "U", "R'", "F'", "R", "y", "L", "U'", "L'"],

        """
  O O X
  - - -
X|X X X|O
X|O O O|X
X|O X X|X
  - - -
  X O O""": ["L", "F'", "L'", "U'", "L", "F", "L'", "y'", "R'", "U", "R"],

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
  O O X""": ["R'", "d'", "L", "d", "R", "U'", "R'", "F'", "R"],

        """
  X X O
  - - -
X|O O X|X
X|O O X|O
X|O X X|X
  - - -
  X O O""": ["L", "d", "R'", "d'", "L'", "U", "L", "F", "L'"],

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
  X X O""": ["L", "U", "L'", "U", "L", "U'", "L'", "U'", "y2'", "R'", "F", "R", "F'"],

        """
  X O X
  - - -
X|O X X|O
X|O O X|O
X|X O O|X
  - - -
  O X X""": ["R'", "U'", "R", "U'", "R'", "U", "R", "U", "y", "F", "R'", "F'", "R"],

        # Z
        """
  X O O
  - - -
X|O X X|X
X|O O O|X
O|X X O|X
  - - -
  X O X""": ["R'", "F", "R", "U", "R'", "U'", "y", "L'", "d", "R"],

        """
  O O X
  - - -
X|X X O|X
X|O O O|X
X|O X X|O
  - - -
  X O X""": ["L", "F'", "L'", "U'", "L", "U", "y'", "R", "d'", "L'"],
    }

    def rotate_repr(src):
        """
        Rotate 90° clockwise:
  a b c
  - - -
l|m n o|d
k|t u p|e
j|s r q|f
  - - -
  i h g
        """
        dst = list(src)
        (
            a, b, c,
            d, e, f,
            g, h, i,
            j, k, l,
            m, n, o, p,
            q, r, s, t
        ) = (
            3, 5, 7,
            25, 35, 45,
            61, 59, 57,
            37, 27, 17,
            19, 21, 23, 33,
            43, 41, 39, 29
        )

        dst[a] = src[j]
        dst[b] = src[k]
        dst[c] = src[l]

        dst[d] = src[a]
        dst[e] = src[b]
        dst[f] = src[c]

        dst[g] = src[d]
        dst[h] = src[e]
        dst[i] = src[f]

        dst[j] = src[g]
        dst[k] = src[h]
        dst[l] = src[i]

        dst[m] = src[s]
        dst[n] = src[t]
        dst[o] = src[m]
        dst[p] = src[n]

        dst[q] = src[o]
        dst[r] = src[p]
        dst[s] = src[q]
        dst[t] = src[r]

        return "".join(dst)

    back_color = rubiks_cube.b.face[1][1].color
    cube_repr = f"\n{rubiks_cube.b}"
    for color in "ywrogb":
        if color == back_color:
            continue
        cube_repr = cube_repr.replace(color, "X")
    cube_repr = cube_repr.replace(back_color, "O")

    for i in range(3):
        try:
            return algo_dic[cube_repr]
        except KeyError:
            cube_repr = rotate_repr(cube_repr)
    raise ValueError(
        "Error: step 3 can't be solved. "
        "Proceeding to smash the cube into a wall... "
        "*BOOOM* ... Recovery successful!"
    )


# STEP 4
def step_4(rubiks_cube):
    return []


# SOLVE ENTRY POINT
def solve(rubiks_cube):
    solution = []
    step = []
    step_func_list = [step_1, step_2, step_3, step_4]
    for step_func in step_func_list:
        solution += step_func(rubiks_cube)
        step.append(len(solution))

    return solution, step
