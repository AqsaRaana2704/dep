#!/usr/bin/env python
# coding: utf-8

# # NIM GAME

# In[20]:


import argparse
import sys

class RbGame:
    def __init__(self, num_red, num_blue, version, first_player, depth):
        self.num_red = num_red
        self.num_blue = num_blue
        self.version = version
        self.first_player = first_player
        self.depth = depth
        self.board = {"red": num_red, "blue": num_blue}
        self.score = 0

    def print_board(self):
        print("Current board: Red - {}, Blue - {}".format(self.board["red"], self.board["blue"]))

    def get_valid_input(self, prompt):
        while True:
            try:
                num_marbles = int(input(prompt))
                if num_marbles in [1, 2]:
                    return num_marbles
                else:
                    raise ValueError("Invalid input, please enter 1 or 2")
            except ValueError as e:
                print("Error:", e)

    def remove_marbles(self, colour, num_marbles):
        self.board[colour] -= num_marbles

    def is_game_over(self):
        return self.board["red"] == 0 or self.board["blue"] == 0

    def calculate_score(self):
        self.score = self.board["red"] * 2 + self.board["blue"] * 3

    def minmax(self, depth, alpha, beta, is_maximizing):
        if self.is_game_over():
            if self.version == "standard":
                return -1 if self.board["red"] == 0 else 1
            else:  # misere
                return 1 if self.board["red"] == 0 else -1
        if depth == 0:
            return self.evaluation()
        if is_maximizing:
            best_score = -float('inf')
            for colour in ["red", "blue"]:
                for num_marbles in [1, 2]:
                    if self.board[colour] >= num_marbles:
                        self.remove_marbles(colour, num_marbles)
                        score = self.minmax(depth - 1, alpha, beta, False)
                        self.board[colour] += num_marbles
                        best_score = max(best_score, score)
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = float('inf')
            for colour in ["red", "blue"]:
                for num_marbles in [1, 2]:
                    if self.board[colour] >= num_marbles:
                        self.remove_marbles(colour, num_marbles)
                        score = self.minmax(depth - 1, alpha, beta, True)
                        self.board[colour] += num_marbles
                        best_score = min(best_score, score)
                        beta = min(beta, score)
                        if beta <= alpha:
                            break
            return best_score

    def evaluation(self):
        if self.version == "standard":
            return self.board["red"] - self.board["blue"]
        else:  # misere
            return self.board["blue"] - self.board["red"]

    def computer_move(self):
        best_score = -float('inf')
        best_move = None
        for colour in ["red", "blue"]:
            for num_marbles in [1, 2]:
                if self.board[colour] >= num_marbles:
                    self.remove_marbles(colour, num_marbles)
                    score = self.minmax(self.depth, -float('inf'), float('inf'), False)
                    self.board[colour] += num_marbles
                    if score > best_score:
                        best_score = score
                        best_move = (colour, num_marbles)
        self.remove_marbles(best_move[0], best_move[1])
        print("Computer removes {} {} marbles.".format(best_move[1], best_move[0]))

    def play_game(self):
        current_player = self.first_player
        while not self.is_game_over():
            self.print_board()
            if current_player == "human":
                colour = input("Enter 'red' or 'blue' to remove marbles: ")
                num_marbles = self.get_valid_input("Enter 1 or 2 to remove marbles: ")
                if num_marbles > self.board[colour]:
                    print("You can't remove that many marbles. There are only {} marbles left.".format(self.board[colour]))
                    continue
                self.remove_marbles(colour, num_marbles)
            else:
                self.computer_move()
            if self.is_game_over():
                if self.board["red"] == 0:
                    print("Game over! You removed all red marbles.")
                else:
                    print("Game over! You removed all blue marbles.")
                break
            current_player = "computer" if current_player == "human" else "human"
        self.calculate_score()
        print("Your final score is:", self.score)

def main():
    parser = argparse.ArgumentParser(description="Red-Blue Nim Game")
    parser.add_argument("--num-red", type=int, default=10, help="Number of red marbles")
    parser.add_argument("--num-blue", type=int, default=10, help="Number of blue marbles")
    parser.add_argument("--version", choices=["standard", "misere"], default="standard", help="Game version")
    parser.add_argument("--first-player", choices=["human", "computer"], default="human", help="First player")
    parser.add_argument("--depth", type=int, default=5, help="Search depth for AI")

    # Check if running interactively
    if any(arg.startswith('-f') for arg in sys.argv):
        args = parser.parse_args([])
    else:
        args = parser.parse_args()

    game = RbGame(args.num_red, args.num_blue, args.version, args.first_player, args.depth)
    game.play_game()

if __name__ == "__main__":
    main()


# In[ ]:




