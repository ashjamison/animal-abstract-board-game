class AnimalGame:
    '''this class controls the board itself. It monitors the piece positions and whose turn it is - thus will communicate with each of the Piece's child classes.'''
    def __init__(self):
        '''initializes all data members'''
        self._board = []
        for row in range(7):
            new_row = []
            for col in range(7):
                new_row.append(None)
            self._board.append(new_row)
        self._turn = "tangerine"
        self._game_state = "UNFINISHED"
        tangerine_pieces = [Chinchilla("tangerine"), Wombat("tangerine"), Emu("tangerine"), Cuttlefish("tangerine"), Emu("tangerine"), Wombat("tangerine"), Chinchilla("tangerine")]
        amethyst_pieces = [Chinchilla("amethyst"), Wombat("amethyst"), Emu("amethyst"), Cuttlefish("amethyst"), Emu("amethyst"), Wombat("amethyst"), Chinchilla("amethyst")]
        self._board[0] = tangerine_pieces
        self._board[6]= amethyst_pieces

    def get_game_state(self):
        '''returns "UNFINISHED", "TANGERINE_WON", or "AMETHYST_WON" based on where the pieces are on the board'''
        tangerine_captured = True
        amethyst_captured = True
        for row in self._board:
            for square in row:
                if square is not None:
                    if square.get_piece_type() == "Cuttlefish":
                        if square.get_color() == "tangerine":
                            tangerine_captured = False
                        elif square.get_color() == "amethyst":
                            amethyst_captured = False
        if tangerine_captured is False and amethyst_captured is False:
            return "UNFINISHED"
        elif tangerine_captured is True:
            return "AMETHYST_WON"
        else:
            return "TANGERINE_WON"

    def make_move(self, moved_from, moved_to):
        '''This method makes the indicated move, updates whose turn it is, and returns True. Will return false if: the square being moved from does not contain a piece belonging to the player whose turn it is, if the piece cannot legally move to the indicated square, or if the game has already been won. Return value is based on moved_from and moved_to parameters'''
        col_labels = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}
        row_labels = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6}
        col_from = col_labels[moved_from[0]]
        row_from = row_labels[moved_from[1]]
        col_to = col_labels[moved_to[0]]
        row_to = row_labels[moved_to[1]]
        piece = self._board[row_from][col_from]
        if self.get_game_state() != "UNFINISHED":
            return False
        if self._board[row_from][col_from] is None:
            return False
        if self._turn == "tangerine" and piece.get_color() != "tangerine":
            return False
        if self._turn == "amethyst" and piece.get_color() != "amethyst":
            return False
        if not piece.legal_move(self._board, row_from, col_from, row_to, col_to):
            return False

        self._board[row_to][col_to] = piece
        self._board[row_from][col_from] = None
        if self._turn == "tangerine":
            self._turn = "amethyst"
        else:
            self._turn = "tangerine"

        return True

class Piece:
    '''this parent class will have general code related to how a piece can legally move. Each class for each individual piece will inherit from this class - thus communicating with each.'''
    def __init__(self, color, piece_type, distance):
        '''initializes all data members'''
        self._color = color
        self._piece_type = piece_type
        self._distance = distance

    def get_color(self):
        '''returns the color'''
        return self._color

    def get_piece_type(self):
        '''returns piece type'''
        return self._piece_type

    def legal_move(self, board, row_from, col_from, row_to, col_to):
        '''checks to see if a move is legal based on piece type and board state.'''
        return False

    def get_distance(self, row_from, col_from, row_to, col_to):
        '''Returns the row and column distances between two positions.'''
        return row_to - row_from, col_to - col_from

    def is_friendly_piece(self, destination_square):
        '''checks to see if the destination square contains a friendly piece'''
        if destination_square is None:
            return False
        return destination_square.get_color() == self._color

class Chinchilla(Piece):
    '''this is a child class of Piece thus communicating with that class, and will communicate with AnimalGame as the class controlling the board. Chinchilla is a sliding piece that can move diagonally for a 1-square distance.'''
    def __init__(self, color):
        '''initializes all data members'''
        super().__init__(color, "Chinchilla", distance=1)

    def legal_move(self, board, row_from, col_from, row_to, col_to):
        '''checks to see if a move is legal based Chinchilla piece rules'''
        row_distance, col_distance = self.get_distance(row_from, col_from, row_to, col_to)
        if not ((abs(row_distance) == 1 and abs(col_distance) == 1) or
                (abs(row_distance) == 1 and col_distance == 0) or
                (row_distance == 0 and abs(col_distance) == 1)):
            return False
        destination_square = board[row_to][col_to]
        if self.is_friendly_piece(destination_square):
            return False

        return True

class Wombat(Piece):
    '''this is a child class of Piece thus communicating with that class, and will communicate with AnimalGame as the class controlling the board. Wombat is a jumping piece that can move orthogonally for a 4-square distance.'''
    def __init__(self, color):
        '''initializes all data members'''
        super().__init__(color, "Wombat", distance=4)

    def legal_move(self, board, row_from, col_from, row_to, col_to):
        '''checks to see if a move is legal based Wombat piece rules'''
        row_distance, col_distance = self.get_distance(row_from, col_from, row_to, col_to)
        if not ((abs(row_distance) == 1 and abs(col_distance) == 1) or
                (abs(row_distance) == 4 and col_distance == 0) or
                (row_distance == 0 and abs(col_distance) == 4)):
            return False
        destination_square = board[row_to][col_to]
        if self.is_friendly_piece(destination_square):
            return False

        return True

class Emu(Piece):
    '''this is a child class of Piece thus communicating with that class, and will communicate with AnimalGame as the class controlling the board. Emu is a sliding piece that can move orthogonally for a 3-square distance.'''
    def __init__(self, color):
        '''initializes all data members'''
        super().__init__(color, "Emu", distance=3)

    def legal_move(self, board, row_from, col_from, row_to, col_to):
        '''checks to see if a move is legal based Emu piece rules'''
        row_distance, col_distance = self.get_distance(row_from, col_from, row_to, col_to)
        if not ((abs(row_distance) == 1 and abs(col_distance) == 1) or
                (abs(row_distance) == 3 and col_distance == 0) or
                (row_distance == 0 and abs(col_distance) == 3)):
            return False
        destination_square = board[row_to][col_to]
        if self.is_friendly_piece(destination_square):
            return False
        if abs(row_distance) == 3 and col_distance == 0:
            if row_distance > 0:
                step = 1
            else:
                step = -1
            current_row = row_from + step
            while current_row != row_to:
                if board[current_row][col_from] is not None:
                    return False
                current_row += step
        if abs(col_distance) == 3 and row_distance == 0:
            if col_distance > 0:
                step = 1
            else:
                step = -1
            current_col = col_from + step
            while current_col != col_to:
                if board[row_from][current_col] is not None:
                    return False
                current_col += step

        return True

class Cuttlefish(Piece):
    '''this is a child class of Piece thus communicating with that class, and will communicate with AnimalGame as the class controlling the board. Cuttlefish is a jumping piece that can move diagonally for a 2-square distance. The game ends when this piece is captured by the opponent'''
    def __init__(self, color):
        '''initializes all data members'''
        super().__init__(color, "Cuttlefish", distance=2)

    def legal_move(self, board, row_from, col_from, row_to, col_to):
        '''checks to see if a move is legal based Cuttlefish piece rules'''
        row_distance, col_distance = self.get_distance(row_from, col_from, row_to, col_to)
        if not ((abs(row_distance) == 2 and abs(col_distance) == 2) or
                (abs(row_distance) == 1 and col_distance == 0) or
                (row_distance == 0 and abs(col_distance) == 1)):
            return False
        destination_square = board[row_to][col_to]
        if self.is_friendly_piece(destination_square):
            return False

        return True

game = AnimalGame()
move_result = game.make_move('c2', 'c4')
state = game.get_game_state()