def push(stack, value):
    return stack.append(value)
    
def pop(stack):
    return stack.pop()
    

my_stack = []

push(my_stack, 10)
push(my_stack, 12)
push(my_stack, 16)
push(my_stack, 18)
push(my_stack, 20)

print(my_stack)

pop(my_stack)
pop(my_stack)
pop(my_stack)

print(my_stack)
