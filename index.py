import ply.yacc as yacc
from main import tokens
from variable import *
import sys
a = "javascript"
tab = 0
try:
    a = sys.argv[1]
except:
    print("Javascript")
# exit function
def p_log(p):
    """expression : LOG FNR STRING FNL SEMI
                  | FNR STRING FNL SEMI
    """

    global tab
    if p[1] == "log":
        if a == "javascript":
            p[0] = "\t" * tab + f"console.log{p[2]}{p[3]}{p[4]}{p[5]}"
        elif a == "python":
            p[0] = "\t" * tab + f"print{p[2]}{p[3]}{p[4]}"
        elif a == "ruby":
            p[0] = "\t" * tab + f"puts {p[2]}{p[3]}{p[4]}"
    else:
        if a == "javascript":
            p[0] = "\t" * tab + f"console.log{p[1]}{p[2]}{p[3]}{p[4]}"
        elif a == "python":
            p[0] = "\t" * tab + f"print{p[1]}{p[2]}{p[3]}"
        elif a == "ruby":
            p[0] = "\t" * tab + f"puts {p[1]}{p[2]}{p[3]}"

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
    int.INT(p,tab,a)

def p_fn(p):
    """expression : NAME NAME FNR FNL EQUAL LBRACE
                  | NAME NAME FNR FNL EQUAL
    """
    global tab
    if a == "javascript":
        p[0] = "\t" * tab + f"function {p[2]}{p[3]}{p[4]}{p[6]}"
    elif a == "python":
        p[0] = "\t" * tab + f"def {p[2]}{p[3]}{p[4]}:"
    elif a == "ruby":
        p[0] = "\t" * tab + f"def {p[2]}{p[3]}{p[4]}"
    tab += 1

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

def p_error(token):
    if token is not None:
        print(f"Line {token.lineno}, illegal token {token.value}")
    else:
        print('Unexpected end of input')

def main():
    parser = yacc.yacc(debug=0, write_tables=0)
    result = []
    with open('data.aio', 'r') as fp:
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


