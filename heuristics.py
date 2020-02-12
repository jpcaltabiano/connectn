from board import Board


def evaluate_board(board: Board) -> float:
    return win_loss_evaluate(board)


def win_loss_evaluate(board: Board) -> float:
    if board.get_outcome() == 1:
        return -1
    if board.get_outcome() == 2:
        return 1
    return 0
