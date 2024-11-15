import numpy as np

def minmax_player(game, state):
    
    """Given a state in a game, calculate the best move by searching
    forward all the way to the terminal states. [Figure 5.3]"""

    player = game.to_move(state)

    def max_value(state):
        if game.terminal_test(state):
            return game.utility(state, player)

        v = -np.inf
        for action in game.actions(state):
            v = max(v, min_value(game.result(state, action)))
            

        return v

    def min_value(state):
        global cnt
        if game.terminal_test(state):
            return game.utility(state, player)

        v = np.inf
        for action in game.actions(state):
            v = min(v, max_value(game.result(state, action)))

        return v
    
    def min_value_print(state,a):
        result = min_value(game.result(state, a))
        return result

    return max(game.actions(state), key=lambda a: min_value_print(state,a))

