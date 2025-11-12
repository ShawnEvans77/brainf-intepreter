import sys

def execute(program):
    mem = [0] * 30000
    p = 0
    i = 0

    stack = []
    loop_map = {}

    for i, c in enumerate(program):
        match c:
            case '[':
                stack.append(i)
            case ']':
                loop_map[stack.pop()] = i

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
                open = i

                if mem[p] == 0:
                    i = loop_map[i] + 1
            case ']':
                if mem[p] != 0:
                    i = open
            case ',':
                mem[p] = int(input())
            case '.':
                print(chr(mem[p]), end="")

        i += 1
    
# def main():
#     file_path = sys.argv[1]
        
#     with open(file_path, "r") as file:
#         program = file.read()

#     execute(program)

# if __name__ == '__main__':
#     main()

execute(">++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-]<+.")