import sys

move_list = ["U", "U'", "U2", "D", "D'", "D2", "R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "B", "B'", "B2"]

move_list_no_dict = {
    "U": [x for x in move_list if x[0] != "U"],
    "D": [x for x in move_list if x[0] != "D"],
    "R": [x for x in move_list if x[0] != "R"],
    "L": [x for x in move_list if x[0] != "L"],
    "F": [x for x in move_list if x[0] != "F"],
    "B": [x for x in move_list if x[0] != "B"]
}

reverse_move_dict = {
    "U": "U'",
    "U'": "U",
    "U2": "U2",
    "D": "D'",
    "D'": "D",
    "D2": "D2",
    "R": "R'",
    "R'": "R",
    "R2": "R2",
    "L": "L'",
    "L'": "L",
    "L2": "L2",
    "F": "F'",
    "F'": "F",
    "F2": "F2",
    "B": "B'",
    "B'": "B",
    "B2": "B2"
}

class Square:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.color
class Face:
    def __init__(self, color):
        self.face = [
            [Square(color), Square(color), Square(color)],
            [Square(color), Square(color), Square(color)],
            [Square(color), Square(color), Square(color)]
        ]
        self.u_edge = None
        self.d_edge = None
        self.r_edge = None
        self.l_edge = None

    # getters
    def get_u(self):
        return [self.face[0][0], self.face[0][1], self.face[0][2]]

    def get_d(self):
        return [self.face[2][2], self.face[2][1], self.face[2][0]]

    def get_r(self):
        return [self.face[0][2], self.face[1][2], self.face[2][2]]

    def get_l(self):
        return [self.face[2][0], self.face[1][0], self.face[0][0]]

    # setters
    def set_edge(self, u, d, r, l):
        self.u_edge = u
        self.d_edge = d
        self.r_edge = r
        self.l_edge = l

    # rotaters (yes, that's a word)
    def rotate_face(self):
        swap = self.face[0][0].color
        self.face[0][0].color = self.face[2][0].color
        self.face[2][0].color = self.face[2][2].color
        self.face[2][2].color = self.face[0][2].color
        self.face[0][2].color = swap
        swap = self.face[0][1].color
        self.face[0][1].color = self.face[1][0].color
        self.face[1][0].color = self.face[2][1].color
        self.face[2][1].color = self.face[1][2].color
        self.face[1][2].color = swap

    def rotate_prime_face(self):
        swap = self.face[0][0].color
        self.face[0][0].color = self.face[0][2].color
        self.face[0][2].color = self.face[2][2].color
        self.face[2][2].color = self.face[2][0].color
        self.face[2][0].color = swap
        swap = self.face[0][1].color
        self.face[0][1].color = self.face[1][2].color
        self.face[1][2].color = self.face[2][1].color
        self.face[2][1].color = self.face[1][0].color
        self.face[1][0].color = swap

    def rotate2_face(self):
        swap = self.face[0][0].color
        self.face[0][0].color = self.face[2][2].color
        self.face[2][2].color = swap
        swap = self.face[0][2].color
        self.face[0][2].color = self.face[2][0].color
        self.face[2][0].color = swap
        swap = self.face[0][1].color
        self.face[0][1].color = self.face[2][1].color
        self.face[2][1].color = swap
        swap = self.face[1][2].color
        self.face[1][2].color = self.face[1][0].color
        self.face[1][0].color = swap

    def rotate_edge(self):
        swap = [self.u_edge[0].color, self.u_edge[1].color, self.u_edge[2].color]
        self.u_edge[0].color = self.l_edge[0].color
        self.u_edge[1].color = self.l_edge[1].color
        self.u_edge[2].color = self.l_edge[2].color
        self.l_edge[0].color = self.d_edge[0].color
        self.l_edge[1].color = self.d_edge[1].color
        self.l_edge[2].color = self.d_edge[2].color
        self.d_edge[0].color = self.r_edge[0].color
        self.d_edge[1].color = self.r_edge[1].color
        self.d_edge[2].color = self.r_edge[2].color
        self.r_edge[0].color = swap[0]
        self.r_edge[1].color = swap[1]
        self.r_edge[2].color = swap[2]

    def rotate_prime_edge(self):
        swap = [self.u_edge[0].color, self.u_edge[1].color, self.u_edge[2].color]
        self.u_edge[0].color = self.r_edge[0].color
        self.u_edge[1].color = self.r_edge[1].color
        self.u_edge[2].color = self.r_edge[2].color
        self.r_edge[0].color = self.d_edge[0].color
        self.r_edge[1].color = self.d_edge[1].color
        self.r_edge[2].color = self.d_edge[2].color
        self.d_edge[0].color = self.l_edge[0].color
        self.d_edge[1].color = self.l_edge[1].color
        self.d_edge[2].color = self.l_edge[2].color
        self.l_edge[0].color = swap[0]
        self.l_edge[1].color = swap[1]
        self.l_edge[2].color = swap[2]

    def rotate2_edge(self):
        swap = [self.u_edge[0].color, self.u_edge[1].color, self.u_edge[2].color]
        self.u_edge[0].color = self.d_edge[0].color
        self.u_edge[1].color = self.d_edge[1].color
        self.u_edge[2].color = self.d_edge[2].color
        self.d_edge[0].color = swap[0]
        self.d_edge[1].color = swap[1]
        self.d_edge[2].color = swap[2]
        swap = [self.r_edge[0].color, self.r_edge[1].color, self.r_edge[2].color]
        self.r_edge[0].color = self.l_edge[0].color
        self.r_edge[1].color = self.l_edge[1].color
        self.r_edge[2].color = self.l_edge[2].color
        self.l_edge[0].color = swap[0]
        self.l_edge[1].color = swap[1]
        self.l_edge[2].color = swap[2]

    def rotate(self):
        self.rotate_face()
        self.rotate_edge()

    def rotate_prime(self):
        self.rotate_prime_face()
        self.rotate_prime_edge()

    def rotate2(self):
        self.rotate2_face()
        self.rotate2_edge()

    # misc
    def is_solved(self):
        color = self.face[1][1].color
        for line in self.face:
            for square in line:
                if square.color != color:
                    return False
        return True

    def print(self):
        for line in self.face:
            for square in line:
                print(square.color, end=" ")
            print()
        print()

    def __repr__(self):
        return "\n".join([
            " ".join([square.color for square in line])
            for line in self.face
        ])
class Cube:
    def __init__(self, real_cube=False):
        self.u = Face("y")
        self.d = Face("w")
        self.r = Face("g")
        self.l = Face("b")
        if real_cube:
            self.f = Face("o")
            self.b = Face("r")
        else:
            self.f = Face("r")
            self.b = Face("o")

        self.u.set_edge(self.b.get_u(), self.f.get_u(), self.r.get_u(), self.l.get_u())
        self.d.set_edge(self.f.get_d(), self.b.get_d(), self.l.get_d(), self.r.get_d())
        self.r.set_edge(self.u.get_r(), self.d.get_r(), self.b.get_l(), self.f.get_r())
        self.l.set_edge(self.u.get_l(), self.d.get_l(), self.f.get_l(), self.b.get_r())
        self.f.set_edge(self.u.get_d(), self.d.get_u(), self.r.get_l(), self.l.get_r())
        self.b.set_edge(self.u.get_u(), self.d.get_d(), self.l.get_l(), self.r.get_r())

        self.switch_move = {
            "U": self.u.rotate,
            "U'": self.u.rotate_prime,
            "U2": self.u.rotate2,
            "D": self.d.rotate,
            "D'": self.d.rotate_prime,
            "D2": self.d.rotate2,
            "R": self.r.rotate,
            "R'": self.r.rotate_prime,
            "R2": self.r.rotate2,
            "L": self.l.rotate,
            "L'": self.l.rotate_prime,
            "L2": self.l.rotate2,
            "F": self.f.rotate,
            "F'": self.f.rotate_prime,
            "F2": self.f.rotate2,
            "B": self.b.rotate,
            "B'": self.b.rotate_prime,
            "B2": self.b.rotate2
        }

    def move(self, m):
        self.switch_move.get(m)()

    def scramble(self, scramble_move_list):
        for scramble_move in scramble_move_list:
            if scramble_move in move_list:
                self.move(scramble_move)
            else:
                print("Invalid scramble move:", scramble_move, "\n\
Valid moves:", *move_list, file=sys.stderr)
                sys.exit(1)

    def reverse_solution(self, solution):
        for move in solution[::-1]:
            if move in move_list:
                self.move(reverse_move_dict[move])
            else:
                print("Invalid solution move:", move, "\n\
Valid moves:", *move_list, file=sys.stderr)
                sys.exit(1)

    def is_solved(self):
        if self.u.is_solved() and self.d.is_solved() and self.r.is_solved() and self.l.is_solved() and self.f.is_solved() and self.b.is_solved():
            return True
        return False

    def search_short_solution(self, current_move_list, solution, i):
        for move in current_move_list:
            solution.append(move)
            self.move(move)
            if self.is_solved():
                return True, solution
            if i > 1:
                ret = self.search_short_solution(move_list_no_dict[move[0]], solution, i - 1)
                if ret[0]:
                    return ret
            solution.pop()
            self.move(reverse_move_dict[move])
        return False, []

    def print(self):
        print("U:")
        self.u.print()
        print("D:")
        self.d.print()
        print("R:")
        self.r.print()
        print("L:")
        self.l.print()
        print("F:")
        self.f.print()
        print("B:")
        self.b.print()
        print("################################")

    def __repr__(self):
        return f"""U:
{self.u}
D:
{self.d}
R:
{self.r}
L:
{self.l}
F:
{self.f}
B:
{self.b}
################################"""
