import load_data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

af_data = load_data.gen_metadata()

# Split data into X and y

X = af_data.drop(['Control'], axis=1)
y = af_data['Control']

# Split data into training and testing sets

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

# Use Decision Tree Classifier to predict the outcome

dt = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=101)
dt.fit(x_train, y_train)
y_pred = dt.predict(x_test)

print('Accuracy of Decision Tree Classifier: {:.4F}'.format(metrics.accuracy_score(y_test, y_pred) * 100))
print(metrics.classification_report(y_test, y_pred))