# Maksymilian Wojnar

from abc import ABC


class Node:
    def accept(self, visitor):
        return visitor.visit(self)


class Program(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class Instructions(Node):
    def __init__(self, instruction):
        self.instructions = [instruction]


class Block(Node):
    def __init__(self, instructions):
        self.instructions = instructions
        self.type = None
        self.var = None
        self.push = True


class Expressions(Node):
    def __init__(self, expr):
        self.expressions = [expr]


class Value(Node, ABC):
    def __init__(self, value):
        self.value = value


class IntNum(Value):
    def __init__(self, value):
        super().__init__(value)


class FloatNum(Value):
    def __init__(self, value):
        super().__init__(value)


class String(Value):
    def __init__(self, value):
        super().__init__(value)


class Variable(Node):
    def __init__(self, name):
        self.name = name


class VectorField(Node):
    def __init__(self, id_name, x, y=None):
        self.id = id_name
        self.x = x
        self.y = y


class VectorRange(Node):
    def __init__(self, id_name, vec_range):
        self.id = id_name
        self.range = vec_range


class BinExpr(Node, ABC):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class AddExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '+', right)


class SubExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '-', right)


class MulExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '*', right)


class DivExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '/', right)


class DotAddExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '.+', right)


class DotSubExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '.-', right)


class DotMulExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '.*', right)


class DotDivExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, './', right)


class AssignExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '=', right)


class AddAssignExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '+=', right)


class SubAssignExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '-=', right)


class MulAssignExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '*=', right)


class DivAssignExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '/=', right)


class LEExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '<=', right)


class LowerExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '<', right)


class GEExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '>=', right)


class GreaterExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '>', right)


class EQExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '==', right)


class NEExpr(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, '!=', right)


class Range(BinExpr):
    def __init__(self, left, right):
        super().__init__(left, ':', right)
        self.len = None


class UnaryExpr(Node, ABC):
    def __init__(self, op, value):
        self.op = op
        self.value = value


class UnaryMinus(UnaryExpr):
    def __init__(self, value):
        super().__init__('-', value)


class Transpose(UnaryExpr):
    def __init__(self, value):
        super().__init__('\'', value)


class Statement(Node, ABC):
    def __init__(self, stmt):
        self.stmt = stmt


class Return(Statement):
    def __init__(self, value=None):
        super().__init__('RETURN')
        self.value = value


class Break(Statement):
    def __init__(self):
        super().__init__('BREAK')


class Continue(Statement):
    def __init__(self):
        super().__init__('CONTINUE')


class Function(Node, ABC):
    def __init__(self, func, args):
        self.func = func

        if isinstance(args, list):
            self.args = args
        else:
            self.args = [args]


class Print(Function):
    def __init__(self, args):
        super().__init__('PRINT', args)


class Zeros(Function):
    def __init__(self, args):
        super().__init__('ZEROS', args)


class Ones(Function):
    def __init__(self, args):
        super().__init__('ONES', args)


class Eye(Function):
    def __init__(self, args):
        super().__init__('EYE', args)


class Vector(Node):
    def __init__(self, elements):
        self.elements = elements
        self.shape = [None, None]
        self.type = None


class IfStatement(Node):
    def __init__(self, condition, if_block, else_block=None):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block


class ForStatement(Node):
    def __init__(self, var, var_range, block):
        self.var = var
        self.range = var_range
        self.block = block


class WhileStatement(Node):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block
