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
        print('[INFO] started reading file batches') 
        for filename in self.data_filenames:
            df = pd.read_csv(f'{self.data_folder}/{filename}')
            dfs.append(df)
        if self.final_data in os.listdir():
            os.remove(self.final_data) 
                  
        concat_df = pd.concat([dfs[i] for i in range(len(dfs))])
        if self.final_data in os.listdir():
            os.remove(self.final_data)
        concat_df.columns = self.preprocess_col_names(concat_df)
        concat_df.to_csv(self.final_data,index = False)
        print("['info']combined_data.csv file is generated")
              
        
    def get_data(self):
        self.data = pd.read_csv(self.final_data)
        return self.data
    
    def preprocess_col_names(self,df):
        feature_names = list(df.columns)
        processed_feature_names = []
        for feature_name in feature_names:
            if ' ' in feature_name:
                feature_name = feature_name.replace(' ','_')
            processed_feature_names.append(feature_name)
        return processed_feature_names
    
    
    def split_data(self,df,features,target):
        X = df[features]
        y = df[target]
        return train_test_split(X,y,test_size = 0.3,random_state = 1)
        