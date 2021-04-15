def LOG(p, tab, a):
    if p[1] == "log":
        if a == "javascript":
            p[0] = "\t" * tab + f"console.log{p[2]}{p[3]}{p[4]}{p[5]}"
        elif a == "python":
            p[0] = "\t" * tab + f"print{p[2]}{p[3]}{p[4]}"
        elif a == "ruby":
            p[0] = "\t" * tab + f"puts {p[2]}{p[3]}{p[4]}"
    elif p[1] == "(":
        if a == "javascript":
            p[0] = "\t" * tab + f"console.log{p[1]}{p[2]}{p[3]}{p[4]}"
        elif a == "python":
            p[0] = "\t" * tab + f"print{p[1]}{p[2]}{p[3]}"
        elif a == "ruby":
            p[0] = "\t" * tab + f"puts {p[1]}{p[2]}{p[3]}"
    elif p[1] == "l":
        if a == "javascript":
            p[0] = "\t" * tab + f"console.log({p[2]})"
        elif a == "python":
            p[0] = "\t" * tab + f"print({p[2]})"
        elif a == "ruby":
            p[0] = "\t" * tab + f"puts {p[2]}"
