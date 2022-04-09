# Maksymilian Wojnar

import ply.yacc as yacc

from scanner import Scanner
from m_ast import AST

tokens = Scanner.tokens

precedence = (
    ('nonassoc', 'IFX'),
    ('nonassoc', 'ELSE'),
    ('right', '=', 'MULASSIGN', 'DIVASSIGN', 'ADDASSIGN', 'SUBASSIGN'),
    ('nonassoc', '>', '<', 'GE', 'LE', 'EQ', 'NE'),
    ('left', 'DOTADD', 'DOTSUB', '+', '-'),
    ('left', 'DOTMUL', 'DOTDIV', '*', '/'),
    ('right', 'UMINUS'),
    ('left', '\''),
)

errors = False


def p_error(p):
    global errors
    errors = True

    if p:
        print(f"Syntax error at line {p.lineno}: LexToken({p.type}, '{p.value}')")

        while (tok := parser.token()) is not None and tok.type not in (';', '}', ')', ']'):
            pass

        parser.errok()
        return tok
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions
               | """
    if len(p) > 1:
        p[0] = AST.Program(p[1])
        p[0].lineno = p.lineno(1)


def p_instructions(p):
    """instructions : instructions instruction
                    | instruction """
    if len(p) == 3:
        p[0] = p[1]
        p[0].instructions.append(p[2])
    else:
        p[0] = AST.Instructions(p[1])

    p[0].lineno = p.lineno(1)


def p_instructions_block(p):
    """instruction : '{' instructions '}' """
    p[0] = AST.Block(p[2])
    p[0].lineno = p.lineno(1)


def p_control_statements(p):
    """instruction : RETURN ';'
                   | RETURN expr ';'
                   | BREAK ';'
                   | CONTINUE ';' """
    if p.slice[1].type == 'RETURN' and len(p) == 4:
        p[0] = AST.Return(p[2])
    elif p.slice[1].type == 'RETURN':
        p[0] = AST.Return()
    elif p.slice[1].type == 'BREAK':
        p[0] = AST.Break()
    elif p.slice[1].type == 'CONTINUE':
        p[0] = AST.Continue()

    p[0].lineno = p.lineno(1)


def p_print(p):
    """instruction : PRINT expressions ';' """
    p[0] = AST.Print(p[2])
    p[0].lineno = p.lineno(1)


def p_assign(p):
    """instruction : var '=' expr ';'
                   | var ADDASSIGN expr ';'
                   | var SUBASSIGN expr ';'
                   | var MULASSIGN expr ';'
                   | var DIVASSIGN expr ';' """
    if p[2] == '=':
        p[0] = AST.AssignExpr(p[1], p[3])
    elif p[2] == '+=':
        p[0] = AST.AddAssignExpr(p[1], p[3])
    elif p[2] == '-=':
        p[0] = AST.SubAssignExpr(p[1], p[3])
    elif p[2] == '*=':
        p[0] = AST.MulAssignExpr(p[1], p[3])
    elif p[2] == '/=':
        p[0] = AST.DivAssignExpr(p[1], p[3])

    p[0].lineno = p.lineno(2)


def p_while_statement(p):
    """instruction : WHILE '(' condition ')' instruction """
    p[0] = AST.WhileStatement(p[3], p[5])
    p[0].lineno = p.lineno(1)


def p_for_statement(p):
    """instruction : FOR ID '=' range instruction
                   | FOR '(' ID '=' range ')' instruction """
    if len(p) == 6:
        p[0] = AST.ForStatement(p[2], p[4], p[5])
    else:
        p[0] = AST.ForStatement(p[3], p[5], p[7])

    p[0].lineno = p.lineno(1)


def p_if_statement(p):
    """instruction : IF '(' condition ')' instruction %prec IFX
                   | IF '(' condition ')' instruction ELSE instruction """
    if len(p) == 8:
        p[0] = AST.IfStatement(p[3], p[5], p[7])
    else:
        p[0] = AST.IfStatement(p[3], p[5])

    p[0].lineno = p.lineno(1)
    

def p_condition(p):
    """condition : expr EQ expr
                 | expr NE expr
                 | expr GE expr
                 | expr LE expr
                 | expr '>' expr
                 | expr '<' expr """
    if p[2] == '==':
        p[0] = AST.EQExpr(p[1], p[3])
    elif p[2] == '!=':
        p[0] = AST.NEExpr(p[1], p[3])
    elif p[2] == '>=':
        p[0] = AST.GEExpr(p[1], p[3])
    elif p[2] == '<=':
        p[0] = AST.LEExpr(p[1], p[3])
    elif p[2] == '<':
        p[0] = AST.LowerExpr(p[1], p[3])
    elif p[2] == '>':
        p[0] = AST.GreaterExpr(p[1], p[3])

    p[0].lineno = p.lineno(2)


def p_id_var(p):
    """var : ID """
    p[0] = AST.Variable(p[1])
    p[0].lineno = p.lineno(1)


def p_vector_range_expr(p):
    """expr : ID '[' range ']' """
    p[0] = AST.VectorRange(p[1], p[3])
    p[0].lineno = p.lineno(1)


def p_vector_range_var(p):
    """var : ID '[' range ']' """
    p[0] = AST.VectorRange(p[1], p[3])
    p[0].lineno = p.lineno(1)


def p_vector_el_var(p):
    """var : ID '[' expr ']'
           | ID '[' expr ',' expr ']' """
    p[0] = vector_el(p)


def p_vector_el_expr(p):
    """expr : ID '[' expr ']'
            | ID '[' expr ',' expr ']' """
    p[0] = vector_el(p)


def vector_el(p):
    if len(p) == 5:
        node = AST.VectorField(p[1], p[3])
    else:
        node = AST.VectorField(p[1], p[3], p[5])

    node.lineno = p.lineno(1)
    return node


def p_unary_minus_expression(p):
    """expr : '-' expr %prec UMINUS """
    p[0] = AST.UnaryMinus(p[2])
    p[0].lineno = p.lineno(1)


def p_binary_expression(p):
    """expr : expr '+' expr
            | expr '-' expr
            | expr '*' expr
            | expr '/' expr
            | expr DOTADD expr
            | expr DOTSUB expr
            | expr DOTMUL expr
            | expr DOTDIV expr """
    if p[2] == '+':
        p[0] = AST.AddExpr(p[1], p[3])
    elif p[2] == '-':
        p[0] = AST.SubExpr(p[1], p[3])
    elif p[2] == '*':
        p[0] = AST.MulExpr(p[1], p[3])
    elif p[2] == '/':
        p[0] = AST.DivExpr(p[1], p[3])
    elif p[2] == '.+':
        p[0] = AST.DotAddExpr(p[1], p[3])
    elif p[2] == '.-':
        p[0] = AST.DotSubExpr(p[1], p[3])
    elif p[2] == '.*':
        p[0] = AST.DotMulExpr(p[1], p[3])
    elif p[2] == './':
        p[0] = AST.DotDivExpr(p[1], p[3])

    p[0].lineno = p.lineno(2)


def p_brackets_expression(p):
    """expr : '(' expr ')' """
    p[0] = p[2]
    p[0].lineno = p.lineno(1)


def p_transpose_expression(p):
    """expr : expr "'" """
    p[0] = AST.Transpose(p[1])
    p[0].lineno = p.lineno(2)


def p_function_expression(p):
    """expr : EYE '(' expr ')'
            | ZEROS '(' expr ')'
            | ONES '(' expr ')' """
    if p.slice[1].type == 'EYE':
        p[0] = AST.Eye(p[3])
    elif p.slice[1].type == 'ZEROS':
        p[0] = AST.Zeros(p[3])
    elif p.slice[1].type == 'ONES':
        p[0] = AST.Ones(p[3])

    p[0].lineno = p.lineno(1)


def p_float_expr(p):
    """expr : FLOATNUM """
    p[0] = AST.FloatNum(p[1])
    p[0].lineno = p.lineno(1)


def p_int_expr(p):
    """expr : INTNUM """
    p[0] = AST.IntNum(p[1])
    p[0].lineno = p.lineno(1)


def p_string_expr(p):
    """expr : STRING """
    p[0] = AST.String(p[1])
    p[0].lineno = p.lineno(1)


def p_id_expr(p):
    """expr : ID """
    p[0] = AST.Variable(p[1])
    p[0].lineno = p.lineno(1)


def p_vector_expr(p):
    """expr : '[' expressions ']' """
    p[0] = AST.Vector(p[2])
    p[0].lineno = p.lineno(1)


def p_range_vector_expr(p):
    """expr : '[' range ']' """
    p[0] = AST.Vector(p[2])
    p[0].lineno = p.lineno(1)


def p_expressions(p):
    """expressions : expressions ',' expr
                   | expr """
    if len(p) == 4:
        p[0] = p[1]
        p[0].expressions.append(p[3])
    else:
        p[0] = AST.Expressions(p[1])

    p[0].lineno = p.lineno(1)


def p_range(p):
    """range : expr ':' expr """
    p[0] = AST.Range(p[1], p[3])
    p[0].lineno = p.lineno(2)


parser = yacc.yacc()
