import math


def alpha_beta(node, level: int, is_max: bool, alpha: float, beta: float):
    if node.children is None:
        if node.board.get_outcome() == 1:
            node.val = -1
            return (-1, None)
        if node.board.get_outcome() == 2:
            node.val = 1
            return (1, None)
        node.val = node.board.get_outcome()    
        return (node.board.get_outcome(), None)

    if is_max:
        best = -math.inf
        for i, child in enumerate(node.children):
            value, _ = alpha_beta(child, level - 1, False, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)
            choice = (best, i)
            if beta <= alpha:
                break
        return choice
    else:
        best = math.inf
        for i, child in enumerate(node.children):
            value, _ = alpha_beta(child, level - 1, True, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)
            choice = (best, i)
            if beta <= alpha:
                break
        return choice
