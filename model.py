# model.py
import joblib	
import shutil
import pandas as pd 
import os 
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report


def make_prediction(model, test_row):
    return model.predict([test_row])[0]

class Model():
	results = dict.fromkeys(["RandomForestClassifier","GradientBoostingClassifier","LogisticRegression","AdaBoostClassifier"])
	def __init__(self,X_train,X_test,y_train,y_test):
		self.X_train = X_train 
		self.X_test = X_test 
		self.y_train = y_train 
		self.y_test = y_test
		
	def train(self,model_class,hyperparameters):
		# the model should be the model class of 
		# hyperparameters is a dictionary 
		model = model_class(** hyperparameters) 
		model.fit(self.X_train,self.y_train)
		y_pred_train = model.predict(self.X_train) 
		y_pred_test = model.predict(self.X_test)
		training_report  = classification_report(self.y_train,y_pred_train,output_dict = True,digits=4,zero_division = 1)
		testing_report = classification_report(self.y_test, y_pred_test,output_dict = True,digits=4,zero_division = 1)
		
		self.results[model_class.__name__]  = dict()
		self.results[model_class.__name__]['training_report'] = training_report
		self.results[model_class.__name__]['testing_report'] = testing_report 
		
		print('Model results are available in the Model.results object') 
		# saving the trained model into the directory; 
		filename = f'models\{model_class.__name__}.sav'
		joblib.dump(model, filename)
		print(f'{model_class.__name__} is saved in models directory') 

	def make_result_csvs(self):
		if 'model_results_csv' in os.listdir():
			shutil.rmtree("model_results_csv")
		os.mkdir('model_results_csv') 
		
		for model in self.results.keys():
			for level in self.results[model].keys():
				df = pd.DataFrame(self.results[model][level])
				df.to_csv(f'model_results_csv\{model}_{level}.csv')


# test 