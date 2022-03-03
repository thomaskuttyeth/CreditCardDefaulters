
import numpy as np
from flask import Flask, request,render_template
import joblib

app = Flask(__name__)
model_name = 'models/RandomForestClassifier.sav'
model = joblib.load(model_name)

@app.route('/',methods = ['GET'])
def home():
    return render_template('index.html')


@app.route("/predict",methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = request.form.get("age")	
        Bill_Amount = request.form.get("bill_amount")
        Education = request.form.get("education")
        Limit_Balance = request.form.get("limit_balance")
        Pay_6	= request.form.get("pay_6")
        Pay_amount = request.form.get("pay_amount")
        Gender = request.form.get("gender")
        Marriage = request.form.get("marriage")

        # arranging the inputs in an array 
        input_list = [Age,Bill_Amount,Education,Limit_Balance,Pay_6,Pay_amount,Gender,Marriage]
        array = np.array(input_list)
        print(array)
        # prediction using model.predict 
        output = model.predict(array.reshape(1,-1))
        output =  output[0]

        # return the page with updated predicted text 
        return render_template('index.html', prediction_text= f"Model Prediction = {output} ")
    else:
        return render_template('index.html')

    
if __name__ == "__main__":
    app.run(debug=True)