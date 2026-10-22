"""Unit tests for Tic-Tac-Toe game and Minimax AI."""

import unittest
from game import AI, EMPTY, HUMAN, TicTacToe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_empty_board_has_nine_moves(self):
        self.assertEqual(len(self.game.available_moves()), 9)

    def test_winner_row(self):
        self.assertEqual(TicTacToe.winner(["X", "X", "X", " ", "O", " ", " ", "O", " "]), HUMAN)

    def test_winner_diagonal(self):
        self.assertEqual(TicTacToe.winner(["O", "X", "X", " ", "O", " ", "X", " ", "O"]), AI)

    def test_draw_detection(self):
        board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        self.assertTrue(TicTacToe.is_draw(board))

    def test_rejects_out_of_range_move(self):
        self.assertFalse(self.game.play_move(0, HUMAN))
        self.assertFalse(self.game.play_move(10, HUMAN))

    def test_rejects_occupied_move(self):
        self.assertTrue(self.game.play_move(1, HUMAN))
        self.assertFalse(self.game.play_move(1, AI))

    def test_ai_takes_winning_move(self):
        board = ["O", "O", " ", "X", "X", " ", " ", " ", " "]
        self.assertEqual(self.game.best_move(board), 2)

    def test_ai_blocks_human_win(self):
        board = ["X", "X", " ", "O", " ", " ", " ", "O", " "]
        self.assertEqual(self.game.best_move(board), 2)

    def test_ai_does_not_move_after_terminal_board(self):
        board = ["X", "X", "X", "O", "O", " ", " ", " ", " "]
        self.assertIsNone(self.game.best_move(board))

    def test_reset(self):
        self.game.play_move(1, HUMAN)
        self.game.reset()
        self.assertEqual(self.game.board, [EMPTY] * 9)


if __name__ == "__main__":
    unittest.main()
