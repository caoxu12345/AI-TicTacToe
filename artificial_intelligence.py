import random
import time


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
        if len(available_moves) == len(tic_tac_toe.square):
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
