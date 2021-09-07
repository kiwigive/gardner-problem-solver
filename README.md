# gardner-problem-solver
This program is part of my Bachelor Degree's project, "An Extension Of Martin Gardner's Card Trick". It can tell whether a Gardner’s problem (a.k.a. the 27-card-trick) with given parameters is solvable or unsolvable. Moreover, for a solvable problem, the program can show all possible ways to perform the Gardner’s trick. In past, they already revealed a solution for the deck of size n<sup>k</sup> cards or even the size of a deck of composite number by using mixed radix sort method (dealing the deck into factors of the number of cards in the deck) by Bolker. However, it is interesting to find the deck with the size other than n^k cards, that can deal cards into fixed number of piles.

### Abstract
Performing the 27-card Gardner’s trick depends on base three arithmetic.
                    First, we subtract the desired position chosen from the spectator by 1 and
                    convert that resulting number into a three digit number in base 3. We will
                    call this base-3 number a “code”. Next, we decode each digit in the code starting
                    from right to left to perform the Gardner’s trick in each round by placing the
                    indicated pile (from the spectator) in the interpreted position. If the digit is 0,
                    the chosen pile goes on top (none above it); if it is 1, the chosen pile goes at the
                    middle (one stack above it); if it is 2, the chosen pile goes at the bottom (two stacks above it).
                    Performing the trick according to this strategy will finally bring the chosen card to the desired position.
                    This table shows all corresponding pairs of desired positions and codes for performing.

### Martin Gardner's Card Trick
In Mathematics, Magic and Mystery, Martin Gardner evolved Gergonne 3-pile problem to the 27-card trick. Playing the trick, let a spectator selects any card in a deck of 27 cards, memorizes it and shuffles the deck as much as desired. The spactator will choose the position 1-27 of the deck. The magician create three face-up piles of nine cards by dealing the top cards respectively onto the left, middle, then right pile and repeating until all the cards are gone. Now, he gets 3 piles of cards. Next, the participant points to which pile contains the chosen card. After that, the magician gather all those piles and put the chosen pile to the specific order. The problem involves distributing these cards with 3 piles and 3 times assembly. Finally, the magician can make the desire position be the chosen card.

### Using the program
-- Each of parameters should be a positive integer --

Definition For a Gardner’s problem, we define parameters M, N, K as follows:
  M is the number of dealing piles in each round,
  N is the number of cards in each dealing pile, and
  K is the number of dealing rounds.

In ======= success ======= section, it will appear usable codes.
In the same way, ======== fail ======== will show unusable codes.
The meaning of number inside the code are (The least possible position of the tracking card after performing K rounds, the greatest possible position of the tracking card after performing K rounds, ( number of piles above the chosen pile in the fisrt round, number of piles above the chosen pile in the second round, ...., number of piles above the chosen pile in the final round (K) ),
eg., (1, 1, (0, 0, 0)) will be in a success section because. The least and the gretest possible position are the same. The code of performing is (0,0,0).

After computed, the program will reveal that is the given parameter solvable or not. All results will appear in a result table.
