from collections import deque

def reverse_string(string):
    stack = deque()
    for char in string:
        stack.append(char)
    
    reversed_string = ""
    while len(stack) > 0:
        reversed_string += stack.pop()
    
    return reversed_string

input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(reversed_string)
