import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.svm import LinearSVC

# Read file from parent directory

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
file_path = 'data/Preprocessed_AFData.csv'
relative_path = os.path.join(parent_dir, file_path)

data = pd.read_csv(relative_path)