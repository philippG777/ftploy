#!/usr/bin/python3
import os

def create_path(path, file):
    if path == "" or path == "/":
        return file
    else:
        return path + "/" + file

def get_file_ext(path):
    parts = path.split("/")
    file_part = parts[len(parts) - 1]       # last part
    file_part = file_part.split(".")
    return file_part[len(file_part) - 1]    # last part

def walk_dir(path):
    files = []
    if path == "":
        ls = os.listdir()
    else:
        ls = os.listdir(path)

    for item in ls:
        file_path = create_path(path, item)
        if os.path.isdir(file_path):
            files += walk_dir(file_path)
        else:
            files.append(file_path)

    return files

def file_exists(path):
    return os.path.isfile(path)

def dir_part(path):          # path has to be a file path
    parts = path.split("/")
    return "/".join(parts[0:-1])
