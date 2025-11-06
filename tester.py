
import unittest
from game import AnimalGame, Chinchilla, Wombat, Emu, Cuttlefish

class TestAnimalGame(unittest.TestCase):
    '''Contains unit tests for game.py '''

    def test_1(self):
        """tests AnimalGame.__init__ to make sure the board is initialized with pieces and empty squares in correct spots."""
        game = AnimalGame()
        self.assertIsNotNone(game._board[0][0])
        self.assertIsNotNone(game._board[6][6])
        self.assertIsNone(game._board[3][3])

    def test_2(self):
        """tests get_game_state for when amethyst Cuttlefish is captured."""
        game = AnimalGame()
        game._board[6][3] = None
        state = game.get_game_state()
        self.assertEqual(state, "TANGERINE_WON")

    def test_3(self):
        """tests make_move for when trying to move opponent's piece out of turn."""
        game = AnimalGame()
        game._turn = "amethyst"
        result = game.make_move('a1', 'a2')
        self.assertEqual(result, False)

    def test_4(self):
        """tests Piece.get_piece_type"""
        game = AnimalGame()
        piece = game._board[0][2]
        self.assertEqual(piece.get_piece_type(), "Wombat")

    def test_5(self):
        """tests Piece.get_color"""
        game = AnimalGame()
        piece = game._board[6][5]
        self.assertEqual(piece.get_color(), "amethyst")

    def test_6(self):
        """Test Chinchilla.legal_move"""
        game = AnimalGame()
        piece = game._board[0][0]
        self.assertEqual(piece.legal_move(game._board, 0, 0, 1, 1), True)
        self.assertEqual(piece.legal_move(game._board, 0, 0, 1, 0), True)
        self.assertEqual(piece.legal_move(game._board, 0, 0, 2, 2), False)

    def test_7(self):
        """Test Wombat.legal_move"""
        piece = Wombat("tangerine")
        board = [[None for col in range(7)] for row in range(7)]
        self.assertEqual(piece.legal_move(board, 3, 3, 7, 3), False)
        self.assertEqual(piece.legal_move(board, 3, 3, 3, 7), False)

    def test_8(self):
        """Test Emu.legal_move"""
        piece = Emu("tangerine")
        board = [[None for col in range(7)] for row in range(7)]
        board[3][3] = piece
        board[4][3] = Wombat("tangerine")
        self.assertEqual(piece.legal_move(board, 3, 3, 6, 3), False)

    def test_9(self):
        """Test Cuttlefish.legal_move"""
        piece = Cuttlefish("tangerine")
        board = [[None for col in range(7)] for row in range(7)]
        board[3][3] = piece
        self.assertEqual(piece.legal_move(board, 3, 3, 5, 5), True)
        self.assertEqual(piece.legal_move(board, 3, 3, 4, 3), True)
        self.assertEqual(piece.legal_move(board, 3, 3, 6, 3), False)

if __name__ == '__main__':
    unittest.main()
