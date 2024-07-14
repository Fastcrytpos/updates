class Move_piece:
    def move_piece(board,piece,start_row,start_col,end_row,end_col):

        #if a normal move 
        if abs(start_row-end_row)==1:
            board[start_row][start_col]=' '
            
            if piece=="c" and end_row==7:
                board[end_row][end_col]="Q"

            elif piece=="p" and end_row==0:
                board[end_row][end_col]="K"
            else:
                board[end_row][end_col]=piece

        #if a capture moving up 
        if start_row-end_row==2:
            board[start_row][start_col]=' '
            #capturing right
            if start_col-end_col==-2:
               #captured piece
                board[start_row-1][start_col+1]=' '

                if piece=="c" and end_row==7:
                    board[end_row][end_col]="Q"

                elif piece=="p" and end_row==0:
                    board[end_row][end_col]="K"
                else:
                    board[end_row][end_col]=piece
            #capturing left 
            elif start_col-end_col==2:
               #captured piece
                board[start_row-1][start_col-1]=' '

                if piece=="c" and end_row==7:
                    board[end_row][end_col]="Q"

                elif piece=="p" and end_row==0:
                    board[end_row][end_col]="K"
                else:
                    board[end_row][end_col]=piece
               
         #if a capture moving down 
        if start_row-end_row==-2:
            board[start_row][start_col]=' '
            #capturing left
            if start_col-end_col==-2:
               #captured piece
                board[start_row+1][start_col+1]=' '
                if piece=="c" and end_row==7:
                    board[end_row][end_col]="Q"
                elif piece=="p" and end_row==0:
                    board[end_row][end_col]="K"
                else:
                    board[end_row][end_col]=piece
            #capturing right
            else:
               #captured piece
               board[start_row+1][start_col-1]=' '
               if piece=="c" and end_row==7:
                    board[end_row][end_col]="Q"

               elif piece=="p" and end_row==0:
                    board[end_row][end_col]="K"
               else:
                    board[end_row][end_col]=piece



        

        


        


   