import logging
import os
import sys
import warnings
from datetime import datetime

import click
import coloredlogs

from fuckdl.commands import dl
from fuckdl.config import directories, filenames  # isort: split


# ---- Red & Gold UI theme ---------------------------------------------------
# ANSI escape codes used for the startup banner.
_ANSI_RESET = "\033[0m"
_ANSI_BOLD = "\033[1m"
_ANSI_RED = "\033[38;5;196m"      # bright red
_ANSI_DEEP_RED = "\033[38;5;124m"  # deeper red for accents
_ANSI_GOLD = "\033[38;5;220m"     # rich gold
_ANSI_PALE_GOLD = "\033[38;5;229m" # pale gold for sub text

# coloredlogs level / field styles tuned to the red & gold palette.
RED_GOLD_LEVEL_STYLES = {
    "spam":     {"color": "yellow", "faint": True},
    "debug":    {"color": "yellow", "faint": True},
    "verbose":  {"color": "yellow"},
    "info":     {"color": "yellow", "bold": True},      # gold
    "notice":   {"color": "yellow", "bold": True, "background": "red"},
    "warning":  {"color": "red", "bold": True},
    "success":  {"color": "yellow", "bold": True},
    "error":    {"color": "red", "bold": True},
    "critical": {"color": "white", "bold": True, "background": "red"},
}

RED_GOLD_FIELD_STYLES = {
    "asctime":     {"color": "yellow"},
    "hostname":    {"color": "red"},
    "levelname":   {"color": "yellow", "bold": True},
    "name":        {"color": "red", "bold": True},
    "programname": {"color": "yellow"},
    "username":    {"color": "yellow"},
    "message":     {"color": "white"},
}


def _print_red_gold_banner() -> None:
    """Print the Fuckdl ASCII banner in the red & gold theme."""
    # Enable ANSI on legacy Windows consoles where possible.
    if os.name == "nt":
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass

    banner_lines = [
        "  ███████╗██╗   ██╗ ██████╗██╗  ██╗██████╗ ██╗     ",
        "  ██╔════╝██║   ██║██╔════╝██║ ██╔╝██╔══██╗██║     ",
        "  █████╗  ██║   ██║██║     █████╔╝ ██║  ██║██║     ",
        "  ██╔══╝  ██║   ██║██║     ██╔═██╗ ██║  ██║██║     ",
        "  ██║     ╚██████╔╝╚██████╗██║  ██╗██████╔╝███████╗",
        "  ╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═════╝ ╚══════╝",
    ]
    bar = f"{_ANSI_DEEP_RED}{'═' * 56}{_ANSI_RESET}"
    print(bar)
    for line in banner_lines:
        print(f"{_ANSI_BOLD}{_ANSI_RED}{line}{_ANSI_RESET}")
    tagline = "Modded version of Vinetrimmer with latest updates"
    print(f"  {_ANSI_BOLD}{_ANSI_GOLD}{tagline}{_ANSI_RESET}")
    print(f"  {_ANSI_PALE_GOLD}Telegram: {_ANSI_GOLD}@barbiedrm{_ANSI_RESET}")
    print(bar)


@click.command(context_settings=dict(
    allow_extra_args=True,
    ignore_unknown_options=True,
    max_content_width=116,  # max PEP8 line-width, -4 to adjust for initial indent
))
@click.option("--debug", is_flag=True, default=False,
              help="Enable DEBUG level logs on the console. This is always enabled for log files.")
def main(debug):
    """
    Fuckdl is the most convenient command-line program to
    download videos from Playready and Widevine DRM-protected video platforms.
    """
    LOG_FORMAT = "[{levelname[0]}] {name} : {message}"
    LOG_DATE_FORMAT = ""
    LOG_STYLE = "{"

    def log_exit(self, msg, *args, **kwargs):
        self.critical(msg, *args, **kwargs)
        sys.exit(1)

    logging.Logger.exit = log_exit

    os.makedirs(directories.logs, exist_ok=True)
    logging.basicConfig(
        level=logging.DEBUG,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
        style=LOG_STYLE,
        handlers=[logging.FileHandler(
            os.path.join(directories.logs, filenames.log.format(time=datetime.now().strftime("%Y%m%d-%H%M%S"))),
            encoding="utf-8"
        )]
    )

    coloredlogs.install(
        level=logging.DEBUG if debug else logging.INFO,
        fmt=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
        style=LOG_STYLE,
        level_styles=RED_GOLD_LEVEL_STYLES,
        field_styles=RED_GOLD_FIELD_STYLES,
        handlers=[logging.StreamHandler()],
    )

    log = logging.getLogger("fuckdl")

    _print_red_gold_banner()

    log.info("Fuckdl - Restructured for Scalability")
    log.info("[Telegram]        : @barbiedrm")
    log.info(f"[Root Config]     : {filenames.user_root_config}")
    log.info(f"[Service Configs] : {directories.service_configs}")
    log.info(f"[Cookies]         : {directories.cookies}")
    log.info(f"[CDM Devices]     : {directories.devices}")
    log.info(f"[Cache]           : {directories.cache}")
    log.info(f"[Logs]            : {directories.logs}")
    log.info(f"[Temp Files]      : {directories.temp}")
    log.info(f"[Downloads]       : {directories.downloads}")

    os.environ["PATH"] = os.path.abspath("./binaries")

    if len(sys.argv) > 1 and sys.argv[1].lower() == "dl":
        sys.argv.pop(1)

    dl()


if __name__ == "__main__":
    main()
