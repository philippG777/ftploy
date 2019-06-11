#!/usr/bin/python3
from fileops import read_config, get_source_files, get_existing_files, \
    filter_unchanged_files, remove_existing_files, copy_files_to_dest
from builder import run_build_command

print("""   __ _        _          
  / _| |_ _ __| |___ _  _ 
 |  _|  _| '_ \ / _ \ || |
 |_|  \__| .__/_\___/\_, |
         |_|         |__/ """)

print("Reading deploy.json")
config = read_config()
print()

print("Running build command")
run_build_command(config)
print()

print("Analyzing source-files")
source_files = get_source_files(config)
print("Source files: ", source_files)
print()

print("Analyzing existing files")
existing_files = get_existing_files(config)
print("Existing files: ", existing_files)
print()

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

    print()
    print("Finished")
else:
    print("Aborted by user")
