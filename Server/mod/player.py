# from constants import *
# from board import Board
from flask import jsonify
class Player:
    # def get_player_move(board):
                
    #     while True:
    #         while True:
    #             start_input = input(ansi_green + "Enter start position (row col): ").strip().split()

    #             if not start_input:
    #                 print(ansi_red + "please input an option")
    #                 continue

    #             if start_input[0].lower() == 'q':
    #                 print(ansi_red+"plAYER HAS QUITE 😞😞")
    #                 exit()
    #             if start_input[0].lower() == 's':
    #                 print(ansi_yellow + "Player Restarted🔄🔄🔄.")
    #                 from main import main
    #                 main()
    #             else:
    #                 break

    #         while True:               
    #             end_input = input(ansi_green + "Enter end position (row col): ").strip().split()

    #             if not end_input:
    #                 print(ansi_red + "please input an option")
    #                 continue

    #             if end_input[0].lower() == 'q':
    #                 print(ansi_red+"plAYER HAS QUITE 😞😞")
    #                 exit()
    #             if end_input[0].lower() == 's':
    #                 print(ansi_yellow + "Player Restarted 🔄🔄🔄.")
    #                 from main import main
    #                 main()
    #                 break
    #             else:
    #                 break

    #         try:
    #             start_row, start_col = map(int, start_input)
    #             end_row, end_col = map(int, end_input)
    #         except ValueError:
    #             print(ansi_red + "checking on input. Please enter integers.")
    #             continue
    #         #to not accept skipping boxes. Only move one at a time
    #         try:
    #             if not (0<=start_col<8 and 0<=start_row<8 and 0<=end_col<8 and 0<=end_col<8):
    #                 raise ValueError
    #         except ValueError:
    #             print(ansi_red + "Invalid move. You cant move outside of the board")
    #             continue

    #         try:
    #             if (start_col- end_col>2 or start_row-end_row>2):
    #                 raise ValueError
                
    #         except ValueError:
    #             print(ansi_red + "Invalid move. You cant move two blocks at once")
    #             continue

    #         try:
    #             if board[end_row][end_col] !=" ":
    #                 raise ValueError
                
    #         except ValueError:
    #             print(ansi_red + "Invalid move. You cant move tO AN OCCUPIED POSITION")
    #             continue
    #         try:
    #             if board[start_row][start_col] !="K" and end_row>start_row:
    #                 raise ValueError
                
    #         except ValueError:
    #             print(ansi_red + "Invalid move. You cant move only move a normal piece forward")
    #             continue

    #         try:
    #             if board[start_row][start_col] ==" ":
    #                 raise ValueError
                
    #         except ValueError:
    #             print(ansi_red + "Invalid move. You cant move a none existing piece")
    #             continue

    #         #can only move diagonally
    #         try:
    #             if (start_row==end_row or start_col==end_col):
    #                 raise ValueError
    #         except ValueError:
    #             print(ansi_red + "Invalid move. You can only move diagonally from your start Position")
    #             continue
    #         if board[start_row][start_col] in ['p', 'K']:
    #             piece = board[start_row][start_col]

    #         return ( piece, start_row, start_col, end_row, end_col)
    
    def validate_move(start_row,start_col,end_row,end_col,board):
            print(start_row,start_col,end_row,end_col)
            # if type(start_row,start_col,end_row,end_col)
            #    return jsonify({'message': 'checking on input. Please enter integers.'})
            # #to not accept skipping boxes. Only move one at a time
            # try:
            if not (0<=start_col<8 and 0<=start_row<8 and 0<=end_col<8 and 0<=end_col<8):
                return jsonify({'message': 'Invalid move. You cant move outside of the board'})
                

            if (-2>start_col- end_col>2 or -2>start_row-end_row>2):
                return jsonify({'message': 'Invalid move. You cant move two blocks at once'})
            

            
            if board[end_row][end_col] !=' ':
                return jsonify({'message':'Invalid move. You cant move tO AN OCCUPIED POSITION'})
                
            if board[start_row][start_col] !='K' and end_row>start_row:
                return jsonify({'message':'Invalid move. You cant move only move a normal piece forward'})

            if board[start_row][start_col] ==' ':
                return jsonify({'message':'Invalid move. You cant move a none existing piece'})
                

            #can only move diagonally
            if (start_row==end_row or start_col==end_col):
                return jsonify({'message':'Invalid move. You can only move diagonally from your start Position'})
               
            if board[start_row][start_col] in ['p', 'K']:
                piece = board[start_row][start_col]

            return ( piece, start_row, start_col, end_row, end_col)
            
        
# if __name__=='__main__':
    # game=Board()
    # Player.validate_move("5 6","4 7",game.board)