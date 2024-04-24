from argparse import ArgumentParser, Namespace
from src import __version__, curses_views, pattern
from pathlib import Path

class CLI:

    @classmethod
    def get_command_line_args(cls, get_all_patterns) -> Namespace:
        parser = ArgumentParser(
            prog="Conway's Game Of Life",
            description="A Conway's Game Of Life in your terminal"
        )

        parser.add_argument(
            "--version", action="version", version=f"%(prog)s v{__version__}")
        
        parser.add_argument(
            "-p",
            "--pattern",
            choices=[pattern.name for pattern in get_all_patterns()],
            default="Bunnies",
            help="Take a pattern for the Game of Life (default: %(default)s)"
        )

        parser.add_argument(
            "-a",
            "--all",
            action="store_true",
            help="Show all the available patterns in a sequence"
        )

        parser.add_argument(
            "-v",
            "--view",
            choices=curses_views.__all__,
            default="CursesView",
            help="Display the life grid in a specific view (default: %(default)s)"
        )

        parser.add_argument(
            "-g",
            "--gen",
            metavar="NUM_GENERATIONS",
            type=int,
            default=10,
            help="Number of generations (default: %(default)s)"
        )

        parser.add_argument(
            "-f",
            "--fps",
            metavar="FRAMES_PER_SECOND",
            type=int,
            default=7,
            help="Frames per second (default: %(default)s)"
        )

        return parser.parse_args()