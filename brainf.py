file_path = "program.txt"
array = [0] * 30000
pointer = 0

# > = increases memory pointer, or moves the pointer to the right 1 block.
# < = decreases memory pointer, or moves the pointer to the left 1 block.
# + = increases value stored at the block pointed to by the memory pointer
# - = decreases value stored at the block pointed to by the memory pointer
# [ = like c while(cur_block_value != 0) loop.
# ] = if block currently pointed to's value is not zero, jump back to [
# , = like c getchar(). input 1 character.
# . = like c putchar(). print 1 character to the console

def main():
    with open(file_path, "r") as file:
        program = file.read()

        for character in program:

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

if __name__ == 'main':
    main()