def RETURN(p, tab, a, funtype):
    try:
        int(p[2])
        if funtype == "int":
            if a == "javascript":
                p[0] = "\t" * tab + f"return {p[2]}"
            elif a == "python":
                p[0] = "\t" * tab + f"return {p[2]}"
            elif a == "ruby":
                p[0] = "\t" * tab + f"return {p[2]}"
    except:
        try:
            float(p[2])
            if funtype == "float":
                if a == "javascript":
                    p[0] = "\t" * tab + f"return {p[2]}"
                elif a == "python":
                    p[0] = "\t" * tab + f"return {p[2]}"
                elif a == "ruby":
                    p[0] = "\t" * tab + f"return {p[2]}"
        except:
            if funtype == "char":
                if a == "javascript":
                    p[0] = "\t" * tab + f"return {p[2]}"
                elif a == "python":
                    p[0] = "\t" * tab + f"return {p[2]}"
                elif a == "ruby":
                    p[0] = "\t" * tab + f"return {p[2]}"
