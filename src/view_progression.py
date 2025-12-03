from colorama import Fore, Style, init

init(autoreset=True)

COLORS = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA]


def colored(text: str, color: str, bold: bool = False) -> str:
    if bold:
        return Style.BRIGHT + color + text + Style.RESET_ALL
    return color + text + Style.RESET_ALL


def view_progression(steps: int = 5):
    """
    Display progression of a 5x6 grid over `steps` steps.
    The left column shows bold colored f"{x}/{m}".
    The right 5 columns form a 5x5 square with colored X's or blanks.
    """
    for step in range(1, steps + 1):
        print(f"\n=== STEP {step} ===")
        for row in range(5):
            # --- LEFT COLUMN: f"x/m" ---
            color = COLORS[row % len(COLORS)]
            left = colored(f"{step}/{row}", color, bold=True)

            # --- RIGHT 5×5 block ---
            row_cells = []
            for col in range(5):
                # example rule:
                # fill X up to the diagonal based on the step
                if col <= step - 1 and row <= step - 1:
                    is_bold = (row + col + step) % 2 == 0
                    cell_color = COLORS[(row + col) % len(COLORS)]
                    cell = colored("X", cell_color, bold=is_bold)
                else:
                    cell = " "

                row_cells.append(cell)

            print(left, *row_cells)
