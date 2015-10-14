from . import db

# class Engine(db.Model):

#     # Columns

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)

#     title = db.Column(db.String(128))

#     thrust = db.Column(db.Integer, default=0)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username