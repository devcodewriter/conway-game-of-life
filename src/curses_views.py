from src.pattern import Pattern
import curses
from curses import window
from time import sleep
from src.life_grid import LifeGrid

class CursesView:

    def __init__(self, pattern: Pattern, generation: int =10, frame_rate: int = 7, bbox: (int, int, int, int) = (0, 0, 40, 40)) -> None:
        self.pattern    = pattern
        self.generation = generation
        self.frame_rate = frame_rate
        self.bbox       = bbox

    def show(self) -> None :
        curses.wrapper(self._draw)

    def _draw(self, screen: window) -> None:
        grid = LifeGrid(self.pattern)
        curses.curs_set(0)
        screen.clear()
        try:
            screen.addstr(0, 0, grid.display_grid(self.bbox))
        except curses.error:
            raise ValueError(f"Terminal too smal for {self.pattern.name} pattern")
        for _ in range(self.generation):
            grid.evolve()
            screen.addstr(0, 0, grid.display_grid(self.bbox))
            screen.refresh()
            sleep(1 / self.frame_rate)