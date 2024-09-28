import subprocess

from utils import *


def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as ex:
        log(f"[FLUX]: Error executing command: {ex}")
