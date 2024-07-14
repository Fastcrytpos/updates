from flask import Flask, request, jsonify, session,redirect
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt  # For password hashing
from models import db, User
from mod.player import Player
from mod.board import Board
from mod.movepiece import Move_piece
from mod.computer import ComputerMove
from mod.constants import *




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Secret key for session management
bcrypt = Bcrypt(app)
db.init_app(app)
CORS(app)


# Routes for APIs

@app.route("/register", methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'Missing username, email, or password'}), 400

    existing_user = User.query.filter_by(username=username).first()
    existing_email = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({'message': 'Username already exists. Please choose a different one.'}), 409
    elif existing_email:
        return jsonify({'message': 'Email address already registered. Please use a different email.'}), 409
    else:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'Account created successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Missing username or password'}), 400

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'message': 'Login unsuccessful. Please check your username and password.'}), 401

@app.route("/logout", methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully!'}), 200

@app.route("/profile", methods=['GET'])
def profile():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email
        }), 200
    else:
        return jsonify({'message': 'Authentication required to access this resource.'}), 401


@app.route("/game", methods=['GET','POST'])
def get_game_board():
    game = Board()
    board=game.board
    # if 'user_id' in session:
    if request.method=='GET':
        # Example: Return the game board as JSON
        return jsonify(board), 200
    
    if request.method=='POST':
        data = request.get_json()
       
        start_row = data.get('start_row')
        start_col = data.get('start_col')
        end_row = data.get('end_row')
        end_col = data.get('end_col')

        if not end_col or not end_row or not start_row or not start_col:
             return jsonify({'message': 'One of the values is missing'}), 400
        elif not (0<=start_col<8 and 0<=start_row<8 and 0<=end_col<8 and 0<=end_col<8):
                return jsonify({'message': 'Invalid move. You cant move outside of the board'})

        elif (start_col- end_col>2 or start_row-end_row>2 ):
            return jsonify({'message': 'Invalid move. You cant move two blocks at once'})
        
        elif board[end_row][end_col] !=' ':
            return jsonify({'message':'Invalid move. You cant move tO AN OCCUPIED POSITION'})
            
        elif board[start_row][start_col] !='K' and end_row>start_row:
            return jsonify({'message':'Invalid move. You cant move only move a normal piece forward'})

        elif board[start_row][start_col] ==' ':
            return jsonify({'message':'Invalid move. You cant move a none existing piece'})
            

        #can only move diagonally
        elif (start_row==end_row or start_col==end_col):
            return jsonify({'message':'Invalid move. You can only move diagonally from your start Position'})
            
        elif board[start_row][start_col] in ['p', 'K']:
            piece = board[start_row][start_col]
            
            # Player's move
            Move_piece.move_piece(board, piece, start_row, start_col, end_row, end_col)
            player_move_message = f'player moved {piece} from {start_row},{start_col} to {end_row},{end_col}'

            # Computer's move
            computer_piece,computer_start_row, computer_start_col, computer_end_row, computer_end_col = ComputerMove.get_computer_move(board)
            Move_piece.move_piece(board, computer_piece, computer_start_row, computer_start_col, computer_end_row, computer_end_col)
            computer_move_message = f'computer moved {computer_piece} from {computer_start_row},{computer_start_col} to {computer_end_row},{computer_end_col}'

            # Combine the messages and board into a single JSON response
            response = {
                'player_move': player_move_message,
                'computer_move': computer_move_message,
                'board': board
            }

            return jsonify(response)
        


        # else:
            # Player.validate_move(start_row,start_col,end_row,end_col,board)
            
            # return jsonify(board), 200 

        

    # else:
    #     return jsonify({'message': 'Authentication required to access the game board.'}), 401




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
