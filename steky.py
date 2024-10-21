class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
          return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):

        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):

        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())
print(stack.pop())
print(stack.size())
print(stack.is_empty())