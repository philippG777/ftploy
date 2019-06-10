#!/usr/bin/python3
from fileops import read_config, get_source_files, get_existing_files, \
    filter_unchanged_files, remove_existing_files, copy_files_to_dest

config = read_config()

source_files = get_source_files(config)
print("Source files")
print(source_files)

existing_files = get_existing_files(config)
print("Existing files")
print(existing_files)

source_files, existing_files = filter_unchanged_files(config, source_files, existing_files)
""" print("Source files")
print(source_files)
print("Existing files")
print(existing_files) """

ok = input("Remove / copy files? (yes/No): ")
if ok.lower() == "yes" or ok.lower() == "y":
    print("Removing files")
    remove_existing_files(config, existing_files)

    print("Copying files")
    copy_files_to_dest(config, source_files)

    print("Finished")
else:
    print("Aborted by user")
