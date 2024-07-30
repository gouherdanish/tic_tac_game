from enum import Enum

class WinningCombos(Enum):
    HORZ1 = '1,2,3'
    HORZ2 = '4,5,6'
    HORZ3 = '7,8,9'
    VERT1 = '1,4,7'
    VERT2 = '2,5,8'
    VERT3 = '3,6,9'
    DIAG1 = '1,5,9'
    DIAG2 = '3,5,7'