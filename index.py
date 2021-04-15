import ply.yacc as yacc
from main import tokens
from variable import *
from console import *
from function import *
import sys
a = "javascript"
tab = 0
funtype = "void"
precedence = (    #計算の優先順位を決める
    ('left', 'PLUS', 'MINUS'),
    ('right', 'ASTERISK','SLASH'),
    ('right', 'PERCENT')
)
try:
    a = sys.argv[1]
except:
    print("Javascript")
# exit function
def p_log(p):
    """expression : LOG FNR STRING FNL SEMI
                  | FNR STRING FNL SEMI
                  | SHORTLOG STRING
                  | LOG FNR expression FNL SEMI
                  | FNR expression FNL SEMI
                  | SHORTLOG expression
    """

    global tab
    log.LOG(p,tab,a)

def p_input(p):
    """expression : NAME EQUAL INPUT FNR STRING FNL
    """
    global tab
    if a == "javascript":
        p[0] = "\t" * tab + f"{p[1]}{p[2]}{p[4]}" + "{"
    elif a == "python":
        p[0] = "\t" * tab + f"{p[1]}{p[2]}{p[3]}{p[4]}{p[5]}{p[6]}"
    elif a == "ruby":
        p[0] = "\t" * tab + f"if {p[2]}{p[3]}{p[4]}"

def p_if(p):
    """expression : IF expression DOUBLEEQUAL expression FN
                  | IF expression DOUBLEEQUAL expression LBRACE
    """
    global tab
    if a == "javascript":
        p[0] = "\t" * tab + f"if {p[2]}{p[3]}{p[4]}" + "{"
    elif a == "python":
        p[0] = "\t" * tab + f"if {p[2]}{p[3]}{p[4]}:"
    elif a == "ruby":
        p[0] = "\t" * tab + f"if {p[2]}{p[3]}{p[4]}"
    tab += 1
def p_expression_binop(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression ASTERISK expression
                  | expression SLASH expression
                  | expression PERCENT expression
    """
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '%':
        p[0] = p[1] % p[3]

def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = int(p[1])

def p_string(p):
    """expression : STRING"""
    p[0] = p[1]

def p_char(p):
    """expression : CHAR NAME EQUAL STRING SEMI
                  | CONST CHAR NAME EQUAL STRING SEMI
    """
    global tab
    char.CHAR(p,tab,a)

def p_float(p):
    """expression : FLOAT NAME EQUAL NUMBER_FLOAT SEMI
                  | CONST FLOAT NAME EQUAL NUMBER_FLOAT SEMI
    """
    global tab
    float.FLOAT(p,tab,a)

def p_int(p):
    """expression : INT NAME EQUAL NUMBER SEMI
                  | CONST INT NAME EQUAL NUMBER SEMI
    """
    global tab
    Int.INT(p, tab, a)

def p_fn(p):
    """expression : INT NAME FNR FNL FN
                  | INT NAME FNR FNL LBRACE
                  | CHAR NAME FNR FNL FN
                  | CHAR NAME FNR FNL LBRACE
                  | FLOAT NAME FNR FNL FN
                  | FLOAT NAME FNR FNL LBRACE
                  | VOID NAME FNR FNL FN
                  | VOID NAME FNR FNL LBRACE
                  | INT NAME FNR expression FNL FN
                  | INT NAME FNR expression FNL LBRACE
                  | CHAR NAME FNR expression FNL FN
                  | CHAR NAME FNR expression FNL LBRACE
                  | FLOAT NAME FNR expression FNL FN
                  | FLOAT NAME FNR expression FNL LBRACE
                  | VOID NAME FNR expression FNL FN
                  | VOID NAME FNR expression FNL LBRACE
    """
    global tab
    global funtype
    funtype = p[1]
    function.FUN(p,tab,a)
    tab += 1

def p_variable(p):
    """expression : INT NAME
                  | INT NAME COMMA expression
                  | INT NAME EQUAL NUMBER
                  | INT NAME EQUAL NUMBER COMMA expression
    """
    try:
        if a == "javascript":
            p[0] = f"{p[2]}{p[3]}{p[4]}"
        elif a == "python":
            p[0] = f"{p[2]}{p[3]}{p[4]}"
        elif a == "ruby":
            p[0] = f"{p[2]}{p[3]}{p[4]}"
    except:
        if a == "javascript":
            p[0] = f"{p[2]}"
        elif a == "python":
            p[0] = f"{p[2]}"
        elif a == "ruby":
            p[0] = f"{p[2]}"


def p_return(p):
    """expression : RETURN expression SEMI"""
    global tab
    global funtype
    RETURN.RETURN(p, tab, a,funtype)

def p_rbrace(p):
    """expression : RBRACE"""
    global tab
    tab -= 1
    if a == "javascript":
        p[0] = "\t" * tab + f"{p[1]}"
    elif a == "python":
        p[0] = "\t" * tab + f""
    elif a == "ruby":
        p[0] = "\t" * tab + f"end"

def p_comment(p):
    """expression : COMMENT"""
    p[0] = ""

def p_end(p):
    """expression : END"""
    global tab
    if a == "javascript":
        p[0] = "\t" * tab + f"{p[1]}"
    elif a == "python":
        p[0] = "\t" * tab + f""
    elif a == "ruby":
        p[0] = "\t" * tab + f"end"

def p_error(token):
    if token is not None:
        print(f"Line {token.lineno}, illegal token {token.value} type {token.type}")
    else:
        print('Unexpected end of input')

def main():
    parser = yacc.yacc(debug=0, write_tables=0)
    result = []
    with open('data.aioc', 'r') as fp:
        for line in fp:
            try:
                result += [parser.parse(line)]
            except EOFError:
                break
    result = [a for a in result if a != '']
    with open(f'test.{"js" if a == "javascript" else "py" if a == "python" else "rb"}', mode='w') as f:
        f.write('\n'.join(result))

if __name__ == '__main__':
    #yacc_test()
    main()


