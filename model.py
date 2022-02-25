# model.py
import joblib	
import shutil
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report


def make_prediction(model, test_row):
    return model.predict([test_row])[0]

class Model:
	results = dict.fromkeys(["RandomForestClassifier","GradientBoostingClassifier","LogisticRegression","AdaBoostClassifier"])
	def __init__(self,X_train,X_test,y_train,y_test):
		self.X_train = X_train 
		self.X_test = X_test 
		self.y_train = y_train 
		self.y_test = y_test
		
	def train(self,model_class,hyperparameters):
		# the model should be the model class of 
		# hyperparameters is a dictionary 
		model = model_class(hyperparameters) 
		model.fit(self.X_train,y_train)
		y_pred_train = model.predict(self.X_train) 
		y_pred_test = model.predict(self.X_test)
		training_report  = classification_report(y_train,y_pred_train)
		testing_report = classificaton_report(y_test, y_pred_test) 
		
		self.results[str(model_class)] = (training_report,testing_report)
		print('Model results are available in the Model.results object') 
		# saving the trained model into the directory; 
		if 'models' in os.listdir():
			# make sure that the previously traind models should not be there. 
			shutil.rmtree('models')
			os.mkdir('models')
		joblib.dump(model,f'{str(model_class)}_model') 
		
		print('str(model_class) is saved in models directory') 

