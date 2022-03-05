from flask_wtf import FlaskForm
from wtforms import IntegerField,SubmitField
from wtforms.validators import DataRequired,Length,InputRequired

class PredictionForm(FlaskForm):
	Limit_Balance = IntegerField('Limit Balance',validators = [DataRequired()])
	gender = IntegerField('Gender',validators = [DataRequired()])
	education = IntegerField('Education',validators = [DataRequired()])
	marriage = IntegerField('Marriage',validators = [InputRequired()])
	age = IntegerField('Age',validators = [DataRequired()])
	pay_amount = IntegerField('Pay Amount',validators = [DataRequired()])
	submit = SubmitField('Get Prediction')
