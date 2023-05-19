def create_stack():
    stack = []
    return stack 

def check_empty(stack):
    return len(stack)==0

def push(stack , item):
    stack.append(item)
    print("Pushed Item {}".format(item))
    
def pop(stack):
    if check_empty(stack):
        print("Stack is empty")
    else:
        return stack.pop()
    
def display(stack):
    for i in stack:
        print(i)
    
s = create_stack()

ck = check_empty(s)
print(ck)

push(s,10)
push(s,20)
push(s,2390)
push(s,2340)
push(s,230)

display(s)

pop(s)
pop(s)