import time
import agent
from node import Node


###########################
# Alpha-Beta Search Agent #
###########################

class AlphaBetaAgent(agent.Agent):
    """Agent that uses alpha-beta search"""

    # Class constructor.
    #
    # PARAM [string] name:      the name of this player
    # PARAM [int]    min_depth: the minimum depth of the tree (ignores time limit)
    # PARAM [int]    expand_time: the number of seconds to spend expanding the tree
    def __init__(self, name: str, min_depth: int, expand_time: int):
        super().__init__(name)
        self.min_depth = min_depth
        self.expand_time = expand_time

    # Expands the tree representing possible moves until the stop_time
    #
    # PARAM [Node]  node: the board at the root node from which to build tree
    # PARAM [int]   level: the current depth of the tree
    # PARAM [float] start_time: the time we started building the tree
    def expand_tree(self, node: Node, level: int = 0, start_time: float = time.time()):
        if node.board.get_outcome() != 0:
            return

        if level >= self.min_depth and time.time() > start_time + self.expand_time:
            return

        for board, move in self.get_successors(node.board):
            node.children.append(Node(board, move))

        for child in node.children:
            self.expand_tree(child, level + 1, start_time)

    # Pick a column.
    #
    # PARAM [board.Board] brd: the current board state
    # RETURN [int]: the column where the token must be added
    #
    # NOTE: make sure the column is legal, or you'll lose the game.
    def go(self, brd):
        """Search for the best move (choice of column for the token)"""

        # Create a new root node from the current board state
        root = Node(brd, None)
        # Expand out tree
        self.expand_tree(root)
        # Run minmax alpha beta search for the next best move
        move = root.alpha_beta_search()
        # Print the tree for debugging
        # print(root)
        # Return the move
        return move

    # Get the successors of the given board.
    #
    # PARAM [board.Board] brd: the board state
    # RETURN [list of (board.Board, int)]: a list of the successor boards,
    #                                      along with the column where the last
    #                                      token was added in it
    def get_successors(self, brd):
        """Returns the reachable boards from the given board brd. The return value is a tuple (new board state, column number where last token was added)."""
        # Get possible actions
        freecols = brd.free_cols()
        # Are there legal actions left?
        if not freecols:
            return []
        # Make a list of the new boards along with the corresponding actions
        succ = []
        for col in freecols:
            # Clone the original board
            nb = brd.copy()
            # Add a token to the new board
            # (This internally changes nb.player, check the method definition!)
            nb.add_token(col)
            # Add board to list of successors
            succ.append((nb, col))
        return succ
