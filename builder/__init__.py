#!/usr/bin/python3
import subprocess

def run_build_command(config):
    command = config["build"].split(" ")
    subprocess.run(command)
