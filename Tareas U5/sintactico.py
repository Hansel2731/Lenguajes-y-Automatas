import ply.yacc as yacc

import math
file = open("libro.txt")
from lexico import tokens

# Reglas de gramática
def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_expr(p):
    '''statement : expression'''
    p[0] = p[1]

def p_expression_number(p):
    '''expression : NUMERO'''
    p[0] = p[1]

def p_expression_operadores(p):
    '''expression : expression Suma expression
                  | expression Resta expression
                  | expression Multiplicacion expression
                  | expression Division expression
                  | expression Igual expression
                  | expression Diferente expression
                  | expression Menor expression
                  | expression Menor_Igual expression
                  | expression Mayor expression
                  | expression Mayor_Igual expression
                  | expression Y expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '&&':
        p[0] = p[1] and p[3]

def p_expression_imp(p):
    'expression : Imprimir Agrupar_I STRING Agrupar_F'
    p[0] = p[3]

def p_expression_cos(p):
    'expression : COS Agrupar_I NUMERO Agrupar_F'
    p[0] = math.cos(math.radians(p[3]))

def p_expression_sen(p):
    'expression : SEN Agrupar_I NUMERO Agrupar_F'
    p[0] = math.sin(math.radians(p[3]))

def p_expression_tan(p):
    'expression : TAN Agrupar_I NUMERO Agrupar_F'
    p[0] = math.tan(math.radians(p[3]))

def p_statement_if(p):
    '''statement : IF Agrupar_I condition Agrupar_F Encapsular_I statements Encapsular_F else_statement'''
    p[0] = ('if', p[3], p[6], p[8])

def p_else_statement(p):
    '''else_statement : ELSE Encapsular_I statements Encapsular_F
                      | empty'''
    if len(p) == 5:
        p[0] = ('else', p[3])
    else:
        p[0] = None

def p_condition(p):
    '''condition : expression'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Syntax error")


parser = yacc.yacc()

# Función para ejecutar el código
def execute(node):
    if isinstance(node, list):
        for subnode in node:
            execute(subnode)
    elif isinstance(node, tuple):
        if node[0] == 'if':
            condition = node[1]
            if condition:
                execute(node[2])
            elif node[3] is not None and node[3][0] == 'else':
                execute(node[3][1])
        elif isinstance(node, str):
            print(node)  # Imprimir la cadena directamente
        else:
            print(node)  # Para otros casos de expresiones
    else:
        if node is not None:
            print(node)

def parse_input(a):
    result = parser.parse(a)
    return result


a = file.read()
results = parse_input(a)
execute(results)
