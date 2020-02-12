import agent
import heuristics
from node import Node, alpha_beta


###########################
# Alpha-Beta Search Agent #
###########################

class AlphaBetaAgent(agent.Agent):
    """Agent that uses alpha-beta search"""

    # Class constructor.
    #
    # PARAM [string] name:      the name of this player
    # PARAM [int]    max_depth: the maximum search depth
    def __init__(self, name, max_depth):
        super().__init__(name)
        # Max search depth
        self.max_depth = max_depth

    # Builds the tree representing possible moves to x level
    #
    # PARAM [Board] board: the board at the root node from which to build tree
    # PARAM [int]   level: the level to which to build the tree
    #   (1 level is 1 player's move)
    def build_tree(self, node, level):

        # TODO: See if it more efficient to give no children
        # and stop making tree for node that is an end state
        #   (would involve checking each board, may add lots of time)
        # or just give winning states very high heuristics
        # so they are always chosen regardless of children states

        if level == 0:
            return node

        if node.board.get_outcome() != 0:
            return node

        children = self.get_successors(node.board)
        for i, c in enumerate(children):
            children[i] = Node(c[0], c[1])

        for i in range(len(children)):
            self.build_tree(children[i], level - 1)

        node.children = children
        return node

    # Pick a column.
    #
    # PARAM [board.Board] brd: the current board state
    # RETURN [int]: the column where the token must be added
    #
    # NOTE: make sure the column is legal, or you'll lose the game.
    def go(self, brd):
        """Search for the best move (choice of column for the token)"""
        # Your code here

        # get successors down to x level
        # at level x, calculate the evaluation of that state
        #   initial eval func can be 1 if win, -1 if lose, 0 if 
        #   neither for testing purposes
        # alpha-beta search the completed tree

        # Create the initial tree down to some level

        root = Node(brd, None)
        self.build_tree(root, 5)

        move = alpha_beta(root)

        print(heuristics.line_map(brd))
        return move

        # return score[1]

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
