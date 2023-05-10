# -*- coding: utf-8 -*-


import random
import numpy as np

MIN_LEN = 3
MOVES = ['R', 'P', 'S']
RESPONSES = {
    'R': 'P',
    'P': 'S',
    'S': 'R'
}


def player(prev_play, opponent_history=[], play_orders={}):
  steps = MIN_LEN

  if prev_play != '':
    opponent_history.append(prev_play)

  #Data insufficient so return a random move
  if len(opponent_history) <= steps:
    return MOVES[random.randint(0,2)]

  #Limit length of opponent history
  if len(opponent_history) > steps + 1:
    opponent_history.pop(0)

  #Increment the last observed plays
  sequence = "".join(opponent_history)
  play_orders[sequence] = play_orders.get(sequence, 0) + 1

  #Make actual predictions
  sequence="".join(opponent_history[-steps:])
  rock=play_orders.get(sequence+"R",0)
  paper=play_orders.get(sequence+"P",0)
  scissors=play_orders.get(sequence+"S",0)
  max_index=np.argmax([rock, paper, scissors])
  prediction=MOVES[max_index]

  return RESPONSES[prediction]
