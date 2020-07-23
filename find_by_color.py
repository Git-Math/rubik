
def _find_border(self, color_a, color_b):
    for face_name in 'udrlfb':
        face = self.__dict__[face_name]
        if (
                face.face[0][1].color == color_a
                and face.u_edge[1].color == color_b
        ):
            return face_name, 1, 0  # up
        if (
                face.face[1][2].color == color_a
                and face.r_edge[1].color == color_b
        ):
            return face_name, 2, 1  # right
        if (
                face.face[2][1].color == color_a
                and face.d_edge[1].color == color_b
        ):
            return face_name, 1, 2  # down
        if (
                face.face[1][0].color == color_a
                and face.l_edge[1].color == color_b
        ):
            return face_name, 0, 1  # left
    raise ValueError(f"Border ({color_a}, {color_b}) not found.")


def _find_corner(self, color_a, color_b, color_c):
    for face_name in 'udrlfb':
        face = self.__dict__[face_name]
        if (
                face.face[0][0].color == color_a
                and face.l_edge[2].color == color_b
                and face.u_edge[0].color == color_c
        ):
            return face_name, 0, 0  # top-left
        if (
                face.face[0][2].color == color_a
                and face.u_edge[2].color == color_b
                and face.r_edge[0].color == color_c
        ):
            return face_name, 2, 0  # top-right
        if (
                face.face[2][2].color == color_a
                and face.r_edge[2].color == color_b
                and face.d_edge[0].color == color_c
        ):
            return face_name, 2, 2  # bottom-right
        if (
                face.face[2][0].color == color_a
                and face.d_edge[2].color == color_b
                and face.l_edge[0].color == color_c
        ):
            return face_name, 0, 2  # bottom-left
    raise ValueError(f"Corner ({color_a}, {color_b}, {color_c}) not found.")


def where_is(self, color_a, color_b, color_c=None):
    """
    Find a border coresponding to the given color.
    The color format is assumed to be the same as ´Square.color´.
    Fill only the ´color_a´ and ´color_b´ if you want to find a border,
    otherwise if you want to find a corner also fill ´color_c´.

    Returns a tuple:
    - face_name (str) where ´color_a´ was found: one of u d r l f b
    - x (int): -
    - y (int): the coordinates of ´color_a´ on ´face_name´
    Raises ValueError if nothing was found.

    Ex:
    cube = Cube()
    face_name, x, y = cube.where_is('g', 'y', 'r')
    print(cube.__dict__[face_name].face[y][x])
    >>>> 'g'
    """
    if color_c is None:
        return _find_border(self, color_a, color_b)
    try:
        return _find_corner(self, color_a, color_b, color_c)
    except ValueError:
        # in case the corner's colors are in an impossible order
        return _find_corner(self, color_a, color_c, color_b)


# TEST AREA
if __name__ == '__main__':
    import random
    import cube

    def inspect(c):
        for border in [
                "gy", "go", "gw", "gr",
                "by", "bo", "bw", "br",
                "yr", "yo", "wr", "wo",
        ]:
            print("border", border, "at", where_is(c, border[0], border[1]))
            print("border", border, "at", where_is(c, border[1], border[0]))

        for corner in [
                "bry", "byo", "bow", "bwr",
                "goy", "gyr", "grw", "gwo",
        ]:
            print("corner", corner, "at", where_is(c, corner[0], corner[1], corner[2]))
            print("corner", corner, "at", where_is(c, corner[1], corner[2], corner[0]))
            print("corner", corner, "at", where_is(c, corner[2], corner[0], corner[1]))

    c = cube.Cube(real_cube=True)
    print(c)
    inspect(c)

    moves = cube.move_list * 10
    random.shuffle(moves)
    moves = moves[:5]
    print("Moves:", moves)
    c.scramble(moves)
    print(c)

    inspect(c)
