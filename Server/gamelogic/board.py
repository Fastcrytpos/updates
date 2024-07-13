import random

class Board:
    def __init__(self):
        self.board = [
            [' ', 'c', ' ', 'c', ' ', 'c', ' ', 'c'],
            ['c', ' ', 'c', ' ', 'c', ' ', 'c', ' '],
            [' ', 'c', ' ', 'c', ' ', 'c', ' ', 'c'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
            [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
            ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' ']
        ]
        self.current_turn = 'player'  # Track whose turn it is

    def get_board(self):
        return self.board

    def count_pieces(self):
        player_pieces = sum(row.count('p') + row.count('K') for row in self.board)
        computer_pieces = sum(row.count('c') + row.count('Q') for row in self.board)
        return {'player_pieces': player_pieces, 'computer_pieces': computer_pieces}

    def validate_move(self, from_row, from_col, to_row, to_col):
        # Placeholder validation: Check if the move is within bounds and to an empty space
        if 0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8:
            if self.board[from_row][from_col] in ['p', 'K'] and self.board[to_row][to_col] == ' ':
                return True
        return False

    def make_move(self, from_row, from_col, to_row, to_col):
        # Make the move and update the board
        self.board[to_row][to_col] = self.board[from_row][from_col]
        self.board[from_row][from_col] = ' '

    def computer_move(self):
        # Simple logic: Choose a random move for the computer
        while True:
            from_row = random.randint(0, 7)
            from_col = random.randint(0, 7)
            to_row = random.randint(0, 7)
            to_col = random.randint(0, 7)

            if self.validate_move(from_row, from_col, to_row, to_col):
                self.make_move(from_row, from_col, to_row, to_col)
                break
