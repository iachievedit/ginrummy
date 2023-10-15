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

Currently the script plays a game with itself:

I need to have different output modes - the intent of this one is to eventually feed into a learning algorithm.  Each card has a value of
0 to 51.  -1 means "no card" and is useful when building the 'move' of hand.

* ♣️ - 0-12 for A through K
* ♦️- 13-25 
* ♥️ - 26-38
* ♠️ - 39-51

In this example - player 0 starts off with eleven cards, and the array [-1, -1, 1] means "I haven't seen a card, I haven't drawn a card, and I've discarded the 2 of clubs."  The resulting hand is 
then displayed.

Player 1 then 'says' "I have seen the 2 of clubs, I drew the 6 of clubs, and discarded the 2 of hearts"

```
 ./ginrummy.py
Player 0's starting hand: [2, 1, 44, 21, 26, 17, 50, 51, 41, 32, 14]
Player 1's starting hand: [33, 0, 42, 27, 13, 9, 10, 43, 39, 6]
---
Player 0 [-1, -1, 1] [2, 44, 21, 26, 17, 50, 51, 41, 32, 14] 10
Player 1 [1, 5, 27] [33, 0, 42, 13, 9, 10, 43, 39, 6, 5] 7
Player 0 [27, 7, 41] [2, 44, 21, 26, 17, 50, 51, 32, 14, 7] 10
Player 1 [41, 41, 5] [33, 0, 42, 13, 9, 10, 43, 39, 6, 41] 7
```

The scoring function for each hand is based upon the number of cards
that cannot be put in a set.  10 is the worst possible, meaning no card is in a set.  0 is the best possible, meaning all cards are in a hand (and you've won).

## Running the play.py script

This is a work in progress, but the play.py scripts goal will be to
generate human-readable output, as well as a file that contains
vectors for the "before hand", the action, the "after hand", and the
score.  


```
./play.py 
...
5♥️ ,6♥️ ,9♥️ ,10♥️ ,J♥️ ,Q♥️ ,7♥️ ,7♠️ ,8♣️ ,8♦️ ,A♠️   J♦️ ,J♥️ ,A♠️   5♥️ ,6♥️ ,9♥️ ,10♥️ ,J♥️ ,Q♥️ ,7♥️ ,7♠️ ,8♣️ ,8♦️   3
3♥️ ,3♣️ ,4♠️ ,4♣️ ,2♠️ ,Q♦️ ,10♠️ ,6♦️ ,9♦️ ,8♠️ ,K♣️   A♠️ ,K♣️ ,8♠️   3♥️ ,3♣️ ,4♠️ ,4♣️ ,2♠️ ,Q♦️ ,10♠️ ,6♦️ ,9♦️ ,K♣️   10
Testing  7♥️
Testing  Q♥️
Testing  6♥️
Testing  8♣️
Testing  10♥️
Testing  7♠️
Discarded  7♠️
[32, 37, 31, 7, 35, 45, 34, 20, 30, 36, 46] , [-1, -1, 45] , [32, 37, 31, 7, 35, 34, 20, 30, 36, 46] , 0
Inner script returned 0. Stopping!
```

# ChatGPT

This project is another exercise is using ChatGPT to help fill in the blanks or generate code for the mundane (score the hand, pretty print things, etc.)