import sys, traceback
from os import path


def logipy_exception_handler(type, value, tb):
    file = sys.stderr
    for line in traceback.TracebackException(type, value, tb).format():
        splt = line.split("\"",3)
        if len(splt) > 1:
            if splt[1].endswith("logipy\\wrappers.py") or splt[1].endswith("logipy\\logic\\rules.py") or splt[1].endswith("logipy\\logic\\properties.py"):
                continue
            if splt[1].endswith(".py") and path.exists(splt[1][:-3]+".lpy"):
                splt[1] = splt[1][:-3]+".lpy"
        line = "\"".join(splt)
        while True:
            found_method = line.find("logipy_call")
            if found_method == -1:
                break
            end_method = line.find(",", found_method)
            line = line[:found_method]+line[found_method+12:end_method]+"("+line[end_method+1:]

        print(line, file=file, end="")