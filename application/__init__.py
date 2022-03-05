from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asldkf29348%@kv@$@5235'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:adminpassword@localhost/CreditCardDefaulters'
# uri format ="postgres://YourUserName:YourPassword@YourHostname:5432/YourDatabaseName"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from application import routes 