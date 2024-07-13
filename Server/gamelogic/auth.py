from flask import Flask, request, jsonify, session
# from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from models import db, User
from board import Board  # Import your Board class here
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)
db.init_app(app)
secret_key = secrets.token_hex(16)  # Generate a 32-character (16 bytes) random key
app.secret_key = secret_key

# Initialize Board instance
board_instance = Board()

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

@app.route("/board", methods=['GET'])
def get_game_board():
    if 'user_id' in session:
        # Example: Return the game board as JSON
        board = board_instance.get_board()
        return jsonify(board), 200
    else:
        return jsonify({'message': 'Authentication required to access the game board.'}), 401
@app.route('/pieces', methods=['GET'])
def get_pieces_route():
    pieces_count = board_instance.count_pieces()
    return jsonify(pieces_count)


@app.route('/move', methods=['POST'])
def player_move():
    data = request.json
    from_row = data['from_row']
    from_col = data['from_col']
    to_row = data['to_row']
    to_col = data['to_col']

    # Validate the move
    if board_instance.validate_move(from_row, from_col, to_row, to_col):
        board_instance.make_move(from_row, from_col, to_row, to_col)

        # After player's move, let computer make a move
        board_instance.computer_move()

        return jsonify({'message': 'Move successful'})
    else:
        return jsonify({'message': 'Invalid move'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
