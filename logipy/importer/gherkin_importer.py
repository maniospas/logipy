import os, glob
from logipy.logic.rules import add_rule


def import_gherkin_path(root_path=""):
    for path in glob.glob(root_path+"**/*.gherkin", recursive=True):
        if os.path.isfile(path):
            import_gherkin_file(path)


def import_gherkin_file(path):
    if not path.endswith(".gherkin"):
        raise Exception("Can only import .gherkin files: "+path)

    lines = list()
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line and line[0] != "#":
                if line[-1] == "\n":
                    line[-1] = line[:-1]
                lines.append(line)
        file.close()

    import_gherkin_lines(lines)


def import_gherkin_lines(lines):
    for rule in (" ".join(lines)).split("SCENARIO:"):
        rule = rule.strip()
        if rule:
            add_rule(rule)