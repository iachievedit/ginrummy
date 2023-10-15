import random

class Card:
    suits = ['C', 'D', 'H', 'S']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    value_map = {value: index + 1 for index, value in enumerate(values)}

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __lt__(self, other):
        return self.value_map[self.value] < other.value_map[other.value]
    
    def __repr__(self):
        return f"{self.value} of {self.suit} - {self.uniqid()}"
    
    def uniqid(self):
        suit_index = Card.suits.index(self.suit)
        value_index = Card.values.index(self.value)
        return suit_index * 13 + value_index

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]
        random.shuffle(self.cards)

    def deal(self, num_players, num_cards_per_player):
        hands = [[] for _ in range(num_players)]

        for i in range(num_cards_per_player):
            for j in range(num_players):
                if self.cards:
                    hands[j].append(self.cards.pop())
                else:
                    break

        return hands
    
    def draw(self):
        """
            Draws a card from the deck and adds it to the given player's hand.
            """
        if self.cards:
            return self.cards.pop()
        else:
            return None


