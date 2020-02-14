import agent
from node import Node
import heuristics


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

    # Expands the tree representing possible moves to max_depth
    #
    # PARAM [Node] node: the board at the root node from which to build tree
    # PARAM [int]   level: the level to which to build the tree
    def expand_tree(self, node: Node, level: int = None):
        if level is None:
            level = self.max_depth

        if level == 0:
            return

        if node.board.get_outcome() != 0:
            return

        for board, move in self.get_successors(node.board):
            node.children.append(Node(board, move))

        for child in node.children:
            self.expand_tree(child, level - 1)

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

        # TODO: always move in middle if all moves equak
        #       always move into line of n - 1, no search necessary
        for i in root.children:
            print(i.move, i.value)
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


THE_AGENT = AlphaBetaAgent("Group17", 5)
