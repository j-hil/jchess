from cmath import pi
from dataclasses import dataclass
from pieces import Color, Piece, King, Queen, Bishop, Knight, Rook, Pawn
from colorama import Fore, Style, Back

BACK_ROW = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

@dataclass
class Coord:
    x: int | None = None
    y: int | None = None
    # color: str | None = None


class GameState:
    def __init__(self):
        self.pieces: list[Piece] = [
            # TODO: should be enumerates
            *[Piece((7, i), Color.B) for Piece, i in zip(BACK_ROW, range(8))],
            *[Pawn((6, i), Color.B) for i in range(8)],
            *[Pawn((1, i), Color.W) for i in range(8)],
            *[Piece((0, i), Color.W) for Piece, i in zip(BACK_ROW, range(8))],
        ]
        self.cursor: Coord | None = Coord(4, 5)
        self.selected: Coord | None = None

    @property
    def board(self) -> list[list[Piece | None]]:
        result = [[None] * 8 for _ in range(8)]
        for piece in self.pieces:
            x, y = piece.coord
            result[y][x] = piece
        return result

    def valid_selection(self):
        x, y = self.cursor.x, self.cursor.y
        piece: Piece | None = self.board[y][x]
        return piece is not None and piece.accessible_coords(self)

    def valid_move(self):
        # TODO: don't know why explicit typing necessary here
        piece: Piece = self.board[self.selected.y][self.selected.x]
        return (self.cursor.x, self.cursor.y) in piece.accessible_coords(self)


    def __str__(self):
        row_strings = []

        row_strings.append(":      a   b   c   d   e   f   g   h  ")
        row_strings.append(":    +---+---+---+---+---+---+---+---+")

        for i in range(8):

            current_row = ""
            current_row += f":  {i} |"
            for j in range(8):
                piece = self.board[i][j]
                if (j, i) == (self.cursor.x, self.cursor.y):
                    square_color = Back.YELLOW
                elif self.selected is not None and (j, i) == (self.selected.x, self.selected.y):
                    square_color = Back.RED
                elif self.selected is not None and (j, i) in self.board[self.selected.y][self.selected.x].accessible_coords(self):
                    square_color = Back.GREEN
                elif (i+j) % 2 == 0:
                    square_color = Back.MAGENTA
                else:
                    square_color = Back.BLACK
                current_row += (
                    square_color
                    + ("   " if piece is None else f" {piece} ")
                    + Back.RESET
                    + "|"
                )

            current_row += f" {i}"

            row_strings.append(current_row)
            row_strings.append(":    +---+---+---+---+---+---+---+---+")

        row_strings.append(":      a   b   c   d   e   f   g   h  ")
        return "\n".join(row_strings)
