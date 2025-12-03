from colorama import Fore, Style, init

from src.types import GameProgression, WallType

init(autoreset=True)

COLORS = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.WHITE]


def colored(text: str, color: str, bold: bool = False) -> str:
    if bold:
        return Style.BRIGHT + color + text + Style.RESET_ALL
    return color + text + Style.RESET_ALL


def unbold_grid(grid: list[list[str]]) -> list[list[str]]:
    bold_code = Style.BRIGHT

    new_grid = []
    for row in grid.copy():
        new_row = []
        for cell in row:
            if isinstance(cell, str):
                new_row.append(cell.replace(bold_code, ""))
            else:
                new_row.append(cell)
        new_grid.append(new_row)

    return new_grid


def empty_grid() -> list[list[str]]:
    return [[" " for _ in range(6)] for _ in range(5)]


def make_grids(progression: GameProgression) -> list[list[list[str]]]:
    res: list[list[list[str]]] = []
    grid = empty_grid()

    for previous_step, step in zip(progression[1], progression[1][1:]):
        grid = unbold_grid(grid)

        for m, (previous_line, pattern_line) in enumerate(zip(previous_step, step)):
            if pattern_line.color >= 0:
                color = pattern_line.color
                count = pattern_line.count
                place_tile = False
            if pattern_line.color == -1:
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

            left = colored(f"{count}/{m + 1}", color=COLORS[color], bold=True)

            # Right 5 columns
            row_cells = [left]
            for n in range(5):
                if n == color and place_tile:
                    cell = colored("X", COLORS[color], bold=True)
                else:
                    cell = grid[m][n + 1]
                row_cells.append(cell)

            # Replace row in-place instead of growing the grid
            grid[m] = row_cells

        # Save a copy of the grid for this step
        res.append(grid)

    return res


# ---------------------------------------------------------
# 2) Print multiple grids either horizontally or vertically
# ---------------------------------------------------------
def print_grids(grids, orientation="horizontal"):
    """
    grids: list of 5×6 grids
    orientation: "horizontal" → side-by-side
                 "vertical"   → one below the other
    """
    if orientation == "vertical":
        for g in grids:
            for row in g:
                print(" ".join(row))
            print()  # blank line between grids
        return

    # ---------- Horizontal printing ----------
    # side-by-side: concatenate row i from each grid
    num_rows = len(grids[0])

    for row_idx in range(num_rows):
        line_parts = []
        for grid in grids:
            line_parts.append(" ".join(grid[row_idx]))
        print("     ".join(line_parts))  # spacing between grids
