import os, glob
import logipy.importer.text_converter


temp_files = list()


def convert_path(root_path=""):
    for path in glob.glob(root_path+"**/*.lpy", recursive=True):
        if os.path.isfile(path):
            convert_file(path)


def convert_file(path):
    if not path.endswith(".lpy"):
        raise Exception("Can only convert .lpy files: "+path)
    lines = list()
    with open(path, "r") as file:
        for line in file:
            lines.append(line)
        file.close()
    lines = logipy.importer.text_converter.transform_lines(lines)
    with open(path[:-4]+".py", "w") as save_file:
        temp_files.append(path[:-4]+".py")
        for line in lines:
            save_file.write(line)
        save_file.close()


def cleanup():
    for temp_file in temp_files:
        os.remove(temp_file)