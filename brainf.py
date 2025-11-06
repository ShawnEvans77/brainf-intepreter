import sys

def execute(program):
    mem = [0] * 30000
    p = 0
    i = 0

    while i < len(program):
        match program[i]:
            case '>': 
                p += 1
            case '<':
                p -= 1
            case '+':
                mem[p] += 1 if mem[p] <= 255 else 255
            case '-':
                mem[p] -= 1 if mem[p] > 0 else 0
            case '[':
                closed = program.index(']')
                open = i 

                if mem[p] == 0:
                    i = closed 
            case ']':
                if mem[p] != 0:
                    i = open 
            case ',':
                mem[p] = int(input())
            case '.':
                print(chr(mem[p]), end="")

        i += 1

def main():
    file_path = sys.argv[1]
        
    with open(file_path, "r") as file:
        program = file.read()

    execute(program)

if __name__ == '__main__':
    main()