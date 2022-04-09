# Maksymilian Wojnar

class VariableSymbol:
    def __init__(self, name, ttype, value=None):
        self.name = name
        self.type = ttype
        self.value = value


class SymbolTable(object):
    def __init__(self, parent, scope_type):
        self.parent = parent
        self.type = scope_type
        self.symbols = {}

    def put(self, name, symbol):
        self.symbols[name] = symbol

    def pop(self, name):
        del self.symbols[name]

    def get(self, name):
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent is not None:
            return self.parent.get(name)
        else:
            return None

    def pushScope(self, name):
        return SymbolTable(self, name)

    def popScope(self):
        return self.parent
