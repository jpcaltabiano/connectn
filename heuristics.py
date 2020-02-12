from board import Board


def evaluate_board(board: Board) -> float:
    return moves_to_win_evaluate(board)


def win_loss_evaluate(board: Board) -> float:
    is_won = board.get_outcome()
    if is_won == 1:
        return -1
    if is_won == 2:
        return 1
    return 0


def moves_to_win_evaluate(board: Board) -> float:
    max_moves = board.w * board.h

    stones = 0
    for x in range(board.w):
        for y in range(board.h):
            if board.board[y][x] == 2:
                stones += 1

    is_won = board.get_outcome()
    if is_won == 1:
        return -(max_moves - stones)

    if is_won == 2:
        return max_moves - stones

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
