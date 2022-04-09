# Maksymilian Wojnar

import sys

from m_parser import Parser
from scanner import Scanner

from type_checker.TypeChecker import TypeChecker
from interpreter.Interpreter import Interpreter
from m_ast import TreePrinter
from m_ast import GraphPrinter


if __name__ == '__main__':
    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "examples/example.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()
    ast = Parser.parser.parse(text, lexer=Scanner.lexer)

    type_checker = TypeChecker()
    type_checker.visit(ast)

    if not type_checker.errors and not Parser.errors:
        if len(sys.argv) > 2 and sys.argv[2] == '--ast':
            ast.printTree()
            ast.printGraph()
        else:
            Interpreter().run(ast)
