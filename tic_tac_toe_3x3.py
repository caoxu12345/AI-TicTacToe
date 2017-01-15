from artificial_intelligence import ArtificialIntelligence
# Two playes : X and O
# http://cwoebker.com/posts/tic-tac-toe


class TicTacToe3x3:
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

    def heuristic(self, player):
        X_score = 8
        O_score = 8
        for winning_combo in self.winning_combos:
            if self.X_set.intersection(winning_combo):
                O_score -= 1
            if self.O_set.intersection(winning_combo):
                X_score -= 1
        if player == "X":
            return X_score - O_score
        else:
            return O_score - X_score


if __name__ == "__main__":
    tic_tac_toe = TicTacToe3x3()
    player_one = "X"
    ai_player = ArtificialIntelligence(algorithm_chosen="alphabeta_heuristic",
                                       depth=5)
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
    '''tic_tac_toe = TicTacToe3x3(["X", None, None, None,
    None, None, None, None, None])
    tic_tac_toe.X_set = {0}
    #tic_tac_toe.O_set = {}
    tic_tac_toe.show()
    ai_player = ArtificialIntelligence()
    ai_move = ai_player.choose_move(tic_tac_toe)
    tic_tac_toe.make_move(ai_move, "O")
    tic_tac_toe.show()'''
