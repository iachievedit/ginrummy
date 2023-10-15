# The Game

Gin Rummy has been a favorite game of mine since I was seven years old.  I remember when my grandparents taught me how to play as I was fascinated when they played bridge and were able to hold more than five or so cards in their hand at once!

The version I was taught is simple, and its the one I play to this day:

* There are 2 players, dealer and non-dealer
* The dealer deals each player ten cards, and then to the non-dealer an eleventh card
* The non-dealer plays first by discarding
* To win your hand must be "complete" in that every card (except the discard) must be a part of a set
* A set is a minimum of 3 cards, and can be cards of the same value, or consecutive suited cards

Several examples of sets:

* 3♥️ 3♠️ 3♣️
* 9♥️ 9♦️ 9♣️
* 10♣️ J♣️ Q♣️
* 7♥️ 8♥️ 9 ♥️
* A ♠️2♠️ 3♠️4♠️

When all of the cards in your hand, except the discard, are part of a set, your discard is face down signaling you've won.

# The Goal

I'd like to create an artificial intelligence bot that plays optimal gin rummy.  The "reward function" (at least in my mind at the moment) is simple:  your hand wins or doesn't.  

The mechanics of the game are also easy:  choose to pick up a known card from the discard pile (where it is straightforward to see whether or not it improves your hand), or draw a card from the deck (which cannot be seen).