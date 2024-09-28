import sys

from flux_cfg import load_flux_config
from flux_exec import execute_command
from flux_utils import *


def start():
    if len(sys.argv) < 2:
        log("[Flux] Usage: flux --<function_name>")
        sys.exit(1)

    args = sys.argv[1][2:]
    config = load_flux_config('flux.json')

    if 'flux' in config and args in config['flux']:
        command = config['flux'][args]
        log(f"Executing: {command}")
        execute_command(command)
    elif args.lower() in ['version', 'help']:
        info(config)
    else:
        log(
            f"Function / Command '{args}' not found in flux configuration and is not a valid argument! "
            f"Type 'help' for a list of commands or arguments."
        )
