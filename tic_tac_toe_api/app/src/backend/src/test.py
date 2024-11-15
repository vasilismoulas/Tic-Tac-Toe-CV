from collections import namedtuple
from copy import deepcopy

# GameState = namedtuple('GameState', 'to_move, utility, board, moves')

# child_state = GameState(to_move = 'd', utility='g', board='b', moves=None)

# #child_state.moves = 'f'

# child_state = child_state._replace(moves = 'f')

# board = {"hey": 1}

# board2 = {"hey2": 2}

# board = board2

# print(board)

# move = (1,2)

# x, y = move

#tuple_test = (0, )

#print(len(tuple_test))

#print("x: ",x,"y: ",y)

def recursive(n):
    print(n)
    return recursive(n)


recursive(3)
