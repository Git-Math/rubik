import sys
import random
import cube

def usage():
    print("usage: %s <number> <length>\n\
<number>: number of scramble (must be a number between 1 and 99)\n\
<length>: length of one scramble (must be a number between 1 and 999)" % sys.argv[0])

def print_scramble(length):
    last_move = ""
    for i in range(length):
        move = random.choice([x for x in cube.move_list if len(last_move) == 0 or x[0] != last_move[0]])
        print(move, end="")
        if i < length - 1:
            print(" ", end="")
        else:
            print()
        last_move = move
        i += 1

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
        print_scramble(length)
