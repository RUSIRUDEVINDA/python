# You are given a list of integers representing a sequence of operations. 
# Positive numbers must be pushed onto a stack, while negative indicates a pop operation. 
# Maintain a queue that stores all values removed from the stack in the order they are popped. 
# At the end, return the final stack and the queue of popped elements


def push(stack, value):
    return stack.append(value)

def pop(stack):
    return stack.pop()

def Enqueue(queue,value):
    return queue.append(value)

def Dequeue(queue):
    return queue

my_list = []
my_stack = []
my_queue = []

num_eliments = int(input("Enter no of elimens you need to add: "))

for i in range(num_eliments):
    value = int(input("Enter Item: "))
    my_list.append(value)

    if value < 0 :
        Enqueue(my_queue,value)

    else:
        push(my_stack,value)

print(my_stack)
print(my_queue)








