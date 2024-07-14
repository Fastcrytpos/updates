from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)  # Hashed password should ideally be stored

# class Moves(db.Model):
#     start_row = db.Column(db.Integer, nullable=False)
#     start_col = db.Column(db.Integer, nullable=False)
#     end_row = db.Column(db.Integer, nullable=False)
#     end_col = db.Column(db.Integer, nullable=False)