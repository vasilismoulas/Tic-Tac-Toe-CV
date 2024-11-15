import numpy as np


def minmax_a_b_player(game, state):
    """Given a state in a game, calculate the best move by searching
    forward all the way to the terminal states while possibly excluding 
    some branches in the process that we will choose that are trivial"""

    player = game.to_move(state)

    def max_value(state,alpha,beta):
        if game.terminal_test(state):
            return game.utility(state, player)

        v = -np.inf
        for action in game.actions(state):
            v = max(v, min_value(game.result(state, action),alpha,beta))
            if(v>=beta):
              return v
            alpha = max(alpha,v)

        return v

    def min_value(state,alpha,beta):
        if game.terminal_test(state):
            return game.utility(state, player)

        v = np.inf
        for action in game.actions(state):
            v = min(v, max_value(game.result(state, action),alpha,beta))
            if(v<=alpha):
               return v
            beta = min(beta,v)

        return v
     
   
    return max(game.actions(state), key=lambda a: min_value(game.result(state, a),-np.inf,np.inf))