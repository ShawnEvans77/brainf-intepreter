def execute(code):
        p = 0
        i = 0

        while i < len(code):

            match code[i]:
                case '>':
                    p += 1
                case '<':
                    p -= 1
                case '+':
                    array[p] += 1 if array[p] <= 255 else 255
                case '-':
                    array[p] -= 1 if array[p] > 0 else 0
                case '.':
                    print(chr(array[p]), end="")
                case ',':
                    array[p] = int(input())
                case '[':
                    ending_brace = code.index(']')
                    starting_brace = i
            
                    if array[p] == 0:
                        i = ending_brace 
                case ']':
                    if array[p] != 0:
                        i = starting_brace 

            i = i + 1

file_path = "program.txt"
array = [0] * 30000

with open(file_path, "r") as file:
    program = file.read()
    execute(program)

# print(array[:10])