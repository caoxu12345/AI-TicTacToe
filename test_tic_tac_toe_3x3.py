import unittest
from tic_tac_toe_3x3 import TicTacToe3x3
from artificial_intelligence import MinimaxArtificialIntelligence
from artificial_intelligence import AlphaBetaArtificialIntelligence
from artificial_intelligence import MinimaxHeuristicArtificialIntelligence
from artificial_intelligence import AlphaBetaHeuristicArtificialIntelligence


class TicTacToe3x3Tests(unittest.TestCase):

    def test_tic_tac_toe_creation(self):
        tic_tac_toe = TicTacToe3x3()
        self.assertEqual(tic_tac_toe.square, [None for i in range(9)])

    def test_tic_tac_toe_available_moves(self):
        tic_tac_toe = TicTacToe3x3()
        self.assertEqual(tic_tac_toe.available_moves(), [i for i in range(9)])

    def test_tic_tac_toe_available_moves_in_game(self):
        tic_tac_toe = TicTacToe3x3(["X", None, None, None, None,
                                    "O", None, None, None])
        self.assertEqual(tic_tac_toe.available_moves(), [1, 2, 3, 4, 6, 7, 8])

    def test_tic_tac_toe_make_move(self):
        tic_tac_toe = TicTacToe3x3()
        self.assertEqual(tic_tac_toe.make_move(0, "X"), True)
        self.assertEqual(tic_tac_toe.square, ["X", None, None, None, None,
                                              None, None, None, None])

    def test_tic_tac_toe_make_move_in_game(self):
        tic_tac_toe = TicTacToe3x3(["X", None, None, None, None,
                                    "O", None, None, None])
        self.assertEqual(tic_tac_toe.make_move(1, "X"), True)
        self.assertEqual(tic_tac_toe.square, ["X", "X", None, None, None,
                                              "O", None, None, None])

    def test_tic_tac_toe_make_move_alredy_occupied(self):
        tic_tac_toe = TicTacToe3x3(["X", None, None, None, None,
                                    "O", None, None, None])
        self.assertEqual(tic_tac_toe.make_move(0, "O"), False)
        self.assertEqual(tic_tac_toe.square, ["X", None, None, None, None,
                                              "O", None, None, None])

    def test_tic_tac_toe_complete(self):
        tic_tac_toe = TicTacToe3x3(["X", "X", "X", "X", "X",
                                    "O", "X", "X", "X"])
        self.assertEqual(tic_tac_toe.complete(), True)

    def test_tic_tac_toe_not_complete(self):
        tic_tac_toe = TicTacToe3x3(["X", None, None, None, None,
                                    "O", None, None, None])
        self.assertEqual(tic_tac_toe.complete(), False)

    def test_tic_tac_toe_has_winner(self):
        tic_tac_toe = TicTacToe3x3(["X", "X", "X", "X", "X",
                                    "O", "X", "X", "X"])
        tic_tac_toe.X_set = {0, 1, 2, 3, 4, 6, 7, 8}
        tic_tac_toe.O_set = {5}
        self.assertEqual(tic_tac_toe.has_winner(), True)

    def test_tic_tac_toe_not_has_winner(self):
        tic_tac_toe = TicTacToe3x3()
        self.assertEqual(tic_tac_toe.has_winner(), False)

    def test_tic_tac_toe_find_winner(self):
        tic_tac_toe = TicTacToe3x3(["X", "X", "X", "X", "X",
                                    "O", "X", "X", "X"])
        tic_tac_toe.X_set = {0, 1, 2, 3, 4, 6, 7, 8}
        tic_tac_toe.O_set = {5}
        self.assertEqual(tic_tac_toe.find_winner(), "X win")

    def test_tic_tac_toe_find_winner_o_win(self):
        tic_tac_toe = TicTacToe3x3(["X", "O", "X", "O", "O",
                                    "O", "X", "O", "X"])
        tic_tac_toe.X_set = {0, 2, 6, 8}
        tic_tac_toe.O_set = {1, 3, 4, 5, 7}
        self.assertEqual(tic_tac_toe.find_winner(), "O win")

    def test_tic_tac_toe_find_winner_draw(self):
        tic_tac_toe = TicTacToe3x3(["X", "X", "O", "O", "O",
                                    "X", "X", "X", "O"])
        tic_tac_toe.X_set = {0, 1, 5, 6, 7}
        tic_tac_toe.O_set = {2, 3, 4, 8}
        self.assertEqual(tic_tac_toe.find_winner(), "Draw")

    def test_heuristic_beginning(self):
        tic_tac_toe = TicTacToe3x3()
        self.assertEqual(tic_tac_toe.heuristic('O'), 0)

    def test_tic_tac_toe_heuristic(self):
        tic_tac_toe = TicTacToe3x3(["X", "O", None, "O", None,
                                    None, "X", "O", "X"])
        tic_tac_toe.X_set = {0, 6, 8}
        tic_tac_toe.O_set = {1, 3, 7}
        self.assertEqual(tic_tac_toe.heuristic('O'), -1)


class ArtificialIntelligenceTicTacToe3x3Tests(unittest.TestCase):

    def test_minimax_artificial_intelligence_creation(self):
        minimax_artificial_intelligence = MinimaxArtificialIntelligence()
        self.assertEqual(minimax_artificial_intelligence.symbol, "O")

    def test_alphabeta_artificial_intelligence_creation(self):
        alphabeta_artificial_intelligence = AlphaBetaArtificialIntelligence()
        self.assertEqual(alphabeta_artificial_intelligence.symbol, "O")

    def test_minimax_heuristic_artificial_intelligence_creation(self):
        minimax_heuristic_artificial_intelligence = \
            MinimaxHeuristicArtificialIntelligence()
        self.assertEqual(minimax_heuristic_artificial_intelligence.symbol, "O")
        self.assertEqual(minimax_heuristic_artificial_intelligence.depth, 5)

    def test_alphabeta_heuristic_artificial_intelligence_creation(self):
        alphabeta_heuristic_artificial_intelligence = \
            AlphaBetaHeuristicArtificialIntelligence()
        self.assertEqual(alphabeta_heuristic_artificial_intelligence.symbol,
                         "O")
        self.assertEqual(alphabeta_heuristic_artificial_intelligence.depth, 5)

    def test_minimax_against_minimax(self):
        result_list = []
        for i in range(5):
            first_ai_player = MinimaxArtificialIntelligence()
            second_ai_player = MinimaxArtificialIntelligence(symbol="X")
            tic_tac_toe = TicTacToe3x3()

            while not tic_tac_toe.complete():
                # AI one
                first_ai_move = first_ai_player.choose_move(
                                                        tic_tac_toe)
                tic_tac_toe.make_move(first_ai_move,
                                      first_ai_player.symbol)
                if tic_tac_toe.complete() or tic_tac_toe.has_winner():
                    break

                # AI two
                second_ai_move = second_ai_player.choose_move(
                                                        tic_tac_toe)
                tic_tac_toe.make_move(second_ai_move,
                                      second_ai_player.symbol)
                if tic_tac_toe.complete() or tic_tac_toe.has_winner():
                    break
            result_list.append(tic_tac_toe.find_winner())
        self.assertEqual(result_list, ["Draw" for i in range(5)])

    def test_alphabeta_against_alphabeta(self):
        result_list = []
        for i in range(5):
            first_ai_player = AlphaBetaArtificialIntelligence()
            second_ai_player = AlphaBetaArtificialIntelligence(symbol="X")
            tic_tac_toe = TicTacToe3x3()

            while not tic_tac_toe.complete():
                # AI one
                first_ai_move = first_ai_player.choose_move(
                                                        tic_tac_toe)
                tic_tac_toe.make_move(first_ai_move,
                                      first_ai_player.symbol)
                if tic_tac_toe.complete() or tic_tac_toe.has_winner():
                    break

                # AI two
                second_ai_move = second_ai_player.choose_move(
                                                        tic_tac_toe)
                tic_tac_toe.make_move(second_ai_move,
                                      second_ai_player.symbol)
                if tic_tac_toe.complete() or tic_tac_toe.has_winner():
                    break
            result_list.append(tic_tac_toe.find_winner())
        self.assertEqual(result_list, ["Draw" for i in range(5)])

    def test_minimax_heuristic_against_alphabeta(self):
        result_list = []
        for i in range(5):
            first_ai_player = MinimaxArtificialIntelligence()
            second_ai_player = AlphaBetaArtificialIntelligence(symbol="X")
            tic_tac_toe = TicTacToe3x3()

            while not tic_tac_toe.complete():
                # AI one
                first_ai_move = first_ai_player.choose_move(
                                                        tic_tac_toe)
                tic_tac_toe.make_move(first_ai_move,
                                      first_ai_player.symbol)
                if tic_tac_toe.complete() or tic_tac_toe.has_winner():
                    break

                # AI two
                second_ai_move = second_ai_player.choose_move(
                                                        tic_tac_toe)
                tic_tac_toe.make_move(second_ai_move,
                                      second_ai_player.symbol)
                if tic_tac_toe.complete() or tic_tac_toe.has_winner():
                    break
            result_list.append(tic_tac_toe.find_winner())
        self.assertEqual(result_list, ["Draw" for i in range(5)])

    def test_alphabeta_heuristic_against_alphabeta(self):
        result_list = []
        for i in range(5):
            first_ai_player = \
                AlphaBetaHeuristicArtificialIntelligence(symbol="O")
            second_ai_player = AlphaBetaArtificialIntelligence(symbol="X")
            tic_tac_toe = TicTacToe3x3()

            while not tic_tac_toe.complete():
                # AI one
                first_ai_move = first_ai_player.choose_move(
                                                        tic_tac_toe)
                tic_tac_toe.make_move(first_ai_move,
                                      first_ai_player.symbol)
                if tic_tac_toe.complete() or tic_tac_toe.has_winner():
                    break

                # AI two
                second_ai_move = second_ai_player.choose_move(
                                                        tic_tac_toe)
                tic_tac_toe.make_move(second_ai_move,
                                      second_ai_player.symbol)
                if tic_tac_toe.complete() or tic_tac_toe.has_winner():
                    break
            result_list.append(tic_tac_toe.find_winner())
        self.assertEqual(result_list, ["Draw" for i in range(5)])

    def test_minimax_against_human_strategy(self):
        result_list = []
        for i in range(30):
            first_ai_player = MinimaxArtificialIntelligence(symbol="O")
            tic_tac_toe = TicTacToe3x3(["X", None, None, None, "O", None, None,
                                        None, "X"])
            tic_tac_toe.X_set = {0, 8}
            tic_tac_toe.O_set = {4}
            first_ai_move = first_ai_player.choose_move(tic_tac_toe)
            result_list.append(first_ai_move)
        self.assertNotIn(2, result_list)
        self.assertNotIn(6, result_list)
        result_list = []
        for i in range(30):
            first_ai_player = MinimaxArtificialIntelligence(symbol="O")
            tic_tac_toe = TicTacToe3x3(["X", None, None, None, None, None,
                                        None, None, None])
            tic_tac_toe.X_set = {0}
            first_ai_move = first_ai_player.choose_move(tic_tac_toe)
            result_list.append(first_ai_move)
        self.assertEqual([4 for i in range(30)], result_list)

    def test_alphabeta_against_human_strategy(self):
        result_list = []
        for i in range(40):
            first_ai_player = AlphaBetaArtificialIntelligence(symbol="O")
            tic_tac_toe = TicTacToe3x3(["X", None, None, None, "O", None, None,
                                        None, "X"])
            tic_tac_toe.X_set = {0, 8}
            tic_tac_toe.O_set = {4}
            first_ai_move = first_ai_player.choose_move(tic_tac_toe)
            result_list.append(first_ai_move)
        self.assertNotIn(2, result_list)
        self.assertNotIn(6, result_list)
        result_list = []
        for i in range(40):
            first_ai_player = AlphaBetaArtificialIntelligence(symbol="O")
            tic_tac_toe = TicTacToe3x3(["X", None, None, None, None, None,
                                        None, None, None])
            tic_tac_toe.X_set = {0}
            first_ai_move = first_ai_player.choose_move(tic_tac_toe)
            result_list.append(first_ai_move)
        self.assertEqual([4 for i in range(40)], result_list)

    def test_minimax_heuristic_against_human_strategy(self):
        result_list = []
        for i in range(50):
            first_ai_player = \
                MinimaxHeuristicArtificialIntelligence(symbol="O")
            tic_tac_toe = TicTacToe3x3(["X", None, None, None, "O", None, None,
                                        None, "X"])
            tic_tac_toe.X_set = {0, 8}
            tic_tac_toe.O_set = {4}
            first_ai_move = first_ai_player.choose_move(tic_tac_toe)
            result_list.append(first_ai_move)
        self.assertNotIn(2, result_list)
        self.assertNotIn(6, result_list)
        result_list = []
        for i in range(50):
            first_ai_player = \
                MinimaxHeuristicArtificialIntelligence(symbol="O")
            tic_tac_toe = TicTacToe3x3(["X", None, None, None, None, None,
                                        None, None, None])
            tic_tac_toe.X_set = {0}
            first_ai_move = first_ai_player.choose_move(tic_tac_toe)
            result_list.append(first_ai_move)
        self.assertNotIn(2, result_list)
        self.assertNotIn(6, result_list)

    def test_alphabeta_heuristic_against_human_strategy(self):
        result_list = []
        for i in range(50):
            first_ai_player = \
                AlphaBetaHeuristicArtificialIntelligence(symbol="O")
            tic_tac_toe = TicTacToe3x3(["X", None, None, None, "O", None, None,
                                        None, "X"])
            tic_tac_toe.X_set = {0, 8}
            tic_tac_toe.O_set = {4}
            first_ai_move = first_ai_player.choose_move(tic_tac_toe)
            result_list.append(first_ai_move)
        self.assertNotIn(2, result_list)
        self.assertNotIn(6, result_list)
        for i in range(50):
            first_ai_player = \
                AlphaBetaHeuristicArtificialIntelligence(symbol="O")
            tic_tac_toe = TicTacToe3x3(["X", None, None, None, None, None,
                                        None, None, None])
            tic_tac_toe.X_set = {0}
            first_ai_move = first_ai_player.choose_move(tic_tac_toe)
            result_list.append(first_ai_move)
        self.assertNotIn(2, result_list)
        self.assertNotIn(6, result_list)
