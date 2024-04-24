from collections import defaultdict
from src.pattern import Pattern
from typing import Dict
ALIVE   = "\u2764"
DEAD    = "\u2610"

class LifeGrid:
    def __init__(self, pattern: Pattern) -> None:
        self.pattern = pattern
    
    def evolve(self) -> None:
        neighbors = (
            (-1, -1),   # Above left
            (-1, 0),    # Above
            (-1, 1),    # Above right
            (0, -1),    # Left
            (0, 1),     # Right
            (1, -1),    # Below left
            (1, 0),     # Below
            (1, 1),     # Below right
        )
        living_neighbors: Dict[tuple[int, int], int] = defaultdict(int)
        for row, col in self.pattern.alive_cells:
            for drow, dcol in neighbors:
                living_neighbors[(row + drow, col + dcol)] += 1
        will_stay_alive: set[tuple[int,int]] = {
            cell for cell, num in living_neighbors.items() if num in {2,3}
        } & self.pattern.alive_cells
        will_become_alive: set[tuple[int,int]] = {
            cell for cell, num in living_neighbors.items() if num == 3
        } - self.pattern.alive_cells
        self.pattern.alive_cells = will_stay_alive | will_become_alive


    def display_grid(self, bbox: tuple[int, int, int, int]) -> str:
        start_col, start_row, end_col, end_row = bbox
        display: list[str] = [self.pattern.name.center(2 * (end_col - start_col))]
        for row in range(start_row, end_row):
            display_row: list[str] = [
                ALIVE if (row, col) in self.pattern.alive_cells else DEAD
                for col in range(start_col, end_col)
            ]
            display.append(" ".join(display_row))
        return "\n".join(display)

    def __str__(self) -> str:
        return (
            f"{self.pattern.name}:\n"
            f"Alive cells -> {sorted(self.pattern.alive_cells)}"
        )