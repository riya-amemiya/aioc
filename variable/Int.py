def INT(p, tab, a,variables):
    if p[1] != "const":
        if p[2] != "[":
            variables[p[2]] = [p[1], ""]
            if a == "javascript":
                p[0] = "\t" * tab + f"let {p[2]} {p[3]} {p[4]}"
            elif a == "python":
                p[0] = "\t" * tab + f"{p[2]} {p[3]} {p[4]}"
            elif a == "ruby":
                p[0] = '\t' * tab + f"{p[5]} {p[2]} {p[3]} {p[4]}"
        else:
            variables[p[4]] = [p[1], ""]
            if a == "javascript":
                p[0] = "\t" * tab + f"let {p[4]} {p[5]} {p[6]}{p[7]}{p[8]}"
            elif a == "python":
                p[0] = "\t" * tab + f"{p[4]} {p[5]} {p[6]}{p[7]}{p[8]}"
            elif a == "ruby":
                p[0] = '\t' * tab + f"{p[4]} {p[5]} {p[6]}{p[7]}{p[8]}"
    else:
        variables[p[3]] = [p[2], p[1]]
        if a == "javascript":
            p[0] = "\t" * tab + f"const {p[3]} {p[4]} {p[5]}"
        elif a == "python":
            p[0] = "\t" * tab + f"{p[3].upper()} {p[4]} {p[5]}"
        elif a == "ruby":
            p[0] = "\t" * tab + f"{p[6]}{p[3].upper()} {p[4]} {p[5]}"



