import math


def alpha_beta(node, level: int, is_max: bool, alpha: float, beta: float):
    if node.children is None:
        # Call H on this node
        pass

    if is_max:
        best = -math.inf
        for child in node.children:
            value = alpha_beta(child, level - 1, False, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for child in node.children:
            value = alpha_beta(child, level - 1, True, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
