from random import*

def random_player(game, state):
 """A random player."""
 game.display(state)
 actions = game.actions(state)

 while True:
   (x,y) = (randrange(game.h+1),randrange(game.v+1))
   action = (x,y)
   if (action in actions):
      break
   else:
      continue
       
 return action
