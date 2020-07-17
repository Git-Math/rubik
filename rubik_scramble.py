import sys
import random

def usage():
    print("usage: %s <number> <length>\n\
<number>: number of scramble (must be a number between 1 and 99)\n\
<length>: length of one scramble (must be a number between 1 and 999)" % sys.argv[0])

move_list = ["U", "U'", "U2", "D", "D'", "D2", "R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "B", "B'", "B2"]

reverse_move_dict = {
    "": "",
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

def print_scramble(length, last_move):
    move = random.choice([x for x in move_list if x != reverse_move_dict[last_move]])
    print(move, end='')
    if length <= 1:
        print()
    else:
        print(" ", end='')
        print_scramble(length - 1, move)
    

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Invalid argument number", file=sys.stderr)
        usage()
        sys.exit(1)
    try:
        number = int(sys.argv[1])
        if number < 1 or number > 99:
            raise
    except:
        print("<number> must be a number between 1 and 99", file=sys.stderr)
        usage()
        sys.exit(1)
    try:
        length = int(sys.argv[2])
        if length < 1 or length > 999:
            raise
    except:
        print("<length> must be a number between 1 and 999", file=sys.stderr)
        usage()
        sys.exit(1)

    for i in range(number):
        print_scramble(length, "")
