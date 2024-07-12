from flask import Flask, jsonify, request
from board import Board

app = Flask(__name__)
board_instance = Board()

@app.route('/board', methods=['GET'])
def get_board_route():
    board = board_instance.get_board()
    return jsonify(board)

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

    # Validate the player's move
    if board_instance.validate_move(from_row, from_col, to_row, to_col):
        board_instance.make_move(from_row, from_col, to_row, to_col)

        # After player's move, let computer make a move
        board_instance.computer_move()

        return jsonify({'message': 'Move successful'})
    else:
        return jsonify({'message': 'Invalid move'})

if __name__ == '__main__':
    app.run(debug=True)
