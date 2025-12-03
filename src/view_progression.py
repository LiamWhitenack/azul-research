from collections.abc import Callable
from typing import Literal

from colorama import Fore, Style, init

from src.score import score_placement
from src.types import GameProgression, WallType
from src.wall import empty_wall

init(autoreset=True)

COLORS = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.WHITE]


def colored(text: str, color_idx: int, bold: bool = False) -> str:
    if bold:
        return Style.BRIGHT + COLORS[color_idx] + text + Style.RESET_ALL
    return COLORS[color_idx] + text + Style.RESET_ALL


MARKDOWN_COLOR_CLASSES = ["red", "green", "blue", "orange", "purple", "black"]


def md_color(text: str, color_idx: int, bold: bool = False) -> str:
    color_class = MARKDOWN_COLOR_CLASSES[color_idx % len(MARKDOWN_COLOR_CLASSES)]
    if bold:
        return f'<span class="{color_class}" style="font-weight:bold;">{text}</span>'
    return f'<span class="{color_class}">{text}</span>'


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
    style_function: Callable[[str, int, bool], str] = colored,
) -> tuple[list[list[list[str]]], list[str]]:
    res: list[list[list[str]]] = []
    labels: list[str] = []
    grid = empty_grid()
    wall: WallType = empty_wall()
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

            left = style_function(f"{count}/{m + 1}", (color - m) % 5, place_tile)

            # Right 5 columns
            row_cells = [left]
            for n in range(5):
                if n == color and place_tile:
                    cell = style_function("X", (color - m) % 5, True)
                    score += score_placement(wall, m, n)
                    wall[m, n] = True  # update wall
                else:
                    cell = grid[m][n + 1]

                row_cells.append(cell)

            grid[m] = row_cells

        res.append(grid)
        labels.append(str(score))

    return res, labels


GRID_WIDTH = 13  # width of each grid (cells + left number column)
GRID_SPACING = 1  # spaces between grids


def styled_grid_progression(
    progression: GameProgression, style: Literal["print", "markdown"] = "print"
) -> str:
    use_markdown = style == "markdown"
    grids, labels = make_grids(progression, colored if not use_markdown else md_color)

    if not grids:
        return ""

    num_rows = len(grids[0])
    out: list[str] = []

    if not use_markdown:
        # ───────────────────────────────
        # PRINT MODE (unchanged)
        # ───────────────────────────────
        label_line = []
        for label in labels:
            label_line.append(label.center(GRID_WIDTH))
        out.append((" " * GRID_SPACING).join(label_line))
        out.append((" " * GRID_SPACING).join(["-" * GRID_WIDTH for _ in grids]))

        for row_idx in range(num_rows):
            parts = []
            for grid in grids:
                row_str = " ".join(grid[row_idx])
                parts.append(row_str.ljust(GRID_WIDTH))
            out.append((" " * GRID_SPACING).join(parts))
        return "\n".join(out)

    # ───────────────────────────────
    # MARKDOWN MODE (table output with CSS classes)
    # ───────────────────────────────
    # Add CSS style block at the top of output
    # Also update the CSS block to include new colors
    out.append(
        "---\n"
        "marp: true\n"
        "theme: custom\n"
        "---\n"
        "<style>\n"
        ".red { color: red; }\n"
        ".green { color: green; }\n"
        ".blue { color: blue; }\n"
        ".orange { color: orange; }\n"
        ".purple { color: purple; }\n"
        ".black { color: black; }\n"
        "td { width: 80px; text-align: center; }\n"
        "</style>\n",
    )

    for grid_idx, grid in enumerate(grids):
        label = labels[grid_idx]

        out.append(f"### Step {grid_idx + 1} — Score: **{label}**\n")

        # # header row (dummy, for alignment)
        out.append("|  |  |  |  |  |  |")
        out.append("|------|------|------|------|------|------|")

        for r in range(num_rows):
            # each cell uses span class and fixed width
            row_cells = [
                grid[r][c].replace("\n", "<br>") if grid[r][c].strip() else "&nbsp;"
                for c in range(len(grid[r]))
            ]
            out.append("| " + " | ".join(row_cells) + " |")

        out.append("")  # spacing after table
        out.append("---\n")  # Marp slide separator

    return "\n".join(out)
