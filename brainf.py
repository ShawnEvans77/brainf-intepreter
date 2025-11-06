file_path = "program.txt"
array = [0] * 30000
pointer = 0

def execute(code):
        for character in code:

            match character:
                case '>':
                    pointer += 1
                case '<':
                    pointer -= 1
                case '+':
                    array[pointer] += 1
                case '-':
                    array[pointer] -= 1
                case '.':
                    print(chr(array[pointer]))
                case ',':
                    array[pointer] = int(input("enter integer: "))
                case '[':
                    ending_brace = program.index(']')

                    while array[pointer] > 0:
                        execute(program[ending_brace+1:])

with open(file_path, "r") as file:
    program = file.read()
    execute(program)