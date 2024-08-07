Red-Blue Nim Game Description
The Red-Blue Nim Game is a variant of the classic Nim game involving two types of marbles: red and blue. The objective of the game is to strategically remove marbles from the board to either win or avoid losing based on the selected game version.

Game Setup
Number of Marbles: The game starts with a certain number of red and blue marbles, which can be specified by the player. By default, both types start with 10 marbles.
Game Version: Players can choose between two versions:
Standard: The player who removes the last marble of any color loses.
Misere: The player who removes the last marble of any color wins.
Starting Player: The game can be started by either the human player or the computer.
Gameplay
Turn-Based Play:

Players alternate turns to remove marbles from the board.
On each turn, a player can remove 1 or 2 marbles from either the red or blue pile.
Human Player:

The human player selects which color of marbles to remove and how many marbles to remove (either 1 or 2).
Computer Player:

The computer player uses a strategy based on the minimax algorithm with alpha-beta pruning to determine the best move. The search depth for this decision-making process can be adjusted.
Game End:

The game ends when one of the marble piles is completely depleted.
In Standard version: If the player who made the move causes the last marble of any color to be removed, that player loses the game.
In Misere version: If the player who made the move causes the last marble of any color to be removed, that player wins the game.
Scoring
The final score is calculated based on the number of remaining marbles. The score is computed as:
Score = (Number of remaining red marbles) * 2 + (Number of remaining blue marbles) * 3
Interactive Play
User Input: Players provide input via the command line to specify the number of marbles, the game version, the first player, and the depth of the search for AI.
Computer Moves: The computer player calculates its move based on the game state to optimize its chances of winning or avoiding loss.
