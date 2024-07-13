from board import Board
from intro import Intro
from player import Player
from movepiece import Move_piece
from computer import ComputerMove

def main():
    Intro.print_game_rules()
    game=Board()

    while True:
        Board.print_board(game)        
            
        piece,start_row,start_col,end_row,end_col=Player.get_player_move(game.board)
        Move_piece.move_piece(game.board,piece,start_row,start_col,end_row,end_col) 
        #import constants color
        from constants import ansi_yellow
        #print statements for the player
        print()
        print(f"{ansi_yellow}Player moved piece {piece}" ,
              f"from ({ansi_yellow}{start_row}{ansi_yellow},{ansi_yellow}{start_col}{ansi_yellow})"
              f"to({end_row}, {end_col})")
        #adds a space to the end of the line 
        

        
        # computer turn
        piece,start_row,start_col,end_row,end_col=ComputerMove.get_computer_move(game.board)
        Move_piece.move_piece(game.board,piece,start_row,start_col,end_row,end_col) 
        #import constants color and add in the print movement
        from constants import ansi_yellow
        print(f"computer  moved piece {piece}" ,
              f"from ({ansi_yellow}{start_row}{ansi_yellow},{ansi_yellow}{start_col}{ansi_yellow})"
              f"to({end_row}, {end_col})")

        

             



        
if __name__=="__main__":
    main()
              
