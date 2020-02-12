import math

from heuristics import evaluate_board


class Node(object):
    def __init__(self, board, move):
        self.children = None  # list of children nodes
        self.board = board  # board state
        self.move = move
        self.value = None

    def is_leaf(self) -> bool:
        return self.children is None


def alpha_beta(node: Node) -> int:
    v = alpha_beta_max(node, -math.inf, math.inf)
    for child in node.children:
        if child.value == v:
            return child.move
    return None


def alpha_beta_max(node: Node, alpha: float, beta: float) -> float:
    if node.is_leaf():
        return evaluate_board(node.board)

    v = -math.inf
    for child in node.children:
        child.value = alpha_beta_min(child, alpha, beta)
        v = max(v, child.value)
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def alpha_beta_min(node: Node, alpha: float, beta: float) -> float:
    if node.is_leaf():
        return evaluate_board(node.board)

    v = math.inf
    for child in node.children:
        child.value = alpha_beta_max(child, alpha, beta)
        v = max(v, child.value)
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v
