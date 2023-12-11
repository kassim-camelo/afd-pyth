import ply.lex as lex

# Lista de nomes de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Expressões regulares para cada token
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# Uma regra para reconhecer números e convertê-los para inteiros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regra para rastrear números de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres a serem ignorados
t_ignore = ' \t'

# Função de tratamento de erros
def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir o lexer
def main():
    lexer = lex.lex(input())

if __name__ == "__main__":
    main()