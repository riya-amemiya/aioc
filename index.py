import ply.yacc as yacc
from main import tokens
from variable import *
from console import *
from function import *
import sys
a = "javascript"
tab = 0
funtype = "void"
funs = {}
variables = {}
precedence = (    #計算の優先順位を決める
    ('left', 'PLUS', 'MINUS'),
    ('right', 'ASTERISK','SLASH'),
    ('right', 'PERCENT')
)
try:
    if sys.argv[1] == "js":
        a = "javascript"
    elif sys.argv[1] == "rb":
        a = "ruby"
    elif sys.argv[1] == "py":
        a = "python"
    else:
        a  = sys.argv[1]
except:
    print("Javascript")
# exit function
def p_log(p):
    """log : LOG FNR STRING FNL SEMI
           | FNR STRING FNL SEMI
           | SHORTLOG STRING SEMI
           | LOG FNR expression FNL SEMI
           | FNR expression FNL SEMI
           | SHORTLOG expression SEMI
    """

    global tab
    log.LOG(p,tab,a)

def p_input(p):
    """expression : INT NAME EQUAL INPUT FNR STRING FNL SEMI
             | CONST INT NAME EQUAL INPUT FNR STRING FNL SEMI
             | CHAR NAME EQUAL INPUT FNR STRING FNL SEMI
             | CONST CHAR NAME EQUAL INPUT FNR STRING FNL SEMI
             | FLOAT NAME EQUAL INPUT FNR STRING FNL SEMI
             | CONST FLOAT NAME EQUAL INPUT FNR STRING FNL SEMI
    """
    global tab
    if p[1] != "const":
        #p[0] = "\t" * tab + f"let {p[2]} {p[3]} {p[4]}{p[5]}"
        if a == "javascript":
            p[4] = f"window.prompt({p[6]}, "");"
        elif a == "python":
            p[4] = f"{p[4]}{p[5]}{p[6]}{p[7]}"
        elif a == "ruby":
            p[4] = f"gets.chomp"
            p[5] = f"puts {p[6]}\n"
            if p[1] == "int":
                p[4] += ".to_i"
        if p[1] == "int":
            Int.INT(p,tab,a)
        elif p[1] == "char":
            char.CHAR(p, tab, a)
        elif p[1] == "float":
            Float.FLOAT(p, tab, a)
    else:
        if a == "javascript":
            p[5] = f"window.prompt({p[7]}, "");"
        elif a == "python":
            p[5] = f"{p[5]}{p[6]}{p[7]}{p[8]}"
        elif a == "ruby":
            p[5] = f"gets.chomp"
            p[6] = f"puts {p[7]}\n"
            if p[2] == "int":
                p[5] += ".to_i"
        if p[2] == "int":
            Int.INT(p, tab, a)
        elif p[1] == "char":
            char.CHAR(p, tab, a)
        elif p[1] == "float":
            Float.FLOAT(p, tab, a)

def p_short_if(p):
    """expression : expression QUESTION expression FN expression
    """
    global tab
    if a == "javascript":
        p[0] = "\t" * tab + f"{p[1]} {p[2]} {p[3]} {p[4]} {p[5]}"
    elif a == "python":
        p[0] = "\t" * tab + f"{p[3]} if {p[1]} else {p[5]}"
    elif a == "ruby":
        p[0] = "\t" * tab + f"{p[1]} {p[2]} {p[3]} {p[4]} {p[5]}"

def p_doubleequal(p):
    """doubleequal : expression DOUBLEEQUAL expression"""
    p[0] = f"{p[1]}{p[2]}{p[3]}"

def p_if(p):
    """expression : IF FNR doubleequal FNL FN
                  | IF FNR doubleequal FNL LBRACE
    """
    global tab
    if a == "javascript":
        p[0] = "\t" * tab + f"if {p[2]}{p[3]}{p[4]}{p[5]}" + "{"
    elif a == "python":
        p[0] = "\t" * tab + f"if {p[3]}{p[4]}{p[5]}:"
    elif a == "ruby":
        p[0] = "\t" * tab + f"if {p[2]}{p[3]}{p[4]}{p[5]}"
    tab += 1
def p_expression_binop(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression ASTERISK expression
                  | expression SLASH expression
                  | expression PERCENT expression
    """
    global tab
    try:
        int(p[3]);
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
    except:
        p[0] = "\t" * tab + f"{p[1]}{p[2]}{p[3]}"

def p_FOR_P(p):
    """expression : NAME DOUBLEEPLUS
    """
    p[0] = f"{p[1]}{p[2]}"

def p_BREAK(p):
    """expression : BREAK SEMI
    """
    p[0] = "\t" * tab + f"{p[1]}{p[2]}"

def p_FOR(p):
    """expression : FOR FNR INT NAME EQUAL NUMBER SEMI NAME LTS NUMBER SEMI expression FNL LBRACE
                  | FOR FNR INT NAME EQUAL NUMBER SEMI NAME LTR NUMBER SEMI expression FNL LBRACE
                  | FOR FNR INT NAME EQUAL NUMBER SEMI NAME LTS NUMBER SEMI expression FNL FN
                  | FOR FNR INT NAME EQUAL NUMBER SEMI NAME LTR NUMBER SEMI expression FNL FN
    """
    global tab
    if a == "javascript":
        p[0] = "\t" * tab + f"for(let {p[4]}{p[5]}{p[6]}{p[7]}{p[8]}{p[9]}{p[10]}{p[11]}{p[12]})" + "{"
    elif a == "python":
        p[0] = "\t" * tab + f"for {p[4]} in range({p[6]},{p[10]}):"
    elif a == "ruby":
        p[0] = "\t" * tab + f"for {p[4]} in {p[6]}..{int(p[10])-1} do"
    tab += 1


def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = int(p[1])

def p_expression_float(p):
    """expression : NUMBER_FLOAT"""
    p[0] = float(p[1])

def p_name(p):
    """expression : NAME"""
    p[0] = p[1]

def p_string(p):
    """expression : STRING"""
    p[0] = p[1]

def p_char(p):
    """expression : CHAR NAME EQUAL STRING SEMI
                  | CONST CHAR NAME EQUAL STRING SEMI
    """
    global tab
    global variables
    char.CHAR(p,tab,a,variables)

def p_float(p):
    """expression : FLOAT NAME EQUAL NUMBER_FLOAT SEMI
                  | CONST FLOAT NAME EQUAL NUMBER_FLOAT SEMI
    """
    global tab
    global variables
    Float.FLOAT(p, tab, a, variables)

def p_int_p(p):
    """int_p : NUMBER COMMA NUMBER"""
    p[0] = f"{p[1]}{p[2]}{p[3]}"

def p_int(p):
    """expression : INT NAME EQUAL NUMBER SEMI
                  | CONST INT NAME EQUAL NUMBER SEMI
                  | INT PR PL NAME EQUAL PR int_p PL
    """
    global tab
    global variables
    Int.INT(p, tab, a,variables)

def p_vs(p):
    """expression : NAME EQUAL expression SEMI
    """
    global tab
    global variables
    try:
        if variables[p[1]][1] == "const":
            print("定数です!")
        else:
            if variables[p[1]][0] == "int":
                try:
                    p[0] = f"{p[1]}{p[2]}{int(p[3])}"
                except:
                    print("int型じゃありません")
            elif variables[p[1]][0] == "float":
                try:
                    p[0] = f"{p[1]}{p[2]}{float(p[3])}"
                except:
                    print("float型じゃありません")
            elif variables[p[1]][0] == "char":
                try:
                    int(p[3])
                    float(p[3])
                    print("char型じゃありません")
                except:
                    p[0] = f"{p[1]}{p[2]}{p[3]}"
    except:
        print(f"{p[1]}は宣言されてません")

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
    global funs
    funs[p[2]] = [p[1],p[4] if p[4] != ")" else ""]
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
            p[0] = "\t" * tab + f"{p[2]}{p[3]}{p[4]}"
        elif a == "python":
            p[0] = "\t" * tab + f"{p[2]}{p[3]}{p[4]}"
        elif a == "ruby":
            p[0] = "\t" * tab + f"{p[2]}{p[3]}{p[4]}"
    except:
        if a == "javascript":
            p[0] = "\t" * tab + f"{p[2]}"
        elif a == "python":
            p[0] = "\t" * tab + f"{p[2]}"
        elif a == "ruby":
            p[0] = "\t" * tab + f"{p[2]}"


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
        p[0] = "\t" * tab + "}"
    elif a == "python":
        p[0] = "\t" * tab + f""
    elif a == "ruby":
        p[0] = "\t" * tab + f"end"
def p_cfn(p):
    """expression : NAME FNR FNL SEMI
                  | NAME FNR expression FNL SEMI
    """
    global tab
    tab -= 1
    for n in funs:
        if funs[n][1] and p[3] == ")":
            print(f"警告!\n引数{funs[n][1]}が渡されてません!")
    if not funs[n][1] and p[3] == ")":
        if a == "javascript":
            p[0] = "\t" * tab + f"{p[1]}{p[2]}{p[3]}"
        elif a == "python":
            p[0] = "\t" * tab + f"{p[1]}{p[2]}{p[3]}"
        elif a == "ruby":
            p[0] = "\t" * tab + f"{p[1]}{p[2]}{p[3]}"
    else:
        if a == "javascript":
            p[0] = "\t" * tab + f"{p[1]}{p[2]}{p[3]}{p[4]}"
        elif a == "python":
            p[0] = "\t" * tab + f"{p[1]}{p[2]}{p[3]}{p[4]}"
        elif a == "ruby":
            p[0] = "\t" * tab + f"{p[1]}{p[2]}{p[3]}{p[4]}"

def p_comment(p):
    """expression : COMMENT"""
    p[0] = ""

def p_end(p):
    """expression : END"""
    global tab
    tab -= 1
    if a == "javascript":
        p[0] = "\t" * tab + "}"
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
    with open(sys.argv[2], 'r') as fp:
        for line in fp:
            try:
                result += [parser.parse(line)]
            except EOFError:
                break
    result = [a for a in result if a != '']
    with open(f'{sys.argv[3]}.{"js" if a == "javascript" else "py" if a == "python" else "rb"}', mode='w') as f:
        f.write('\n'.join(result))

if __name__ == '__main__':
    #yacc_test()
    main()


