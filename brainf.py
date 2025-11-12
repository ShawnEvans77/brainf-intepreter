def execute(program):
    mem = [0] * 30000
    p = 0
    i = 0

    stack = []
    dict = create_map(program)
    reverse_dict = {close : opening for opening, close in dict.items()}

    print(dict)

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
                stack.append(i)

                if mem[p] == 0:
                    i = dict[i]
                    stack.pop()
        
            case ']':

                # print(f"the matching brace for closing bracket at index {i} is {stack[-1]}")
                
                if mem[p] != 0:  
                    i = reverse_dict[i] - 1
            case ',':
                mem[p] = int(input())
            case '.':
                print(chr(mem[p]), end="")

        i += 1


def create_map(program): 
    stack = []
    dict = {}
    
    for i, c in enumerate(program):
        match c:
            case '[':
                stack.append(i)
            case ']':
                dict[stack.pop()] = i

    return dict

# def main():
#     file_path = sys.argv[1]
        
#     with open(file_path, "r") as file:
#         program = file.read()

#     execute(program)

# if __name__ == '__main__':
#     main()


# execute("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")

# execute(">++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-]<+.")

execute("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")

