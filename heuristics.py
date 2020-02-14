from board import Board


def evaluate_board(board: Board) -> float:
    line_map = make_line_map(board)
    h = get_heuristics(board, line_map)
    # print(h)
    return h
    # return 0


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
            if board.board[y][x] == board.player:
                stones += 1

    is_won = board.get_outcome()
    if is_won == 1:
        return -(max_moves - stones)

    if is_won == 2:
        return max_moves - stones

    return 0

def make_line_map(board):
    lines = []
    for i in range(board.h):
        for j in range(board.w - board.n + 1):
            lines.append(((i, j),(1, 0)))

    for i in range(board.w):
        for j in range(board.h - board.n + 1):
            lines.append(((j, i),(0, 1)))

    for i in range(board.h - board.n + 1):
        for j in range(board.w - board.n + 1):
            lines.append(((i, j),(1, 1)))

    for i in range(board.h - board.n + 1):
        for j in range((board.w-1), (board.n-2), -1):
            lines.append(((i, j),(-1, -1)))
    return lines
                
def score_line(mine, theirs, n):
    DANGER = 100
    BENEFIT = 100
    # benefit maxxed at n - 1, even bigger benefit if winning line?    
    benefit_factor = BENEFIT / n
    danger_threshold = 0.3
    max_occ = (n - 1) / n # maximum opponent occupation percentage allowed
    occ = theirs / n # actual opponent occupation percentage

    danger, benefit = 0, 0

    if occ >= danger_threshold:
        danger = occ * (DANGER / max_occ)

    if mine >= 1:
        if theirs >= 1:
            benefit = 10
        else:
            benefit = benefit_factor * mine

    return danger, benefit


def get_heuristics(board, line_map):
    danger_total, benefit_total = 0, 0
    for i in line_map:
        y = i[0][0]
        x = i[0][1]
        # counters for playable spots, self pieces, opponent pieces
        playable, mine, theirs = 0, 0, 0
        for _ in range(board.n - 1):
            x += i[1][0]
            y += i[1][1]
            if (y == 0 or y-1 >= 0):
                if board.board[y][x] == 0:
                    playable += 1
            if board.board[y][x] == 1:
                mine += 1
            if board.board[y][x] == 2:
                theirs += 1
        # if playable = 0
        # if mine + their counter = board.n then full line, score
        num_lines = 0
        if 0 < playable < board.n or mine + theirs == board.n:
            num_lines += 1
            line_danger, line_benefit = score_line(mine, theirs, board.n)
            danger_total += line_danger
            benefit_total += line_benefit

            score = (benefit_total / num_lines) - (danger_total / num_lines)
            # score = (benefit_total / num_lines) if danger_total < benefit_total else (danger_total / num_lines)
            # score = (benefit_total / danger_total) if danger_total else 0
            # print(score)
            return score
        else: return 0

'''
Lines with
    only your pieces are good
    only their pieces are bad
    mix of pieces are good but not great
        better the higher the ratio is in your favor
    
    consider the number of winable lines remaining...?
        score would be lessened at lower levels nomatter what...?
'''