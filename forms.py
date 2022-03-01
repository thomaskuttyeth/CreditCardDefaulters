from db_model import TrainingData
from wtforms import IntegerField,SubmitField


class RegistrationForm(FlaskForm):
	age= IntegerField()
    bill_amount = IntegerField()
    education = IntegerField()
    limit_balance = IntegerField()
    pay = IntegerField()
    pay_amount = IntegerField()
    sex = IntegerField()
    marriage = IntegerField()
    submit = SubmitField('Predict')
