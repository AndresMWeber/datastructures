# FIFO
class Queue(object):
    def __init__(self):
        self.queue = []

    def push(self, stack_element):
        self.queue.append(stack_element)

    def pop(self):
        val = self.queue[0]
        self.queue = self.queue[1:]
        return val
