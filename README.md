# Single-player Expendibots

The single-player variant of Expendibots we will analyse works as follows. You will always play as White, and
you will be the only player that acts. The Black player is static and does not take any turns. As the White
player, you will start with at most 3 tokens in some conguration. You will repeatedly take turns until all of the
Black tokens have been eliminated, at which point you win. If on your last turn you eliminate all enemy tokens
but lose your last token, you still win.

## The tasks
Firstly, your team will design and implement a program that `plays' a game of single-player Expendibots | given
a board configuration, your program will find a sequence of actions for the White player to take to win (to
eliminate all enemy tokens). Your program's performance will be judged based upon its ability to nd winning
sequences of actions and handle cases involving multiple tokens. There
is no requirement that your sequences be optimal.
Secondly, your team will write a brief report discussing and analysing the strategy your program uses to solve
this search problem. These tasks are described in detail in the following sections.
The program
You must create a program to play this game in the form of a Python 3.6 module called search (for example, a
folder named search containing a Python le called main .py as the program entry-point1 would be sufficient
| see the provided skeleton code for a starting point).
When executed, your program must read a JSON-formatted board conguration from a le, calculate a
winning sequence of actions, and print out this sequence of actions. The input and output format are specied
below, along with the coordinate system we will use for both input and output.

## Coordinate system
The coordinate system in use is a two element pair (x; y) representing the x (horizontal) and y (vertical) position
on the board.