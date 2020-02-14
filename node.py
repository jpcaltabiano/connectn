import math

from heuristics import evaluate_board


class Node(object):
    def __init__(self, board, move):
        self.children = []  # list of children nodes
        self.board = board  # board state
        self.move = move
        self.value = None

    def is_leaf(self) -> bool:
        return self.children == []

    def alpha_beta_search(self) -> int:
        self.alpha_beta_max(-math.inf, math.inf)

        v = -math.inf
        move = 0
        for child in self.children:
            if child.value > v:
                move = child.move
                v = child.value
        return move

    def alpha_beta_max(self, alpha: float, beta: float) -> None:
        if self.is_leaf():
            self.value = evaluate_board(self.board)

        # self.value = -math.inf
        best_value = -math.inf
        for child in self.children:
            child.alpha_beta_min(alpha, beta)
            self.value = max(best_value, child.value)
            # if self.value >= beta:
            #     return
            alpha = max(alpha, best_value)

    def alpha_beta_min(self, alpha: float, beta: float) -> None:
        if self.is_leaf():
            self.value = evaluate_board(self.board)

        # self.value = math.inf
        best_value = math.inf
        for child in self.children:
            child.alpha_beta_max(alpha, beta)
            self.value = min(best_value, child.value)
            # if self.value <= alpha:
            #     return
            beta = min(beta, best_value)

    def __str__(self, level=0):
        ret = "\t" * level + f"Node({repr(self.board.player)}, {repr(self.move)}, {repr(self.value)})" + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

