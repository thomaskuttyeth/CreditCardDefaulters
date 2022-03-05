from application import db

class Monitoring(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    Limit_Balance = db.Column(db.Integer,nullable = False)
    gender = db.Column(db.Integer,nullable = False)
    education = db.Column(db.Integer,nullable = False)
    marriage = db.Column(db.Integer, nullable = False)
    age = db.Column(db.Integer,nullable = False)
    pay_amount = db.Column(db.Integer,nullable = False)
    model_prediction = db.Column(db.Integer,nullable = True )

    def __repr__(self):
        return f"Row('{self.Limit_Balance},{self.gender},{self.education},{self.marriage},{self.age},{self.pay_amount},{self.model_prediction})"
