class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0


# Input list
my_list = ['A', 'B', 'A', 'D', 'E']

my_stack = Stack()
my_stack_A = Stack()
my_queue = Queue()

for i in my_list:
    if i == 'A':
        my_stack_A.push(i)
    else:
        my_stack.push(i)

print("Stack:", my_stack.stack)
print("Queue:", my_stack_A.stack)

pop1 = my_stack.pop()
pop2 = my_stack.pop()
pop3 = my_stack.pop()

my_queue.enqueue(pop1)
my_queue.enqueue(pop2)
my_queue.enqueue(pop3)

print("Output: ", my_queue.queue)




