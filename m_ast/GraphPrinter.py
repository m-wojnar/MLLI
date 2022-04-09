# Maksymilian Wojnar

import networkx as nx
import random
import pydot

from . import AST


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator


class GraphPrinter:
    @addToClass(AST.Node)
    def printGraph(self, graph, parent, label_dict):
        raise Exception("printGraph not defined in class " + self.__class__.__name__)

    @addToClass(AST.Program)
    def printGraph(self):
        graph = nx.DiGraph()
        label_dict = {id(self): 'PROGRAM'}

        self.instructions.printGraph(graph, id(self), label_dict)

        for node in graph.nodes:
            graph.nodes[node]['label'] = label_dict[node]

        nx.drawing.nx_pydot.write_dot(graph, 'm_ast/ast.dot')
        dot = pydot.graph_from_dot_file('m_ast/ast.dot')[0]

        if '"\\n"' in dot.obj_dict['nodes']:
            del dot.obj_dict['nodes']['"\\n"']

        dot.write('m_ast/ast.png', format='png')

    @addToClass(AST.Instructions)
    def printGraph(self, graph, parent, label_dict):
        for instruction in self.instructions:
            instruction.printGraph(graph, parent, label_dict)
            
    @addToClass(AST.Block)
    def printGraph(self, graph, parent, label_dict, ):
        graph.add_edge(parent, id(self))
        label_dict[id(self)] = 'BLOCK'
        self.instructions.printGraph(graph, id(self), label_dict)

    @addToClass(AST.Variable)
    def printGraph(self, graph, parent, label_dict):
        graph.add_edge(parent, id(self))
        label_dict[id(self)] = self.name

    @addToClass(AST.Value)
    def printGraph(self, graph, parent, label_dict):
        graph.add_edge(parent, id(self))
        label_dict[id(self)] = self.value

    @addToClass(AST.BinExpr)
    def printGraph(self, graph, parent, label_dict):
        graph.add_edge(parent, id(self))
        label_dict[id(self)] = self.op

        self.left.printGraph(graph, id(self), label_dict)
        self.right.printGraph(graph, id(self), label_dict)

    @addToClass(AST.Range)
    def printGraph(self, graph, parent, label_dict):
        graph.add_edge(parent, id(self))
        label_dict[id(self)] = 'RANGE'

        self.left.printGraph(graph, id(self), label_dict)
        self.right.printGraph(graph, id(self), label_dict)

    @addToClass(AST.Expressions)
    def printGraph(self, graph, parent, label_dict):
        for expr in self.expressions:
            expr.printGraph(graph, parent, label_dict)

    @addToClass(AST.UnaryExpr)
    def printGraph(self, graph, parent, label_dict):
        graph.add_edge(parent, id(self))
        label_dict[id(self)] = self.op
        self.value.printGraph(graph, id(self), label_dict)

    @addToClass(AST.Statement)
    def printGraph(self, graph, parent, label_dict):
        graph.add_edge(parent, id(self))
        label_dict[id(self)] = self.stmt

        if hasattr(self, 'value') and self.value is not None:
            self.value.printGraph(graph, id(self), label_dict)

    @addToClass(AST.Function)
    def printGraph(self, graph, parent, label_dict):
        graph.add_edge(parent, id(self))
        label_dict[id(self)] = self.func

        for arg in self.args:
            arg.printGraph(graph, id(self), label_dict)

    @addToClass(AST.Vector)
    def printGraph(self, graph, parent, label_dict):
        graph.add_edge(parent, id(self))
        label_dict[id(self)] = 'VECTOR'
        self.elements.printGraph(graph, id(self), label_dict)

    @addToClass(AST.VectorField)
    def printGraph(self, graph, parent, label_dict):
        graph.add_edge(parent, id(self))
        label_dict[id(self)] = self.id

        self.x.printGraph(graph, id(self), label_dict)

        if self.y is not None:
            self.y.printGraph(graph, id(self), label_dict)

    @addToClass(AST.VectorRange)
    def printGraph(self, graph, parent, label_dict):
        graph.add_edge(parent, id(self))
        label_dict[id(self)] = self.id
        self.range.printGraph(graph, id(self), label_dict)

    @addToClass(AST.IfStatement)
    def printGraph(self, graph, parent, label_dict):
        graph.add_edge(parent, id(self))
        label_dict[id(self)] = 'IF'
        self.condition.printGraph(graph, id(self), label_dict)
        self.if_block.printGraph(graph, id(self), label_dict)

        if self.else_block is not None:
            self.else_block.printGraph(graph, id(self), label_dict)

    @addToClass(AST.ForStatement)
    def printGraph(self, graph, parent, label_dict):
        graph.add_edge(parent, id(self))
        label_dict[id(self)] = 'FOR'

        rnd = random.random()
        graph.add_edge(id(self), rnd)
        label_dict[rnd] = self.var

        self.range.printGraph(graph, id(self), label_dict)
        self.block.printGraph(graph, id(self), label_dict)

    @addToClass(AST.WhileStatement)
    def printGraph(self, graph, parent, label_dict):
        graph.add_edge(parent, id(self))
        label_dict[id(self)] = 'WHILE'
        self.condition.printGraph(graph, id(self), label_dict)
        self.block.printGraph(graph, id(self), label_dict)
