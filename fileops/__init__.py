#!/usr/bin/python3
import json
import os
import filecmp
from shutil import copyfile
from .basic import walk_dir, get_file_ext, create_path, file_exists, dir_part

def read_config(config_file = "deploy.json"):
    path = create_path(os.getcwd(), config_file)
    with open(path) as content:
        config = json.load(content)
    return config

def walk_included_files(include_ext):
    all_files = walk_dir("")    # start
    files = []
    for f in all_files:
        ext = get_file_ext(f)
        if ext in include_ext:
            files.append(f)
    return files

def add_included_files(files, include):   # add included files to file-list
    for f in include:
        src_path = create_path(os.getcwd(), f)
        if file_exists(src_path):           # only add if existing
            files.append(f)
    return files

def filter_excluded_files(files, exclude):    # filter out excluded files
    filtered_files = []
    for f in files:
        if not f in exclude:
            filtered_files.append(f)
    
    return filtered_files

def get_source_files(config):
    initial_cwd = os.getcwd()
    if config["source"] != "" and config["source"] != "/":
        os.chdir(config["source"])
    
    files = walk_included_files(config["include_file_ext"])
    files = add_included_files(files, config["include"])
    files = filter_excluded_files(files, config["exclude"])

    os.chdir(initial_cwd)
    return files

def get_existing_files(config):
    initial_cwd = os.getcwd()
    os.chdir(config["dest"])
    
    files = walk_included_files(config["include_file_ext"])

    os.chdir(initial_cwd)

    for f in config["include"]:
        if file_exists(create_path(config["dest"], f)):
            files.append(f)

    return files

def filter_unchanged_files(config, src_files, dest_files):
    for f in src_files:
        if f in dest_files:                                     # files that are in both lists
            src_path = create_path(config["source"], f)
            dest_path = create_path(config["dest"], f)
            if filecmp.cmp(src_path, dest_path):                # unchanged
                src_files.remove(f)                             # remove
                dest_files.remove(f)
    return src_files, dest_files

def remove_existing_files(config, existing_files):
    for f in existing_files:
        path = create_path(config["dest"], f)
        os.remove(path)

def copy_files_to_dest(config, src_files):
    for f in src_files:
        print("Copy %s" % f)
        src_path = create_path(config["source"], f)
        dest_path = create_path(config["dest"], f)

        os.makedirs(dir_part(dest_path), exist_ok=True)

        copyfile(src_path, dest_path)
