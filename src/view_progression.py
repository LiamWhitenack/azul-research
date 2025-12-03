from colorama import Fore, Style, init

from src.types import GameProgression, WallType

init(autoreset=True)

COLORS = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.WHITE]


def colored(text: str, color: str, bold: bool = False) -> str:
    if bold:
        return Style.BRIGHT + color + text + Style.RESET_ALL
    return color + text + Style.RESET_ALL


def mark_placements_stale(grid: list[list[str]]) -> list[list[str]]:
    new_grid = []
    for row in grid:
        new_row = []
        for cell in row:
            if isinstance(cell, str):
                # Remove bold
                cleaned = cell.replace(Style.BRIGHT, "")
                # Replace X with O
                cleaned = cleaned.replace("X", "O")
                new_row.append(cleaned)
            else:
                new_row.append(cell)
        new_grid.append(new_row)
    return new_grid


def empty_grid() -> list[list[str]]:
    return [[" " for _ in range(6)] for _ in range(5)]


def make_grids(
    progression: GameProgression,
) -> tuple[list[list[list[str]]], list[tuple[int, int]]]:
    res: list[list[list[str]]] = []
    labels: list[tuple[int, int]] = []
    grid = empty_grid()
    score = 0

    for grid_idx, (previous_step, step) in enumerate(
        zip(progression[1], progression[1][1:])
    ):
        grid = mark_placements_stale(grid)

        for m, (previous_line, pattern_line) in enumerate(zip(previous_step, step)):
            if pattern_line.color >= 0:
                color = pattern_line.color
                count = pattern_line.count
                place_tile = False
            elif pattern_line.color == -1:
                color_avail = zip(
                    previous_line.potential_colors, pattern_line.potential_colors
                )
                color = next((i for i, (p, c) in enumerate(color_avail) if p != c), -1)
                if color != -1:
                    count = m + 1
                    place_tile = True
                else:
                    color = -1
                    place_tile = False

            left = colored(
                f"{count}/{m + 1}", color=COLORS[(color - m) % 5], bold=place_tile
            )

            # Right 5 columns
            row_cells = [left]
            for n in range(5):
                if n == color and place_tile:
                    cell = colored("X", COLORS[(color - m) % 5], bold=True)
                else:
                    cell = grid[m][n + 1]
                row_cells.append(cell)

            grid[m] = row_cells

        res.append(grid)
        labels.append((grid_idx + 1, grid_idx + 1))  # both labels = grid number

    return res, labels


GRID_WIDTH = 13  # width of each grid (cells + left number column)
GRID_SPACING = 1  # spaces between grids


def print_grids(
    grids: list[list[list[str]]],
    grid_labels: list[tuple[int, int]],  # two numbers per grid
) -> None:
    if not grids:
        return
    print("\n")

    num_rows = len(grids[0])

    # Print the labels above each grid
    label_line = []
    for label in grid_labels:
        label_str = f"{label[0]},{label[1]}"
        # center the label within the fixed grid width
        label_line.append(label_str.center(GRID_WIDTH))
    print((" " * GRID_SPACING).join(label_line))

    # Print dividing line
    print((" " * GRID_SPACING).join(["-" * GRID_WIDTH for _ in grids]))

    # Print each row of the grids
    for row_idx in range(num_rows):
        line_parts = []
        for grid in grids:
            row_str = " ".join(grid[row_idx])
            # pad the row to the fixed width
            line_parts.append(row_str.ljust(GRID_WIDTH))
        print((" " * GRID_SPACING).join(line_parts))
