import ply.lex as lex

tokens = (
    'NAME',
    'NUMBER',
    'LBRACE',
    'RBRACE',
    'SEMI',
    'STRING',
    'FNL',
    'FNR',
    'EQUAL',
    'LOG',
    'INT',
    'CHAR',
    'FLOAT',
    'NUMBER_FLOAT',
    'CONST',
    'COMMENT'
)

# t_STRING = '"[a-zA-Z][a-zA-Z0-9]*"'
t_STRING = '"[^\t\n\r\f\v]*"'
t_NUMBER = '[0-9.edED+-]+'
t_NUMBER_FLOAT = "[0-9.edED+-]+\.[0-9.edED+-]+"
t_LBRACE = '{'
t_RBRACE = '}'
t_SEMI = ';'
t_FNL = '\)'
t_FNR = '\('
t_EQUAL = '='
t_ignore = ' '
t_NAME = '[a-zA-Z][a-zA-Z0-9]*'


def t_CONST(t):
    r"""const"""
    return t


def t_FLOAT(t):
    r"""float"""
    return t


def t_CHAR(t):
    r"""char"""
    return t


def t_LOG(t):
    r"""log"""
    return t


def t_INT(t):
    r"""int"""
    return t


def t_COMMENT(t):
    """/\*[\s\S]*?\*/|//.*"""
    t.lexer.lineno += t.value.count('\n')
    return t


def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)
    pass


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


def lex_test():
    f = open('data.aio', 'r')
    data = f.read()
    f.close()

    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


if __name__ == '__main__':
    lex_test()
