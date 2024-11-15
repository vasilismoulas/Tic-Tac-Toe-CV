import numpy as np
from math import sqrt, log
from collections import namedtuple
from copy import deepcopy
import time


def monte_carlo_player(game, root_state):
    """Given a state in a game, calculate the best move by searching
    forward all the way to the terminal states through four(4) basic steps:
                    #1. Selection, Expansion
                    #2. Simulation
                    #3. Backpropagation
                    #4. Iteration"""

    
    #tree
    root_id = (0, )
    tree = {root_id: {'GameState': None,
                      'child': []
                     }
           }
    C = 1

    total_N = 0

    # extending initial GameSate (note: we better extend our initial namedtuple instead of creating references of class nodes)
    GameState = namedtuple('GameState', root_state._fields + ('v', 'N', 'UCB','Parent'))

    # extending existing point
    state = GameState(*root_state, v=0, N=0, UCB=np.inf, Parent=None) #root node is relative in this situation and so parent, cause
    
    #UCB formula parameters
    exploration_constant = C = 5

    #current player
    player = game.to_move(state)

    #This the place of where we manage the whole algorithm and return the desired state
    def manage_monte_carlo(root_state):
      tree[root_id]['GameState'] = root_state

      simulations = 0

      actions = []
      
      while simulations < 10000:
      
         selected_leaf_node = selection()
         expanded_sleaf_node = expansion(selected_leaf_node)
         winner = simulation(expanded_sleaf_node)
         #print('winner', winner, 'expanded node: ', expanded_sleaf_node)
         backpropagation(expanded_sleaf_node, winner)
         simulations += 1
     
      # SELECT BEST ACTION
      current_state_node_id = (0,)
      action_candidates = tree[current_state_node_id]['child']
      best_ucb = -100
      for a in action_candidates:
            UCB = tree[(0,)+(a,)]['GameState'].UCB
            if UCB > best_ucb:
                best_ucb = UCB
                best_action = a
      
      #print(maximise_UCB_state)
      #print_tree()
      actions = game.actions(state)
      best_action = actions[best_action]
      print(best_action)
      return best_action #return desired state
      
      
    def print_tree():
      """Print tree's states stats"""
      #print("Root Node:")
      #print(tree[root_id]['GameState'])
  
      for child in tree[root_id]['child']:
         print(tree[child]['GameState'])
      # Print child nodes recursively
      #print_child_nodes(root_id, depth=1)

    def print_child_nodes(node_id, depth):
      """Recursively print child nodes."""
      if not tree[node_id]['child']:
         return

      for child_id in tree[node_id]['child']:
         print("\t" * depth + "Child Node:")
         print("\t" * depth + str(tree[child_id]['GameState']))
         print_child_nodes(child_id, depth + 1)

    def selection(): 
      nonlocal total_N
      leaf_node_found = False
      leaf_node_id = (0, )


      while not leaf_node_found:
         node_id = leaf_node_id
         n_child = len(tree[node_id]['child'])

         if n_child == 0:
            leaf_node_id = node_id
            leaf_node_found = True
         else:
            maximum_uct_value = -100.0
            for i in range(n_child):
                  #child_node_id
                  action = tree[node_id]['child'][i]

                  # print('leaf_node_id', leaf_node_id)
                  child_id = node_id + (action,)
                  v = tree[child_id]['GameState'].v
                  N = tree[child_id]['GameState'].N
                  total_N = total_N
                  # parent_id = self.tree[node_id]['parent']
                  # if parent_id == None:
                  #     total_n = 1
                  # else:
                  #     total_n = self.tree[parent_id]['n']

                  if N == 0:
                     N = 1e-4
                  exploitation_value = v / N
                  exploration_value  = np.sqrt(np.log(total_N)/N)
                  uct_value = exploitation_value + C * exploration_value

                  if uct_value > maximum_uct_value:
                     maximum_uct_value = uct_value
                     leaf_node_id = child_id

      depth = len(leaf_node_id) # as node_id records selected action set
      # print('leaf node found: ', leaf_node_found)
      # print('n_child: ', n_child)
      # print('selected leaf node: ')
      # print(self.tree[leaf_node_id])
      return leaf_node_id


    def expansion(leaf_node_id):
      nonlocal total_N
      leaf_state = tree[leaf_node_id]['GameState']
      winner = _is_terminal(leaf_state)
      possible_actions = game.actions(leaf_state)

      child_node_id = leaf_node_id # default value
      if winner is None:
         '''
         when leaf state is not terminal state
         '''
         childs = []
         for action_id, action in enumerate(possible_actions):
               state = deepcopy(tree[leaf_node_id]['GameState'])
               current_player = tree[leaf_node_id]['GameState'].to_move

               child_id = leaf_node_id + (action_id, )
               childs.append(child_id)
               tree[child_id] = {'GameState': GameState(*game.result(state, action),v=0, N=0, UCB=np.inf, Parent=leaf_node_id),
                                 #'player': next_turn,
                                 'child': []}
                                 #'Parent': leaf_node_id,
                                 #'N': 0, 'v': 0, 'UCB':0}
               tree[leaf_node_id]['child'].append(action_id) #WHY???????
         rand_idx = np.random.randint(low=0, high=len(childs), size=1)
         # print(rand_idx)
         # print('childs: ', childs)
         child_node_id = childs[rand_idx[0]]
         #print('expansion: ',child_node_id )
         #print('expansion: ',childs )
      return child_node_id


    def simulation(child_node_id):
        '''
        simulate game from child node's state until it reaches the resulting state of the game.
        in:
        - child node id (randomly selected child node id from `expansion`)
        out:
        - winner ('o', 'x', 'draw')
        '''
        nonlocal total_N
        total_N = total_N + 1
        state = deepcopy(tree[child_node_id]['GameState'])
        previous_player = tree[child_node_id]['GameState'].to_move
        anybody_win = False

        while not anybody_win:
            winner = _is_terminal(state)
            if winner is not None:
                # print('state')
                # print(state)
                # import matplotlib.pyplot as plt
                # plt.figure(figsize=(4.5,4.56))
                # plt.pcolormesh(state, alpha=0.6, cmap='RdBu_r')
                # plt.grid()
                # plt.axis('equal')
                # plt.gca().invert_yaxis()
                # plt.colorbar()
                # plt.title('winner = ' + winner + ' (o:1, x:-1)')
                # plt.show()
                winner = state.utility
                anybody_win = True
            else:
                possible_actions = game.actions(state)
                # randomly choose action for simulation (= random rollout policy)
                rand_id = np.random.randint(low=0, high=len(possible_actions), size=1)[0]
                action = possible_actions[rand_id]

                if previous_player == 'O':
                    current_player = 'X'
                    state = GameState(*game.result(state, action),v=0, N=0, UCB=np.inf, Parent=child_node_id)
                    #state[action] = -1
                else:
                    current_player = 'O'
                    state = GameState(*game.result(state, action),v=0, N=0, UCB=np.inf, Parent=child_node_id)
                    #state[action] = 1

                previous_player = current_player
        return winner


    def backpropagation(child_node_id, winner):
        nonlocal total_N
        player = deepcopy(tree[(0,)]['GameState'].to_move)

        if winner == 0: #DRAW
            reward = 0
        elif winner == -1: #O
            reward = 1
        else: #X
            reward = -1

        finish_backprob = False
        node_id = child_node_id
        while not finish_backprob:
            tree[node_id]['GameState'] = tree[node_id]['GameState']._replace(N = tree[node_id]['GameState'].N + 1) 
            #print('N = ',tree[node_id]['GameState'].N)
            tree[node_id]['GameState'] = tree[node_id]['GameState']._replace(v = tree[node_id]['GameState'].v + reward)
            tree[node_id]['GameState'] = tree[node_id]['GameState']._replace(UCB = tree[node_id]['GameState'].v / tree[node_id]['GameState'].N) 
            parent_id = tree[node_id]['GameState'].Parent
            if parent_id == (0,):
                #print('parent_id: ',parent_id)
                tree[parent_id]['GameState'] = tree[parent_id]['GameState']._replace(N = tree[parent_id]['GameState'].N + 1) 
                tree[parent_id]['GameState'] = tree[parent_id]['GameState']._replace(v = tree[parent_id]['GameState'].v + reward)
                tree[parent_id]['GameState'] = tree[parent_id]['GameState']._replace(UCB = tree[parent_id]['GameState'].v / tree[parent_id]['GameState'].N)
                finish_backprob = True
            else:
                #print(node_id)
                node_id = parent_id
                #print(node_id)

    def UCB_calculation(state):
        """
        calculate UCB value for each MCST node
        formula: UCB = vi/Ni + √(log(N(Parent(n)))/Ni)
        """ 
        #For root_id that has no parent
        if state.Parent is not None and state.Parent in tree:
         parent_node = tree[state.Parent]

         if state.N == 0:
           UCB = np.inf

         elif parent_node['GameState'].N == 0:
           UCB = state.v/state.N

         else:
           UCB = state.v/state.N + sqrt(log(parent_node['GameState'].N+1)/state.N)*C

        else:
           return state.v/state.N

        return UCB 
        

    def _tree_look_up(leaf_node_id):
       """check if node is contained in tree"""
       if leaf_node_id in tree:
          return True
       else:
          return False 
       
    
    def _is_terminal(leaf_state):
        """check if state is terminal """    
        if(game.terminal_test(leaf_state)):
           return leaf_state.utility
        else:
          return None 
    
    def _is_expanded(leaf_node_id):
       """check if node is already expanded"""
       if len(tree[leaf_node_id]['child']) == 0:
           return False
       else:
           return True



    return manage_monte_carlo(state)

  
       
