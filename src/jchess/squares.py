"""Creates representation of a chess piece."""
from dataclasses import dataclass
from enum import Enum


class Role(Enum):
    """Each type chess piece and a `Null` for empty squares."""

    KING = ("KING", 104)
    QUEEN = ("QUEEN", 9)
    ROOK = ("ROOK", 5)
    BISHOP = ("BISHOP", 3)
    KNIGHT = ("KNIGHT", 3)
    PAWN = ("PAWN", 1)
    NULL = ("NULL", 0)

    @property
    def val(self) -> int:
        """Traditional point worth of each piece."""
        # max score is 103 so KING = 104 gives score > 103 an unambiguous win condition
        return super().value[1]

    def __str__(self) -> str:
        return super().value[0]


class Player(Enum):
    """Which player (if any) that a square or turn belongs to."""

    ONE = "ONE"
    TWO = "TWO"
    NULL = "NULL"


@dataclass
class Square:
    """Representation any square on the board."""

    role: Role
    player: Player


NULL_SQUARE = Square(Role.NULL, Player.NULL)
