# Stack using a list

# Creating a stack
def create_stack():
    stack = []
    return stack

# Checking if the stack is empty
def check_empty(stack):
    return len(stack) == 0

# Adding data to the stack
def push(stack, data):
    stack.append(data)
    # print("pushed data: " + data)

# Removing data from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop()

stack = create_stack()
push(stack, 1)
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
# print("popped data: " + pop(stack))
# print("stack after popping a data: " + str(stack))
print(stack)
