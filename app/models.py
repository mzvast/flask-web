# -*- coding: utf-8 -*- 
from . import db

# class Engine(db.Model):

#     # Columns

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)

#     title = db.Column(db.String(128))

#     thrust = db.Column(db.Integer, default=0)

class User(db.Model):
	__tablename__='users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)
	password = db.Column(db.String(32))
	token = db.Column(db.String(32))
	school = db.Column(db.String(32))
	degree = db.Column(db.String(32))
	department = db.Column(db.String(32))
	enrollment = db.Column(db.String(32))
	gender = db.Column(db.String(32))
	birthday = db.Column(db.String(32))
	hobby = db.Column(db.String(32))
	preference = db.Column(db.String(32))

	def __init__(self, username, email,password):
		self.username = username
		self.email = email
		self.password = password
	def __repr__(self):
		return '<User %r>' % self.username