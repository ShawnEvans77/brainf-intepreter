# Given a string, with [ at specified index, determine its matching bracket. 
# Instrumental for the jumping and implementing nested loops properly. 

code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."

# Output:

# Bracket '[' at index 0's matching brace ']' can be found at index 40.

stack = []

for i, c in enumerate(code):
    match c:
        case '[':
            stack.append(i)
        case ']':
             print(f"Bracket '[' at index {stack.pop()}'s matching brace ']' can be found at index {i}")