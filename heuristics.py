from board import Board


def evaluate_board(board: Board) -> float:
    return win_loss_evaluate(board)


def win_loss_evaluate(board: Board) -> float:
    if board.get_outcome() == 1:
        return -1
    if board.get_outcome() == 2:
        return 1
    return 0


def line_map(board):
    lines = []
    for i in range(board.h):
        for j in range(board.w - board.n + 1):
            lines.append(((i, j),(1, 0)))

    for i in range(board.w):
        for j in range(board.h - board.n + 1):
            lines.append(((i, j),(0, 1)))

    for i in range(board.h - board.n + 1):
        for j in range(board.w - board.n + 1):
            lines.append(((i, j),(1, 1)))

    for i in range(board.h - board.n + 1):
        for j in range((board.w-1), (board.n-1)):
            lines.append(((i, j),(-1, -1)))
    return lines
