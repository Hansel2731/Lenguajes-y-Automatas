import ply.lex as lex

tokens = (
    'NUMERO',
    'COS',
    'SEN',
    'Suma',
    'Resta',
    'Multiplicacion',
    'Division',
    'Diferente',
    'Igual',
    'Mayor',
    'Mayor_Igual',
    'Menor',
    'Menor_Igual',
    'Y',
    'Imprimir',
    'STRING',
    'Agrupar_I',
    'Agrupar_F',
    'TAN',
    'IF',
    'ELSE',
    'Encapsular_I',
    'Encapsular_F'
)

t_COS = r'cos'
t_SEN = r'sen'
t_TAN = r'tan'
t_Agrupar_I = r'\('
t_Agrupar_F = r'\)'
t_Suma = r'\+'
t_Resta = r'-'
t_Multiplicacion = r'\*'
t_Division = r'/'
t_Diferente = r'!='
t_Igual = r'=='
t_Mayor = r'>'
t_Mayor_Igual = r'>='
t_Menor = r'<'
t_Menor_Igual = r'<='
t_Y = r'&&'
t_Imprimir = r'imp'
t_IF = r'if'
t_ELSE = r'else'
t_Encapsular_I = r'\{'
t_Encapsular_F = r'\}'

# Espacios y tabs
t_ignore = ' \t'

# Saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\"]|\\")*\"'
    t.value = t.value[1:-1]
    return t


def t_error(t):
    print(f"Caracter Desconocido '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

