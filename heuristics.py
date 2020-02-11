import itertools

from board import Board


def line(x, y, dx, dy, length=4):
    """Generator for a line starting at (x,y) in direction (dx,dy)."""
    count = length
    for i, j in zip(itertools.count(x, dx), itertools.count(y, dy)):
        if count == 0:
            return i, j
        else:
            yield i, j
        count -= 1


row = [2, 1, 0, 0]
ours = 0
theirs = 0
n = 4

danger_factor = 100
good_factor = 100

for i, j in line(0, 0, 1, 0):
    if row[i] == 1:
        ours += 1
    if row[i] == 2:
        theirs += 1

danger = theirs / n * (danger_factor / ((n - 1) / n))
good = ours * ours * (good_factor / ((n - 1) / n))

print(f"{danger}\t{good}")


def evaluate_board(board: Board) -> float:
    for x in board.w:
        for y in board.h:
            board.is_any_line_at(x, y)

