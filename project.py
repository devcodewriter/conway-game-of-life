from src.life_grid import LifeGrid
from src.pattern import Pattern
from src.curses_views import CursesView
from tomllib import loads
from pathlib import Path

PATTERN_FILE     =   Path(__file__).parent / "src/pattern.toml"

def main() -> None:
    curses_view = CursesView(get_pattern("Pulsar"), generation=150)
    curses_view.show()

def get_pattern(name: str, filename: Path = PATTERN_FILE) -> Pattern:
    data = loads(filename.read_text(encoding="utf-8"))
    return Pattern.from_toml(name,toml_data=data[name])

def get_all_patterns(filename= PATTERN_FILE) -> list[Pattern]:
    data = loads(filename.read_text(encoding="utf-8"))
    return [
        Pattern.from_toml(name, toml_data) for name, toml_data in data.items()
    ]

if __name__ == "__main__":
    main()