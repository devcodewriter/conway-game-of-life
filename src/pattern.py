from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Pattern:
    name: str
    alive_cells: set[tuple[int, int]]

    @classmethod
    def from_toml(cls, name: str, toml_data: dict[str, list[int]]) -> Pattern:
        return cls(
            name,
            alive_cells={tuple(cell) for cell in toml_data["alive_cells"]}
        )
