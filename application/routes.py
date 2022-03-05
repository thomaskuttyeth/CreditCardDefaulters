import joblib
model = joblib.load('application\\random_forest_model.sav')
from application import app,db
from application.forms import PredictionForm
from application.models import Monitoring
import numpy as np 
from flask import render_template,request,flash,redirect,url_for, redirect
import pandas as pd 


@app.route('/',methods = ['GET'])
def home():
    return render_template('home.html')

from flask import send_file

@app.route('/download_training_data', methods = ['GET'])
def download_training_data():
    return send_file(
        'training_data.csv',
        mimetype='text/csv',
        attachment_filename='training_data.csv',
        as_attachment=True)

@app.route('/download_validation_data', methods = ['GET'])
def download_validation_data():
    return send_file(
        'validation_data.csv',
        mimetype='text/csv',
        attachment_filename='validation_data.csv',
        as_attachment=True)
    
@app.route("/make_prediction",methods=['GET','POST'])
def make_prediction():
    form = PredictionForm() 
    if form.validate_on_submit():

        Limit_Balance =  form.Limit_Balance.data,
        gender = form.gender.data,
        education = form.education.data,
        marriage = form.marriage.data,
        age = form.age.data,
        pay_amount = form.pay_amount.data

        input_ar = [[Limit_Balance[0],gender[0],education[0],marriage[0],age[0],pay_amount]]
        model_output = model.predict(input_ar)

        row_data = Monitoring(Limit_Balance= Limit_Balance[0],
            gender = gender[0],
            education = education[0],
            marriage = marriage[0],
            age = age[0],
            pay_amount = pay_amount,
            model_prediction = int(model_output[0])
            )
        db.session.add(row_data)
        db.session.commit()
        flash(f"Features and the model prediction is inserted to the database",'warning') 
        if model_output[0] == 0:
            flash(f"Model Prediction is {model_output[0]}!", 'success')
        else:
            flash(f"Model Prediction is {model_output[0]}!", 'danger')
    return render_template('prediction.html',form = form)

    