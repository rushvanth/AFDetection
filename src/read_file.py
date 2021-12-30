import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Read file from parent directory

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
file_name = 'Preprocessed_AFData.xlsx'
file_path = os.path.join(parent_dir, file_name)

data = pd.read_excel(file_path)
print(data.head())

af_episodes = list(data['Control'])
count_1s = [i for i in af_episodes if i == 1]
print(len(count_1s))