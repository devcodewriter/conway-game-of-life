from src.life_grid import LifeGrid
from src.pattern import Pattern
from src import curses_views
from tomllib import loads
from pathlib import Path
from src.cli import CLI
from argparse import Namespace
import sys

PATTERN_FILE     =   Path(__file__).parent / "src/pattern.toml"

def main() -> None:
    args: Namespace = CLI.get_command_line_args(get_all_patterns)
    View = getattr(curses_views, args.view)
    if args.all:
        for pattern in get_all_patterns():
            _show_pattern(View, pattern, args)
    else:
        _show_pattern(
            View,
            get_pattern(name=args.pattern),
            args
        )

def get_pattern(name: str, filename: Path = PATTERN_FILE) -> Pattern:
    data = loads(filename.read_text(encoding="utf-8"))
    return Pattern.from_toml(name,toml_data=data[name])

def get_all_patterns(filename= PATTERN_FILE) -> list[Pattern]:
    data = loads(filename.read_text(encoding="utf-8"))
    return [
        Pattern.from_toml(name, toml_data) for name, toml_data in data.items()
    ]

def _show_pattern(View: curses_views.CursesView, pattern: Pattern, args: Namespace) -> None:
    try:
        View(pattern=pattern, generation=args.gen, frame_rate=args.fps).show()
    except Exception as error:
        raise ValueError

if __name__ == "__main__":
    main()