# -*- coding: utf-8 -*-

#markov style solution based on the total number of observed sequences of plays from the opponent.
import random
import numpy as np

#tried to set the minimum length to various numbers and 3 seems to be best.
MIN_LEN = 3
#Define possible moves and winning responses
MOVES = ['R', 'P', 'S']
RESPONSES = {
    'R': 'P',
    'P': 'S',
    'S': 'R'
}
#Initialize an empty dictionary so the sequences are correctly remembered outside the function
OBSERVED_PLAYS={}


def player(prev_play, opponent_history=[], play_orders=OBSERVED_PLAYS):
  steps = MIN_LEN

  if prev_play != '':
    opponent_history.append(prev_play)

  #Data insufficient so return a random move
  if len(opponent_history) <= steps:
    return MOVES[random.randint(0,2)]

  #Limit length of opponent history so there are fewer sequences that need to be recorded in the dictionary
  if len(opponent_history) > steps + 1:
    opponent_history.pop(0)

  #Increment the entries in the dictionary or create new entry when there is no preexisting entry
  sequence = "".join(opponent_history)
  play_orders[sequence] = play_orders.get(sequence, 0) + 1

  #Make actual predictions when there is enough data to make predictions with
  sequence="".join(opponent_history[-steps:])
  #Get number of times the specific sequences were observed (the current sequence with the 3 different possible options appended to it)
  rock=play_orders.get(sequence+"R",0)
  paper=play_orders.get(sequence+"P",0)
  scissors=play_orders.get(sequence+"S",0)
  #Find which of them had the most epreviously observed sequences
  max_index=np.argmax([rock, paper, scissors])
  #Make a prediction based on the previously defined index
  prediction=MOVES[max_index]
  #Empty the dictionary once a full game of 1000 matches is finished.
  if len(opponent_history)==1000:
      play_orders={}
        
  #return the winning move based on the prediction
  return RESPONSES[prediction]
