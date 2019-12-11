# LIFO
class Stack(object):
    def __init__(self):
        self.queue = []

    def push(self, stack_element):
        self.queue.append(stack_element)

    def pop(self):
        return self.queue.pop()
