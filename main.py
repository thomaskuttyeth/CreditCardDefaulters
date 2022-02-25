# main.py
import os
working_directory = r'C:\Users\ASUS\Documents\project-carddefaulters'
if os.getcwd() != working_directory:
	os.chdir(working_directory)
else:
	pass
	
	
from dataloader import DataLoader
from model import Model
import applog

dataloader = DataLoader()
dataloader.combine()

df = dataloader.get_data()
feature_names = dataloader.preprocess_col_names()

print(feature_names) 