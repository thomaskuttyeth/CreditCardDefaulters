# data preprocessing 
import pandas as pd 
import os 
import applog
from sklearn.model_selection import train_test_split

class DataLoader():
	data_schema_json = pd.read_json('schema.json') 
	data_folder = 'Training_Data'
	final_data= 'combined_data.csv'	
	def __init__(self):
		pass 
	
	def combine(self):
		self.data_filenames = os.listdir(self.data_folder)
		dfs = []
		for filename in self.data_filenames:
			df = pd.read_csv(f'{self.data_folder}/{filename}')
			print(f'[INFO] reading {filename}')
			dfs.append(df)
		if self.final_data in os.listdir():
			os.remove(self.final_data) 
			
		# concatenated dataframe and saving to csv file 
		concat_df = pd.concat([dfs[i] for i in range(len(dfs))])
		
		# if any 'combined_data.csv' exists - deleting it 
		if self.final_data in os.listdir():
			os.remove(self.final_data)
		concat_df.to_csv(self.final_data,index = False)
		print("['info']combined_data.csv file is generated")
		
	def get_data(self):
		self.data = pd.read_csv(self.final_data)
		return self.data
	
	def preprocess_col_names(self):
		feature_names = list(self.data_schema_json.index)
		processed_feature_names = []
		for feature_name in feature_names:
			if ' ' in feature_name:
				featue_name = feature_name.replace(' ','_')
			processed_feature_names.append(feature_name)
		self.data.columns = processed_feature_names	
		return processed_feature_names
	
	
	def train_validation_split(self,selected_features,target,random_state,test_size):
		X = self.data[selected_features]
		y = self.data[target] 
		self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(X,y,test_size,random_state)
		return self.X_train,self.X_test,self.y_train,self.y_test
	

