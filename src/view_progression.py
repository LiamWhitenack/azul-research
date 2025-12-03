from colorama import Fore, Style, init

init(autoreset=True)

COLORS = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA]


def colored(text: str, color: str, bold: bool = False) -> str:
    if bold:
        return Style.BRIGHT + color + text + Style.RESET_ALL
    return color + text + Style.RESET_ALL


# ---------------------------------------------------------
# 1) Create a single 5×6 grid for a given step
# ---------------------------------------------------------
def make_grid(step: int):
    """
    Returns a 5×6 grid (list of list of strings).
    Column 0 displays f"{step}/{row}" in bold with row-based color.
    Columns 1–5 form the 5×5 square block with dynamic colored X's.
    """
    grid = []

    for row in range(5):
        # Left column (index 0)
        color = COLORS[row % len(COLORS)]
        left = colored(f"{step}/{row}", color, bold=True)

        # Right 5 columns
        row_cells = [left]
        for col in range(5):
            # Example progression: fill X only in top-left k×k
            if col <= step - 1 and row <= step - 1:
                is_bold = (step + row + col) % 2 == 0
                cell_color = COLORS[(row + col) % len(COLORS)]
                cell = colored("X", cell_color, bold=is_bold)
            else:
                cell = " "
            row_cells.append(cell)

        grid.append(row_cells)

    return grid


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
