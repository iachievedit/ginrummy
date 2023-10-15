#!/usr/bin/env python3
import argparse
import copy
from card import Card, Deck
from random import choice, randint

class GinRummy:
  def __init__(self) -> None:
        pass
  
  def winner(self, hand):
      cards_remaining = self.eval(hand)
      return cards_remaining <= 1
    
  def eval(self, hand):
    def find_sequences(cards):
        # This function finds all possible sequences in the given cards.
        sequences = []
        if len(cards) < 3:
            return sequences

        sorted_cards = sorted(cards)
        for i in range(len(sorted_cards) - 2):
            sequence = [sorted_cards[i]]
            for j in range(i + 1, len(sorted_cards)):
                if sorted_cards[j].suit == sequence[-1].suit and Card.value_map[sorted_cards[j].value] - Card.value_map[sequence[-1].value] == 1:
                    sequence.append(sorted_cards[j])
                    if len(sequence) >= 3:
                        sequences.append(sequence.copy())

        return sequences

    def find_sets(cards):
        # This function finds all possible sets in the given cards.
        sets = []
        value_counts = {}
        for card in cards:
            value_counts[card.value] = value_counts.get(card.value, 0) + 1

        for value, count in value_counts.items():
            if count >= 3:
                sets.append([card for card in cards if card.value == value][:count])

        return sets

    if not hand:
        return 0

    sequences = find_sequences(hand)
    sets = find_sets(hand)

    # If no sets or sequences are found, return the length of the hand.
    if not sequences and not sets:
        return len(hand)

    scores = []

    # Try sequences first
    for sequence in sequences:
        new_hand = hand.copy()
        for card in sequence:
            new_hand.remove(card)
        scores.append(self.eval(new_hand))

    # Try sets
    for set_found in sets:
        new_hand = hand.copy()
        for card in set_found:
            new_hand.remove(card)
        scores.append(self.eval(new_hand))

    # Return the minimum score from all the possible combinations.
    return min(scores)
  
  def print_hand_structure(self,hand):
    def find_best_pair(cards):
        sorted_cards = sorted(cards)
        # Check for a pair in a sequence first
        for i in range(len(sorted_cards) - 1):
            if sorted_cards[i].suit == sorted_cards[i + 1].suit and \
               Card.value_map[sorted_cards[i + 1].value] - Card.value_map[sorted_cards[i].value] == 1:
                return [sorted_cards[i], sorted_cards[i + 1]]
        # Check for a pair of the same rank
        for i in range(len(sorted_cards) - 1):
            if sorted_cards[i].value == sorted_cards[i + 1].value:
                return [sorted_cards[i], sorted_cards[i + 1]]
        return []
    
    def find_best_sequence(cards):
        sorted_cards = sorted(cards)
        for i in range(len(sorted_cards) - 2):
            sequence = [sorted_cards[i]]
            for j in range(i + 1, len(sorted_cards)):
                if sorted_cards[j].suit == sequence[-1].suit and Card.value_map[sorted_cards[j].value] - Card.value_map[sequence[-1].value] == 1:
                    sequence.append(sorted_cards[j])
                else:
                    break

            if len(sequence) >= 3:
                return sequence
        return []

    def find_best_set(cards):
        value_counts = {}
        for card in cards:
            value_counts[card.value] = value_counts.get(card.value, 0) + 1

        for value, count in value_counts.items():
            if count >= 3:
                return [card for card in cards if card.value == value][:3]
        return []

    pairs = []
    sequences = []
    sets = []
    remaining = hand.copy()

    # Extract best pairs until none are left
    while True:
        pair = find_best_pair(remaining)
        if pair:
            pairs.append(pair)
            for card in pair:
                remaining.remove(card)
        else:
            break

    # Extract best sequences until none are left
    while True:
        sequence = find_best_sequence(remaining)
        if sequence:
            sequences.append(sequence)
            for card in sequence:
                remaining.remove(card)
        else:
            break

    # Extract best sets until none are left
    while True:
        set_found = find_best_set(remaining)
        if set_found:
            sets.append(set_found)
            for card in set_found:
                remaining.remove(card)
        else:
            break

    # Printing
    organized_hand = []

    for pair in pairs:
        organized_hand.extend(pair)

    for sequence in sequences:
        organized_hand.extend(sequence)

    for set_found in sets:
        organized_hand.extend(set_found)

    organized_hand.extend(remaining)
    #print(organized_hand)

    return organized_hand
  
parser = argparse.ArgumentParser()
parser.add_argument('--pretty-print', dest='pretty_print', action='store_true', default=False,
                    help='Pretty print output (default: False)')

args = parser.parse_args()

player = 0

deck = Deck()
players = deck.deal(num_players=2, num_cards_per_player=10)

drawn = deck.draw()
players[0].append(drawn)

#for idx, hand in enumerate(players, 1):
#    #print(f"Player {idx-1}'s hand:", hand)
#    print(f"Player {idx-1}'s starting hand:", list(map(lambda c: c.uniqid(), hand)))


#print("---")

#discards = [[],[]]
#draws = [[],[]]

seen_draw_discard = [[],[]]

seen = None
drawn = None

while True:
  winner = GinRummy().winner(players[player])

  
  if winner:
#      print(f"Player {player} WINS")
#      structure = GinRummy().print_hand_structure(players[player])
#      print(players[player])
#      print(structure)
#      print(list(map(lambda c: c.uniqid(), hand_before)), ",", sdd, ",", list(map(lambda c: c.uniqid(), players[player])), ",", GinRummy().eval(players[player]))
      hand_before = copy.deepcopy(players[player])
      print(hand_before)
      print(list(map(lambda c: c.uniqid(), hand_before)), ",", [-1,-1,-1], ",", list(map(lambda c: c.uniqid(), players[player])), ",", GinRummy().eval(players[player]))

      exit(0)
  else:
      hand_before = copy.deepcopy(players[player])
      # Pick a card in the hand to discard
      discard = choice(players[player])
      players[player].remove(discard)

      if seen != None:
        if args.pretty_print:
          sdd = [seen, drawn, discard]
        else:
          sdd = [seen.uniqid(), drawn.uniqid(), discard.uniqid()]
      else:
        if args.pretty_print:
           sdd = [None, None, discard]
        else:
          sdd = [-1, -1, discard.uniqid()]

      seen_draw_discard[player].append(sdd)
      #print(f"Player {player} discards:", random_card.uniqid())
      if args.pretty_print:
        hand_before = GinRummy().print_hand_structure(hand_before)
        hand_after  = GinRummy().print_hand_structure(players[player])
        print(' ,'.join(map(str, hand_before)), " ", ' ,'.join(map(str, sdd)), " ", ' ,'.join(map(str,hand_after)), " ", GinRummy().eval(players[player]))
      else:
        print(list(map(lambda c: c.uniqid(), hand_before)), ",", sdd, ",", list(map(lambda c: c.uniqid(), players[player])), ",", GinRummy().eval(players[player]))
  

      player = 1 if player == 0 else 0
      #print(f"Ready Player {player}!")

      # Player 2 can take that card (which it sees) or choose from the deck
      # for now, take card off deck

      # 0 take the discard, 1 draw from the deck
      seen = discard
      if randint(0, 1) == 0:
          players[player].append(discard)
          drawn = discard
      else:
        drawn = deck.draw()
        
        if drawn:
            #draws[player].append(drawn)
            players[player].append(drawn)
        else:        
            #print("No more cards")
            for idx, hand in enumerate(players, 1):
              pass
              #print("Discards:  ", discards[idx-1])
              #print("Draws:  ", draws[idx-1])
              #muxed = [x for pair in zip(discards[idx-1], draws[idx-1]) for x in pair]
              #print(list(map(lambda c: c.uniqid(), muxed)))
              #print(f"Player {idx-1}'s ending hand:", list(map(lambda c: c.uniqid(), hand)))
              #print(seen_draw_discard[idx-1])
              #print(GinRummy().eval(hand))
            exit(-1)



