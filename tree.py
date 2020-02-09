class Tree(object):
    def __init__(self, board, move):
        self.children = None  # list of children nodes
        self.board = board  # board state
        self.move = move
        self.a = None  # alpha value
        self.b = None  # beta value
