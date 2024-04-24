from src.life_grid import LifeGrid
from src.pattern import Pattern
from src.views import CursesView
from tomllib import loads
from pathlib import Path

PATTERN_FILE     =   Path(__file__).parent / "src/pattern.toml"

def main() -> None:
    blinker = get_pattern("Blinker")
    grid = LifeGrid(blinker)
    print(grid)
    print(grid.display_grid((0,0, 5, 5)))

    grid.evolve()
    print(grid)
    print(grid.display_grid((0,0, 5, 5)))

    grid.evolve()
    print(get_all_patterns())

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