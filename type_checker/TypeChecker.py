# Maksymilian Wojnar

from collections import defaultdict

import m_ast.AST
from m_ast import AST
from .SymbolTable import SymbolTable, VariableSymbol


ttype = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))
utype = defaultdict(lambda: defaultdict(lambda: None))

INTNUM = 'int'
FLOATNUM = 'float'
STRING = 'string'
VECTOR = 'vector'
BOOL = 'bool'
RANGE = 'range'

ttype['+'][INTNUM][INTNUM] = INTNUM
ttype['+'][INTNUM][FLOATNUM] = FLOATNUM
ttype['+'][INTNUM][VECTOR] = VECTOR
ttype['+'][FLOATNUM][INTNUM] = FLOATNUM
ttype['+'][FLOATNUM][FLOATNUM] = FLOATNUM
ttype['+'][FLOATNUM][VECTOR] = VECTOR
ttype['+'][VECTOR][INTNUM] = VECTOR
ttype['+'][VECTOR][FLOATNUM] = VECTOR
ttype['+'][VECTOR][VECTOR] = VECTOR
ttype['*'] = ttype['/'] = ttype['-'] = ttype['+']

ttype['+'][STRING][STRING] = STRING
ttype['*'][STRING][INTNUM] = STRING
ttype['*'][INTNUM][STRING] = STRING

ttype['.+'][VECTOR][VECTOR] = VECTOR
ttype['.*'] = ttype['./'] = ttype['.-'] = ttype['.+']

ttype['+='][INTNUM][INTNUM] = INTNUM
ttype['+='][INTNUM][FLOATNUM] = FLOATNUM
ttype['+='][FLOATNUM][INTNUM] = FLOATNUM
ttype['+='][FLOATNUM][FLOATNUM] = FLOATNUM
ttype['+='][VECTOR][INTNUM] = VECTOR
ttype['+='][VECTOR][FLOATNUM] = VECTOR
ttype['+='][VECTOR][VECTOR] = VECTOR
ttype['-='] = ttype['*='] = ttype['/='] = ttype['+=']

ttype['=='][INTNUM][INTNUM] = BOOL
ttype['=='][INTNUM][FLOATNUM] = BOOL
ttype['=='][FLOATNUM][INTNUM] = BOOL
ttype['=='][FLOATNUM][FLOATNUM] = BOOL
ttype['=='][VECTOR][VECTOR] = BOOL
ttype['=='][STRING][STRING] = BOOL
ttype['!='] = ttype['>='] = ttype['>'] = ttype['<='] = ttype['<'] = ttype['==']

ttype[':'][INTNUM][INTNUM] = RANGE

utype['-'][INTNUM] = INTNUM
utype['-'][FLOATNUM] = FLOATNUM
utype['-'][VECTOR] = VECTOR
utype['\''][VECTOR] = VECTOR

BLOCK = 'block'
LOOP = 'loop'
IF = 'if'


class TypeChecker:
    def __init__(self):
        self.errors = False
        self.symbol_table = SymbolTable(None, BLOCK)

    def error(self, node, message):
        print(f'Line {node.lineno}: {message}')
        self.errors = True

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, None)

        if visitor is None:
            method = 'visit_' + node.__class__.__bases__[0].__name__
            visitor = getattr(self, method, None)

        if visitor is None and hasattr(node, 'lineno'):
            self.error(node, 'Unexpected expression.')
        elif visitor is not None:
            return visitor(node)

    def visit_Program(self, node):
        self.visit(node.instructions)

    def visit_Instructions(self, node):
        for instruction in node.instructions:
            self.visit(instruction)

    def visit_Block(self, node):
        self.symbol_table = self.symbol_table.pushScope(LOOP if node.type in (IF, LOOP) else BLOCK)
        if node.var is not None: self.symbol_table.put(node.var, VariableSymbol(node.var, INTNUM))
        self.visit(node.instructions)
        self.symbol_table = self.symbol_table.popScope()

    def visit_Expressions(self, node):
        for expression in node.expressions:
            self.visit(expression)

    def visit_IntNum(self, node):
        return INTNUM

    def visit_FloatNum(self, node):
        return FLOATNUM

    def visit_String(self, node):
        return STRING

    def visit_Variable(self, node):
        var_type = self.symbol_table.get(node.name)

        if var_type is None:
            self.error(node, f'{node.name} is undefined.')
        else:
            return var_type.type

    def visit_BinExpr(self, node):
        typeL = self.visit(node.left)
        typeR = self.visit(node.right)
        op = node.op

        if ttype[op][typeL][typeR] is None:
            self.error(node, f'{typeL} {op} {typeR} is invalid operation.')
        elif typeL == typeR == VECTOR:
            left = right = None

            if isinstance(node.left, AST.Vector):
                left = node.left
            elif isinstance(node.left, AST.Variable):
                left = self.symbol_table.get(node.left.name).value

            if isinstance(node.right, AST.Vector):
                right = node.right
            elif isinstance(node.right, AST.Variable):
                right = self.symbol_table.get(node.right.name).value

            if left is None or right is None:
                return VECTOR

            if left.shape[0] is not None and right.shape[0] is not None and left.shape[0] != right.shape[0]:
                self.error(node, f'Vectors have different sizes.')
            elif left.shape[1] is not None and right.shape[1] is not None and left.shape[0] != right.shape[1]:
                self.error(node, f'Vectors have different sizes.')
            else:
                return VECTOR
        else:
            return ttype[op][typeL][typeR]

    def visit_AssignExpr(self, node):
        typeR = self.visit(node.right)

        if isinstance(node.left, AST.Variable):
            self.symbol_table.put(node.left.name, VariableSymbol(node.left.name, typeR, node.right))
            return typeR
        else:
            typeL = self.visit(node.left)

            if not isinstance(node.left, AST.VectorField) and not isinstance(node.left, AST.VectorRange):
                self.error(node, f'Cannot assign value to {typeL}.')
            elif typeL == VECTOR and typeR not in (FLOATNUM, INTNUM, VECTOR):
                self.error(node, f'Incompatible types {typeL} and {typeR}.')
            elif typeL == FLOATNUM and typeR not in (FLOATNUM, INTNUM):
                self.error(node, f'Incompatible types {typeL} and {typeR}.')
            else:
                return typeR

    def visit_Range(self, node):
        if self.visit_BinExpr(node):
            if isinstance(node.left, AST.IntNum) and isinstance(node.right, AST.IntNum):
                node.len = node.right.value - node.left.value

            return RANGE

    def visit_UnaryExpr(self, node):
        value = self.visit(node.value)
        op = node.op

        if utype[op][value] is None:
            self.error(node, f'Cannot apply {op} operator to {value}.')
        else:
            return utype[op][value]

    def visit_Transpose(self, node):
        if (result := self.visit_UnaryExpr(node)) is not None:
            if isinstance(node.value, AST.Variable):
                node.shape = self.symbol_table.get(node.value.name).value.shape
            else:
                node.shape = node.value.shape

            node.type = VECTOR
            return result

    def visit_Return(self, node):
        if node.value is not None:
            self.visit(node.value)

    def visit_Break(self, node):
        if self.symbol_table.type != LOOP:
            self.error(node, f"Cannot use 'break' outside loop.")

    def visit_Continue(self, node):
        if self.symbol_table.type != LOOP:
            self.error(node, f"Cannot use 'continue' outside loop.")

    def visit_Function(self, node):
        for arg in node.args:
            self.visit(arg)

    def visit_matrix_function(self, node):
        if len(node.args) > 1 or self.visit(node.args[0]) != INTNUM:
            self.error(node, f'{node.func} takes only one positive {INTNUM} argument.')
        else:
            node.shape = [node.args[0].value, node.args[0].value]
            node.type = VECTOR
            return VECTOR

    def visit_Zeros(self, node):
        return self.visit_matrix_function(node)

    def visit_Ones(self, node):
        return self.visit_matrix_function(node)

    def visit_Eye(self, node):
        return self.visit_matrix_function(node)

    def visit_Vector(self, node):
        els = node.elements

        if isinstance(els, AST.Expressions):
            types = [self.visit(expr) for expr in els.expressions]

            if not types:
                self.error(node, f'Empty {VECTOR} initialization.')
            elif all([t in (INTNUM, FLOATNUM) for t in types]):
                node.type = FLOATNUM
                node.shape = [len(types), 0]
                return VECTOR
            elif all([t == VECTOR for t in types]):
                shape = els.expressions[0].shape

                for expr in els.expressions:
                    if expr.type != FLOATNUM:
                        self.error(node, f'Cannot initialize more than two dimensional {VECTOR}.')
                        break
                    if expr.shape != shape:
                        self.error(node, f'Different lengths of {VECTOR} elements.')
                        break
                else:
                    node.type = VECTOR
                    node.shape = shape
                    return VECTOR
            else:
                self.error(node, f'Incorrect {VECTOR} initialization.')
        elif isinstance(els, AST.Range):
            if self.visit(els) == RANGE:
                node.shape = [els.len, 0]
                node.type = FLOATNUM
                return VECTOR
            else:
                self.error(node, f'Incorrect {VECTOR} initialization.')

    def visit_VectorField(self, node):
        var = self.symbol_table.get(node.id)

        if not isinstance(var, AST.Vector):
            return

        if var.type != VECTOR:
            self.error(node, f'{node.id} is not a vector.')
        elif self.visit(node.x) != INTNUM or (node.y is not None and self.visit(node.y) != INTNUM):
            self.error(node, f'Incorrect type for vector element selection.')

        if node.y is not None and var.value.shape[1] == 0:
            self.error(node, f'{node.id} is one dimensional.')
        elif isinstance(node.x, AST.IntNum) and var.value.shape[0] is not None and node.x.value >= var.value.shape[0]:
            self.error(node, f'Index out of range.')
        elif isinstance(node.y, AST.IntNum) and var.value.shape[1] is not None and node.y.value >= var.value.shape[1]:
            self.error(node, f'Index out of range.')
        elif node.y is not None:
            return FLOATNUM
        else:
            return var.value.type

    def visit_VectorRange(self, node):
        if self.symbol_table.get(node.id).type != VECTOR:
            self.error(node, f'{node.id} is not a vector.')
        elif self.visit(node.range) != RANGE:
            self.error(node, f'Incorrect {RANGE} for {VECTOR}.')
        else:
            return VECTOR

    def visit_IfStatement(self, node):
        if self.visit(node.condition) != BOOL:
            self.error(node, f'IF condition must have a {BOOL} type.')

        if isinstance(node.if_block, AST.Block):
            node.if_block.type = IF

        self.visit(node.if_block)

        if node.else_block is not None:
            if isinstance(node.else_block, AST.Block):
                node.else_block.type = IF

            self.visit(node.else_block)

    def visit_ForStatement(self, node):
        self.visit(node.range)
        
        if not isinstance(node.block, AST.Block):
            self.symbol_table.pushScope(LOOP)
            self.symbol_table.put(node.var, VariableSymbol(node.var, INTNUM))
            self.visit(node.block)
            self.symbol_table.popScope()
        else:
            node.block.type = LOOP
            node.block.var = node.var
            self.visit(node.block)

    def visit_WhileStatement(self, node):
        if self.visit(node.condition) != BOOL:
            self.error(node, f'WHILE condition must have a {BOOL} type.')

        if not isinstance(node.block, AST.Block):
            self.symbol_table.pushScope(LOOP)
            self.visit(node.block)
            self.symbol_table.popScope()
        else:
            node.block.type = LOOP
            self.visit(node.block)
