banner = """
███████╗██╗     ██╗   ██╗██╗  ██╗
██╔════╝██║     ██║   ██║╚██╗██╔╝
█████╗  ██║     ██║   ██║ ╚███╔╝ 
██╔══╝  ██║     ██║   ██║ ██╔██╗ 
██║     ███████╗╚██████╔╝██╔╝ ██╗
╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝
"""


def log(message):
    print("[Flux] " + message)


def info(config):
    print(banner)
    log("Available commands in flux.json:")
    if 'flux' in config:
        for command in config['flux']:
            log(f"  --{command}")
    else:
        log("  No commands found in flux configuration.")
