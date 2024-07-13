#from constants import *
import random

class ComputerMove:
 @staticmethod
 def get_computer_move(board):
    available_moves = []
    
    for start_row in range(8):
        for start_col in range(8):
            piece = board[start_row][start_col]
            
            if piece == 'c':
                # Normal moves for 'c': moving one step diagonally forward left or right
                if start_row + 1 < 8 and start_col - 1 >= 0 and board[start_row + 1][start_col - 1] == ' ':
                    available_moves.append((piece, start_row, start_col, start_row + 1, start_col - 1))
                
                if start_row + 1 < 8 and start_col + 1 < 8 and board[start_row + 1][start_col + 1] == ' ':
                    available_moves.append((piece, start_row, start_col, start_row + 1, start_col + 1))
                
                # Jump moves for 'c': capturing opponent's piece by jumping over it
                if start_row + 2 < 8 and start_col - 2 >= 0 and board[start_row + 1][start_col - 1] in ('p', 'K') and board[start_row + 2][start_col - 2] == ' ':
                    available_moves.append((piece, start_row, start_col, start_row + 2, start_col - 2))
                
                if start_row + 2 < 8 and start_col + 2 < 8 and board[start_row + 1][start_col + 1] in ('K', 'p') and board[start_row + 2][start_col + 2] == ' ':
                    available_moves.append((piece, start_row, start_col, start_row + 2, start_col + 2))
            
            elif piece == 'Q':
                # Moves for 'Q': moving one step diagonally in any direction
                if start_row + 1 < 8 and start_col - 1 >= 0 and board[start_row + 1][start_col - 1] == ' ':
                    available_moves.append((piece, start_row, start_col, start_row + 1, start_col - 1))
                
                if start_row + 1 < 8 and start_col + 1 < 8 and board[start_row + 1][start_col + 1] == ' ':
                    available_moves.append((piece, start_row, start_col, start_row + 1, start_col + 1))
                
                # Capture moves for 'Q': capturing opponent's piece diagonally
                if start_row + 2 < 8 and start_col - 2 >= 0 and board[start_row + 1][start_col - 1] in ('p', 'K') and board[start_row + 2][start_col - 2] == ' ':
                    available_moves.append((piece, start_row, start_col, start_row + 2, start_col - 2))
                
                if start_row + 2 < 8 and start_col + 2 < 8 and board[start_row + 1][start_col + 1] in ('K', 'p') and board[start_row + 2][start_col + 2] == ' ':
                    available_moves.append((piece, start_row, start_col, start_row + 2, start_col + 2))
                
                # Backward moves for 'Q'
                if start_row - 1 >= 0 and start_col - 1 >= 0 and board[start_row - 1][start_col - 1] == ' ':
                    available_moves.append((piece, start_row, start_col, start_row - 1, start_col - 1))
                
                if start_row - 1 >= 0 and start_col + 1 < 8 and board[start_row - 1][start_col + 1] == ' ':
                    available_moves.append((piece, start_row, start_col, start_row - 1, start_col + 1))
                
                # Backward capture moves for 'Q'
                if start_row - 2 >= 0 and start_col - 2 >= 0 and board[start_row - 1][start_col - 1] in ('p', 'K') and board[start_row - 2][start_col - 2] == ' ':
                    available_moves.append((piece, start_row, start_col, start_row - 2, start_col - 2))
                
                if start_row - 2 >= 0 and start_col + 2 < 8 and board[start_row - 1][start_col + 1] in ('K', 'p') and board[start_row - 2][start_col + 2] == ' ':
                    available_moves.append((piece, start_row, start_col, start_row - 2, start_col + 2))
    
    if available_moves:
        capture_moves = [move for move in available_moves if abs(move[1] - move[3]) == 2]
        if capture_moves:
            return random.choice(capture_moves)
        else:
            return random.choice(available_moves)
    else:
        return None