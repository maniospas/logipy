import re
specials = '+/%,!?:;"()<>[]#$=-/\n '
keywords = ['range', 'print', 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
logipy_keywords = []

def transform_lines(lines):
    new_lines = ["from logipy.wrappers import LogipyPrimitive, logipy_call\n"]
    for line in lines:
        if line.startswith("import ") or line.startswith("from ") or line.strip().startswith("def ") or line.strip().startswith("class "):
            new_lines.append(line)
        else:
            new_line = ""
            primitive = ""
            for c in line:
                if c in specials:
                    if c == '(' and primitive and primitive not in logipy_keywords and "." != primitive[0]:
                        primitive = "logipy_call("+primitive+","
                        c = ""
                    #elif primitive and primitive not in keywords:
                    #    primitive = "LogipyPrimitive("+primitive+")"
                    new_line += primitive+c
                    primitive = ""
                else:
                    primitive += c
            if primitive:
                new_line += "LogipyPrimitive("+primitive+")"
            new_lines.append(new_line)
    return new_lines