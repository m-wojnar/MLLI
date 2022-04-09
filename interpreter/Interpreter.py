# Maksymilian Wojnar

from m_ast import AST
from .Memory import *
from .Exceptions import *
from .Visit import *

import numpy as np
import sys

sys.setrecursionlimit(10000)


class Interpreter:
    def __init__(self):
        self.memory = MemoryStack()

    def run(self, node):
        try:
            node.accept(self)
        except ReturnValueException as e:
            if e.value is not None:
                print(f'Returned value: {e.value}')

            sys.exit(0)

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Program)
    def visit(self, node):
        node.instructions.accept(self)

    @when(AST.Instructions)
    def visit(self, node):
        for instruction in node.instructions:
            instruction.accept(self)

    @when(AST.Block)
    def visit(self, node):
        if node.push:
            self.memory.push(Memory())
            node.instructions.accept(self)
            self.memory.pop()
        else:
            node.instructions.accept(self)

    @when(AST.Expressions)
    def visit(self, node):
        for expression in node.expressions:
            expression.accept(self)

    @when(AST.IntNum)
    def visit(self, node):
        return node.value

    @when(AST.FloatNum)
    def visit(self, node):
        return node.value

    @when(AST.String)
    def visit(self, node):
        return node.value[1:-1]

    @when(AST.Variable)
    def visit(self, node):
        return self.memory.get(node.name)

    @when(AST.VectorField)
    def visit(self, node):
        if node.y is not None:
            return self.memory.get(node.id)[node.x.accept(self), node.y.accept(self)]
        else:
            return self.memory.get(node.id)[node.x.accept(self)]

    @when(AST.VectorRange)
    def visit(self, node):
        return self.memory.get(node.id)[node.range]

    @when(AST.AddExpr)
    def visit(self, node):
        return node.left.accept(self) + node.right.accept(self)

    @when(AST.DotAddExpr)
    def visit(self, node):
        return node.left.accept(self) + node.right.accept(self)

    @when(AST.SubExpr)
    def visit(self, node):
        return node.left.accept(self) - node.right.accept(self)

    @when(AST.DotSubExpr)
    def visit(self, node):
        return node.left.accept(self) - node.right.accept(self)

    @when(AST.MulExpr)
    def visit(self, node):
        left = node.left.accept(self)
        right = node.right.accept(self)

        if isinstance(left, np.ndarray) and isinstance(right, np.ndarray):
            return left @ right
        else:
            return left * right

    @when(AST.DotMulExpr)
    def visit(self, node):
        return node.left.accept(self) * node.right.accept(self)

    @when(AST.DivExpr)
    def visit(self, node):
        return node.left.accept(self) / node.right.accept(self)

    @when(AST.DotDivExpr)
    def visit(self, node):
        return node.left.accept(self) / node.right.accept(self)

    def assign(self, left, right):
        if isinstance(left, AST.Variable):
            self.memory.set(left.name, right)
        elif isinstance(left, AST.VectorField):
            vector = self.memory.get(left.id)

            if left.y is not None:
                vector[left.x.accept(self), left.y.accept(self)] = right
            else:
                vector[left.x.accept(self)] = right
        elif isinstance(left, AST.VectorRange):
            vector = self.memory.get(left.id)
            vec_range = left.range.accept(self)

            vector[list(vec_range)] = right

    @when(AST.AssignExpr)
    def visit(self, node):
        self.assign(node.left, node.right.accept(self))

    @when(AST.AddAssignExpr)
    def visit(self, node):
        self.assign(node.left, node.left.accept(self) + node.right.accept(self))

    @when(AST.SubAssignExpr)
    def visit(self, node):
        self.assign(node.left, node.left.accept(self) - node.right.accept(self))

    @when(AST.MulAssignExpr)
    def visit(self, node):
        self.assign(node.left, node.left.accept(self) * node.right.accept(self))

    @when(AST.DivAssignExpr)
    def visit(self, node):
        self.assign(node.left, node.left.accept(self) / node.right.accept(self))

    @when(AST.LEExpr)
    def visit(self, node):
        return node.left.accept(self) <= node.right.accept(self)

    @when(AST.LowerExpr)
    def visit(self, node):
        return node.left.accept(self) < node.right.accept(self)

    @when(AST.GEExpr)
    def visit(self, node):
        return node.left.accept(self) >= node.right.accept(self)

    @when(AST.GreaterExpr)
    def visit(self, node):
        return node.left.accept(self) > node.right.accept(self)

    @when(AST.EQExpr)
    def visit(self, node):
        return node.left.accept(self) == node.right.accept(self)

    @when(AST.NEExpr)
    def visit(self, node):
        return node.left.accept(self) != node.right.accept(self)

    @when(AST.Range)
    def visit(self, node):
        return range(node.left.accept(self), node.right.accept(self))

    @when(AST.UnaryMinus)
    def visit(self, node):
        return -node.value.accept(self)

    @when(AST.Transpose)
    def visit(self, node):
        return np.transpose(node.value.accept(self))

    @when(AST.Return)
    def visit(self, node):
        if node.value is not None:
            raise ReturnValueException(node.value.accept(self))
        else:
            raise ReturnValueException()

    @when(AST.Break)
    def visit(self, node):
        raise BreakException()

    @when(AST.Print)
    def visit(self, node):
        print(*(arg.accept(self) for arg in node.args[0].expressions))

    @when(AST.Zeros)
    def visit(self, node):
        size = node.args[0].accept(self)
        return np.zeros((size, size))

    @when(AST.Ones)
    def visit(self, node):
        size = node.args[0].accept(self)
        return np.ones((size, size))

    @when(AST.Eye)
    def visit(self, node):
        size = node.args[0].accept(self)
        return np.eye(size)

    @when(AST.Vector)
    def visit(self, node):
        els = node.elements

        if isinstance(els, AST.Range):
            return np.array(els.accept(self), dtype=np.float64)
        elif isinstance(els, AST.Expressions):
            vector = np.array([els.expressions[0].accept(self)], dtype=np.float64)

            for el in els.expressions[1:]:
                vector = np.append(vector, [el.accept(self)], axis=0)

            return vector

    @when(AST.IfStatement)
    def visit(self, node):
        if node.condition.accept(self):
            node.if_block.accept(self)
        elif node.else_block is not None:
            node.else_block.accept(self)

    @when(AST.ForStatement)
    def visit(self, node):
        if isinstance(node.block, AST.Block):
            node.block.push = False

        self.memory.push(Memory())

        for i in node.range.accept(self):
            try:
                self.memory.insert(node.var, i)
                node.block.accept(self)
            except BreakException:
                break
            except ContinueException:
                continue

        self.memory.pop()

    @when(AST.WhileStatement)
    def visit(self, node):
        if isinstance(node.block, AST.Block):
            node.block.push = False

        self.memory.push(Memory())

        while node.condition.accept(self):
            try:
                node.block.accept(self)
            except BreakException:
                break
            except ContinueException:
                continue

        self.memory.pop()
