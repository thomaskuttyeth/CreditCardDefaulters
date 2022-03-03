import numpy as np
from flask import Flask, request,render_template
import joblib

app = Flask(__name__)
model_name = 'random_forest_model.sav'
model = joblib.load(model_name)

@app.route('/',methods = ['GET'])
def home():
    return render_template('index.html')


@app.route("/predict",methods=['POST'])
def predict():
    if request.method == 'POST':
        Limit_Balance = request.form.get("limit_balance")
        gender = request.form.get("gender")
        education = request.form.get("education")
        marriage = request.form.get("marriage")
        age = request.form.get("age")
        pay_amount = request.form.get("pay_amount")
       
        # arranging the inputs in an array 
        input_list = [Limit_Balance,gender,education,marriage,age,pay_amount]
        array = np.array(input_list)
        print(array)
        # prediction using model.predict 
        output = model.predict([array])

        # return the page with updated predicted text 
        return render_template('index.html', prediction_text= f"Model Prediction = {output} ")
    else:
        return render_template('index.html')

    
if __name__ == "__main__":
    app.run(debug=True)


