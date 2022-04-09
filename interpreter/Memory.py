# Maksymilian Wojnar

class Memory:
    def __init__(self):
        self.symbols = {}

    def has_key(self, name):
        return name in self.symbols

    def get(self, name):
        return self.symbols.get(name, None)

    def put(self, name, value):
        self.symbols[name] = value


class MemoryStack:
    def __init__(self, memory=None):
        self.stack = [memory if memory is not None else Memory()]

    def get(self, name):
        for memory in self.stack[::-1]:
            if (var := memory.get(name)) is not None:
                return var

        return None

    def insert(self, name, value):
        self.stack[-1].put(name, value)

    def set(self, name, value):
        for memory in self.stack[::-1]:
            if memory.has_key(name):
                memory.put(name, value)
                return

        self.stack[-1].put(name, value)

    def push(self, memory):
        self.stack.append(memory)

    def pop(self):
        self.stack.pop()
