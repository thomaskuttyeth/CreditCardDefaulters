import numpy as np 
from flask import Flask, request,render_template 
import joblib
import preprocessing


cols = preprocessing.features

app = Flask(__name__)
model = joblib.load('model_jlib')

def model_predict(model, test_row):
    return model.predict([test_row])[0]
@app.route('/')
@app.route('/home',methods = ['GET'])
def home():
    return render_template('index.html', cols = cols)


@app.route("/predict",methods = ['GET','POST'])
def predict():
    input_ar = []
    if request.method =='POST':
        # getting the feature inputs from the cslient 
        for i in cols:
            input_ar.append(int(request.form.get('i')))
        input_ar = np.array(input_ar)
        
        #making prediction using the loaded model 
        prediction= model.predict(input_ar.rehshape(1,-1))
        print(prediction) 
        return render_template('index.html', prediction = prediction,cols = cols)
    else:
        return render_template('index.html',cols = cols)

if __name__ == "__main__":
    app.run(debug = True) 
    

        
        
        