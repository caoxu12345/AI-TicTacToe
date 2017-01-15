import random
import time


class ArtificialIntelligence:

    def __init__(self, algorithm_chosen="minimax", symbol="O", depth=5):
        self.thinking_time = 0
        self.algorithm_chosen = algorithm_chosen
        self.symbol = symbol
        self.depth = depth

    def get_enemy(self, player):
        if player == "X":
            return "O"
        else:
            return "X"

    def get_final_score(self, result):
        if result == "X win":
            if self.symbol == "O":
                return -1
            else:
                return 1
        elif result == "O win":
            if self.symbol == "O":
                return 1
            else:
                return -1
        else:
            return 0

    def get_heuristic_final_score(self, result):
        if result == "X win":
            if self.symbol == "O":
                return -100
            else:
                return 100
        elif result == "O win":
            if self.symbol == "O":
                return 100
            else:
                return -100
        else:
            return 0

    def minimax(self, node, player):
        if node.has_winner():
            result = node.find_winner()
            return self.get_final_score(result)
        if node.complete():
            result = node.find_winner()
            return self.get_final_score(result)
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
                if player == self.symbol:
                    if val >= best:
                        best = val
                else:
                    if val < best:
                        best = val
        return best

    def minimax_heuristic(self, node, player, depth):
        if node.has_winner():
            result = node.find_winner()
            return self.get_heuristic_final_score(result)
        if node.complete():
            result = node.find_winner()
            return self.get_heuristic_final_score(result)
        if depth == 0:
            return node.heuristic(self.symbol)
        else:
            best = None
            for move in node.available_moves():
                # Admin rights ...
                node.make_move(move, player)
                val = self.minimax_heuristic(node, self.get_enemy(player),
                                             depth - 1)
                # Admin rights ...
                node.square[move] = None
                node.X_set.discard(move)
                node.O_set.discard(move)

                if best is None:
                    best = val
                else:
                    if player == self.symbol:
                        if val >= best:
                            best = val
                    else:
                        if val < best:
                            best = val
            return best

    def alphabeta(self, node, player, alpha, beta):
        if node.has_winner():
            result = node.find_winner()
            return self.get_final_score(result)
        if node.complete():
            result = node.find_winner()
            return self.get_final_score(result)
        for move in node.available_moves():
            node.make_move(move, player)
            val = self.alphabeta(node, self.get_enemy(player), alpha, beta)
            # Admin rights ...
            node.square[move] = None
            node.X_set.discard(move)
            node.O_set.discard(move)
            if player == self.symbol:
                if val > alpha:
                    alpha = val
                elif alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                elif beta <= alpha:
                    return alpha
        if player == self.symbol:
            return alpha
        else:
            return beta

    def alphabeta_heuristic(self, node, player, alpha, beta, depth):
        if node.has_winner():
            result = node.find_winner()
            return self.get_heuristic_final_score(result)
        if node.complete():
            result = node.find_winner()
            return self.get_heuristic_final_score(result)
        if depth == 0:
            return node.heuristic(self.symbol)
        for move in node.available_moves():
            node.make_move(move, player)
            val = self.alphabeta_heuristic(node, self.get_enemy(player),
                                           alpha, beta, depth - 1)
            # Admin rights ...
            node.square[move] = None
            node.X_set.discard(move)
            node.O_set.discard(move)
            if player == self.symbol:
                if val > alpha:
                    alpha = val
                elif alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                elif beta <= alpha:
                    return alpha
        if player == self.symbol:
            return alpha
        else:
            return beta

    def choose_move(self, tic_tac_toe):
        start_thinking_time = time.time()
        limit = -200
        ai_player = self.symbol
        choices = []
        available_moves = tic_tac_toe.available_moves()
        # if len(available_moves) == len(tic_tac_toe.square):
        # return 4
        # else:
        for move in tic_tac_toe.available_moves():
            # print("next move :", move)
            # Admin rights ...
            tic_tac_toe.make_move(move, ai_player)
            if self.algorithm_chosen == "minimax":
                val = self.minimax(tic_tac_toe, self.get_enemy(ai_player))
            elif self.algorithm_chosen == "alphabeta":
                val = self.alphabeta(tic_tac_toe,
                                     self.get_enemy(ai_player), -2, 2)
            elif self.algorithm_chosen == "minimax_heuristic":
                val = self.minimax_heuristic(tic_tac_toe,
                                             self.get_enemy(ai_player),
                                             self.depth)
            elif self.algorithm_chosen == "alphabeta_heuristic":
                val = self.alphabeta_heuristic(tic_tac_toe,
                                               self.get_enemy(ai_player),
                                               -200, 200, self.depth)
            # print(val)
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
