# Maksymilian Wojnar

from . import AST


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator


def print_indent(indent):
    print(''.join('| ' for _ in range(indent)), end='')


class TreePrinter:
    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Program)
    def printTree(self):
        self.instructions.printTree()

    @addToClass(AST.Instructions)
    def printTree(self, indent=0):
        for instruction in self.instructions:
            instruction.printTree(indent)

    @addToClass(AST.Block)
    def printTree(self, indent=0):
        self.instructions.printTree(indent + 1)

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        print_indent(indent)
        print(self.name)

    @addToClass(AST.Value)
    def printTree(self, indent=0):
        print_indent(indent)
        print(self.value)

    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        print_indent(indent)
        print(self.op)

        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.Range)
    def printTree(self, indent=0):
        print_indent(indent)
        print('RANGE')

        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.Expressions)
    def printTree(self, indent=0):
        for expr in self.expressions:
            expr.printTree(indent)

    @addToClass(AST.UnaryExpr)
    def printTree(self, indent=0):
        print_indent(indent)
        print(self.op)
        self.value.printTree(indent + 1)

    @addToClass(AST.Statement)
    def printTree(self, indent=0):
        print_indent(indent)
        print(self.stmt)

        if hasattr(self, 'value') and self.value is not None:
            self.value.printTree(indent + 1)

    @addToClass(AST.Function)
    def printTree(self, indent=0):
        print_indent(indent)
        print(self.func)

        for arg in self.args:
            arg.printTree(indent + 1)

    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        print_indent(indent)
        print('VECTOR')
        self.elements.printTree(indent + 1)

    @addToClass(AST.VectorField)
    def printTree(self, indent=0):
        print_indent(indent)
        print(self.id)

        self.x.printTree(indent + 1)

        if self.y is not None:
            self.y.printTree(indent + 1)

    @addToClass(AST.VectorRange)
    def printTree(self, indent=0):
        print_indent(indent)
        print(self.id)
        self.range.printTree(indent + 1)

    @addToClass(AST.IfStatement)
    def printTree(self, indent=0):
        print_indent(indent)
        print('IF')
        self.condition.printTree(indent + 1)

        print_indent(indent)
        print('THEN')
        self.if_block.printTree(indent + 1)

        if self.else_block is not None:
            print_indent(indent)
            print('ELSE')
            self.else_block.printTree(indent + 1)

    @addToClass(AST.ForStatement)
    def printTree(self, indent=0):
        print_indent(indent)
        print('FOR')

        print_indent(indent + 1)
        print(self.var)

        self.range.printTree(indent + 1)
        self.block.printTree(indent + 1)

    @addToClass(AST.WhileStatement)
    def printTree(self, indent=0):
        print_indent(indent)
        print('WHILE')
        self.condition.printTree(indent + 1)
        self.block.printTree(indent + 1)
