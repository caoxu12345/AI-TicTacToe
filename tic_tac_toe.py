import random
import time

# Two playes : X and O


class TicTacToe:
    winning_combos = (
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8},
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
        {0, 4, 8}, {2, 4, 6})

    winners = ('X win', 'Draw', 'O win')

    def __init__(self, square=[]):
        if len(square) == 0:
            self.square = [None for i in range(9)]
        else:
            self.square = square
        self.X_set = set()
        self.O_set = set()

    def show(self):
        for i in range(0, 9, 3):
            line = ""
            for case in self.square[i:i+3]:
                if case == "X":
                    line += "X "
                elif case == "O":
                    line += "O "
                else:
                    line += ". "
            print(line)

    def available_moves(self):
        available_moves_list = []
        for k, case in enumerate(self.square):
            if case is None:
                available_moves_list.append(k)
        return available_moves_list

    def make_move(self, move, player):
        if move in self.available_moves():
            self.square[move] = player
            if player == "X":
                self.X_set.add(move)
            else:
                self.O_set.add(move)
            return True
        else:
            return False

    def complete(self):
        if None in self.square:
            return False
        else:
            return True

    def has_winner(self):
        for combo in self.winning_combos:
            if combo.issubset(self.X_set) or combo.issubset(self.O_set):
                return True
        return False

    def find_winner(self):
        for combo in self.winning_combos:
            if combo.issubset(self.X_set):
                return self.winners[0]
            elif combo.issubset(self.O_set):
                return self.winners[2]
        return self.winners[1]


class ArtificialIntelligence:

    def __init__(self):
        self.thinking_time = 0

    def get_enemy(self, player):
        if player == "X":
            return "O"
        else:
            return "X"

    def minimax(self, node, player):
        if node.has_winner():
            result = node.find_winner()
            if result == "X win":
                return -1
            elif result == "O win":
                return 1
            else:
                return 0
        if node.complete():
            result = node.find_winner()
            if result == "X win":
                return -1
            elif result == "O win":
                return 1
            else:
                return 0
        best = None
        for move in node.available_moves():
            # Admin rights ...
            node.make_move(move, player)
            val = self.minimax(node, self.get_enemy(player))
            # Admin rights ...
            node.square[move] = None
            node.X_set.discard(move)
            node.O_set.discard(move)

            if best is None:
                best = val
            else:
                if player == "O":
                    if val >= best:
                        best = val
                else:
                    if val < best:
                        best = val
        return best

    def alphabeta(self, node, player, alpha, beta):
        if node.has_winner():
            result = node.find_winner()
            if result == "X win":
                return -1
            elif result == "O win":
                return 1
            else:
                return 0
        if node.complete():
            result = node.find_winner()
            if result == "X win":
                return -1
            elif result == "O win":
                return 1
            else:
                return 0
        for move in node.available_moves():
            node.make_move(move, player)
            val = self.alphabeta(node, self.get_enemy(player), alpha, beta)
            # Admin rights ...
            node.square[move] = None
            node.X_set.discard(move)
            node.O_set.discard(move)
            if player == "O":
                if val > alpha:
                    alpha = val
                elif alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                elif beta <= alpha:
                    return alpha
        if player == "O":
            return alpha
        else:
            return beta

    def choose_move(self, tic_tac_toe):
        start_thinking_time = time.time()
        limit = -2
        ai_player = "O"
        choices = []
        available_moves = tic_tac_toe.available_moves()
        if len(available_moves) == 9:
            return 4
        else:
            for move in tic_tac_toe.available_moves():
                # Admin rights ...
                tic_tac_toe.make_move(move, ai_player)
                # val = self.minimax(tic_tac_toe, self.get_enemy(ai_player))
                val = self.alphabeta(tic_tac_toe,
                                     self.get_enemy(ai_player), -2, 2)
                # Admin rights ...
                tic_tac_toe.square[move] = None
                tic_tac_toe.X_set.discard(move)
                tic_tac_toe.O_set.discard(move)
                # print("move:", move, "causes:",val)
                if val > limit:
                    limit = val
                    choices = [move]
                elif val == limit:
                    choices.append(move)
            self.thinking_time += (time.time() - start_thinking_time)
            return random.choice(choices)

if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    player_one = "X"
    ai_player = ArtificialIntelligence()
    # player_two = "O"
    tic_tac_toe.show()
    while not tic_tac_toe.complete():
        # Player one move
        try:
            player_one_move = int(input("Choose a move (0-8) : "))
        except ValueError:
            print("Wrong value, try again")
            continue
        is_move_made = tic_tac_toe.make_move(player_one_move, player_one)
        if is_move_made:
            pass
        else:
            print("This case is not in range or already chosen, try again")
            continue
        tic_tac_toe.show()
        if tic_tac_toe.complete() or tic_tac_toe.has_winner():
            break

        # Player two move
        ai_move = ai_player.choose_move(tic_tac_toe)
        tic_tac_toe.make_move(ai_move, "O")
        # available_moves = tic_tac_toe.available_moves()
        # player_two_move = random.choice(available_moves)
        # tic_tac_toe.make_move(player_two_move, player_two)
        print("Computer plays")
        tic_tac_toe.show()
        if tic_tac_toe.complete() or tic_tac_toe.has_winner():
            break
    print(tic_tac_toe.find_winner())
    print("Artificial intelligence has thought during : ",
           ai_player.thinking_time, " seconds")

    '''tic_tac_toe = TicTacToe([None, "O", None, "X", "X", "O", None, "X", None])
    tic_tac_toe.X_set = { 3, 4, 7}
    tic_tac_toe.O_set = {1, 5}
    tic_tac_toe.show()
    ai_player = ArtificialIntelligence()
    ai_move = ai_player.choose_move(tic_tac_toe)
    tic_tac_toe.make_move(ai_move, "O")
    tic_tac_toe.show()'''
