"""Program entry point; run as `python -m jchess`."""

import os

import colorama

from jchess import terminal
from jchess.configs import DEFAULT_CONFIG, VSC_CONFIG
from jchess.state import GameState
from jchess.terminal import Action, get_user_action

# attempt to detect that game is being run inside VS Code
DEV_MODE = os.environ.get("TERM_PROGRAM") == "vscode"


def main() -> None:
    """Entry point to begin game. Game state updated & re-printed with each input."""
    size = os.get_terminal_size()
    try:
        colorama.init()
        terminal.clear()
        terminal.resize(87, 25)
        terminal.reset_cursor()
        terminal.hide_cursor()

        game = GameState(DEFAULT_CONFIG if not DEV_MODE else VSC_CONFIG)
        print(game.ctrlseq)
        game.evolve_state(Action.IGNORE)
        print(game.ctrlseq)

        action = get_user_action()
        while action != Action.QUIT:
            game.evolve_state(action)
            print(game.ctrlseq)
            action = get_user_action()
    finally:
        terminal.clear()
        terminal.show_cursor()
        terminal.resize(*size)


if __name__ == "__main__":
    main()
