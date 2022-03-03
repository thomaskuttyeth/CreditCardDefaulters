# main.py
import os
import shutil 
import pandas as pd
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report 
from dataloader import DataLoader
from model import Model
import applog
import joblib
import numpy as np

try:
	working_directory = r'C:\Users\ASUS\Documents\GitHub\CreditCardDefaulters'
	if os.getcwd() != working_directory:
		os.chdir(working_directory)
	if 'models' in os.listdir():
		# make sure that the previously traind models should not be there. 
		shutil.rmtree('models')
except Exception as e: 
	print('[INFO] Unable to setup working directory')
else:
	print('[INFO] Working directory is set')

os.mkdir('models')


# dataloader class 
dataloader = DataLoader()
# combining the batches of data 
dataloader.combine()

# load the dataframe 
df = dataloader.get_data()
feature_names = dataloader.preprocess_col_names()


# setting target and feature names 
target = 'default_payment_next_month'
selected_features = ['AGE','BILL_AMT6','EDUCATION','LIMIT_BAL','PAY_6','PAY_AMT6','SEX','MARRIAGE'] 

X_train,X_test,y_train,y_test = dataloader.split_data(df,selected_features,target)
print('training size  = ',X_train.shape,y_train.shape)
print('testing size = ',X_test.shape,y_test.shape) 

# modeling 
hypers = {
	"RandomForestClassifier" : {
		# random forest hyperparameters 
		},
	"LogisticRegression" : {
		# additional hyperparameters can be added 
		},
	"AdaBoostClassifier" : {
		# adaboost hyperparameters 
		},
	"GradientBoostingClassifier" :{
		# gradient boost hyperparers
		},
}

model_classes = [RandomForestClassifier,GradientBoostingClassifier,AdaBoostClassifier,LogisticRegression]
classifier = Model(X_train,X_test,y_train,y_test)
for i in model_classes:
	classifier.train(model_class = i, hyperparameters = hypers[i.__name__])

# storing the model results as csv file in a dir
classifier.make_result_csvs();



print(X_test.iloc[0])
final_model = joblib.load('models/RandomForestClassifier.sav')
inp_arr = np.array(X_test.iloc[0])
print(inp_arr)
final_prediction = final_model.predict(np.array(X_test.iloc[0]).reshape(-1,1))
print(final_prediction)