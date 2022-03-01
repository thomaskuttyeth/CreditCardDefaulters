from datetime import datetime
from app import db 


class TrainingData(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	age = db.Column(db.Integer,nullable = False)
	bill_amount = db.Column(db.Integer,nullable = False)
	education = db.Column(db.Integer,nullable = False)
	limit_balance = db.Column(db.Integer,nullable = False)
	pay = db.Column(db.Integer,nullable = False)
	pay_amount = db.Column(db.Integer,nullable = False)
	sex = db.Column(db.Integer,nullable = False)
	marriage = db.Column(db.Integer,nullable = False)


	def __repr__(self):
		return f'age = {age}, bill_amount = {bill_amount}, education = {education} ... '
