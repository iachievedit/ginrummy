#!/usr/bin/env python3

from card import Card, Deck
from random import choice, randint

class GinRummy:
  def __init__(self) -> None:
        pass
  
  def winner(self, hand):
      cards_remaining = self.eval(hand)
      return cards_remaining <= 1
  
  def eval(self, hand):
      """
      Evaluates a given hand to determine whether or not it is
      complete.  A complete gin rummy hand is one in which all of 
      its cards are in a set.  A set is three or more cards of
      the same value, or three or more cards are suited and 
      consecutive.  If any card in the hand does not belong to a 
      set, the hand is not complete.
      This function actually returns the number of "non-set" cards,
      so the closer to zero the better.
      """
      
      # First, sort the hand
      sorted_hand = sorted(hand)

      # Group cards by value and check for sets of 3+ of the same value
      i = 0
      while i < len(sorted_hand) - 2:
          if sorted_hand[i].value == sorted_hand[i + 1].value == sorted_hand[i + 2].value:
              sorted_hand = sorted_hand[:i] + sorted_hand[i + 3:]
              continue
          i += 1

      #print("after pass 1", sorted_hand)

      # Sort cards by suit and then by value
      sorted_hand.sort(key=lambda card: (card.suit, card.value_map[card.value]))

      # Check for runs (3+ suited and consecutive cards)
      i = 0
      while i < len(sorted_hand) - 2:
          if (sorted_hand[i].suit == sorted_hand[i + 1].suit == sorted_hand[i + 2].suit and
              Card.value_map[sorted_hand[i].value] == Card.value_map[hand[i + 1].value] - 1 == Card.value_map[sorted_hand[i + 2].value] - 2):
              sorted_hand = sorted_hand[:i] + sorted_hand[i + 3:]
              continue
          i += 1

      #print("after pass 2", sorted_hand)

      return len(sorted_hand)
      

player = 0

deck = Deck()
players = deck.deal(num_players=2, num_cards_per_player=10)

drawn = deck.draw()
if drawn:
  players[player].append(drawn)
else:
    raise

for idx, hand in enumerate(players, 1):
    #print(f"Player {idx-1}'s hand:", hand)
    print(f"Player {idx-1}'s starting hand:", list(map(lambda c: c.uniqid(), hand)))


print("---")

#discards = [[],[]]
#draws = [[],[]]

seen_draw_discard = [[],[]]

seen = None
drawn = None

while True:
  winner = GinRummy().winner(players[player])

  
  if winner:
      print(f"Player {player} WINS")
      exit(0)
  else:
      # Pick a card in the hand to discard
      discard = choice(players[player])
      players[player].remove(discard)
      #discards[player].append(discard)

      if seen != None:
        sdd = [seen.uniqid(), drawn.uniqid(), discard.uniqid()]
      else:
        sdd = [-1, -1, discard.uniqid()]

      seen_draw_discard[player].append(sdd)
      #print(f"Player {player} discards:", random_card.uniqid())
      print(sdd, list(map(lambda c: c.uniqid(), players[player])), GinRummy().eval(players[player]))
  

      player = 1 if player == 0 else 0
      #print(f"Ready Player {player}!")

      # Player 2 can take that card (which it sees) or choose from the deck
      # for now, take card off deck

      # 0 take the chosen card
      seen = discard
      if randint(0, 1) == 0:
          #print("Player takes discard:  ", random_card.uniqid())
          #draws[player].append(discard)
          players[player].append(discard)
          drawn = discard

      else:
        # 1 take off of the deck
        drawn = deck.draw()
        
        if drawn:
            #draws[player].append(drawn)
            players[player].append(drawn)
        else:        
            #print("No more cards")
            for idx, hand in enumerate(players, 1):
              
              #print("Discards:  ", discards[idx-1])
              #print("Draws:  ", draws[idx-1])
              #muxed = [x for pair in zip(discards[idx-1], draws[idx-1]) for x in pair]
              #print(list(map(lambda c: c.uniqid(), muxed)))
              #print(f"Player {idx-1}'s ending hand:", list(map(lambda c: c.uniqid(), hand)))
              print(seen_draw_discard[idx-1])
              #print(GinRummy().eval(hand))
            exit(-1)



