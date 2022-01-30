"""Uses K Nearest Neighbors to classify data as AF vs Non-AF"""
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

def knn(X,y):
    # Use KNN to predict the outcome
    print("Training KNN...\n")
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    print("KNN Results\n" + "-" * 50 + "\n")
    print('Accuracy of KNN: {:.4F} \n'.format(metrics.accuracy_score(y_test, y_pred) * 100))
    print('Confusion Matrix (KNN): \n', metrics.confusion_matrix(y_test, y_pred))
    print('Area under curve (KNN): {:.4F} \n'.format(metrics.roc_auc_score(y_test, y_pred)))
    print(metrics.classification_report(y_test, y_pred))
    print("-" * 50 + "\n")
    return {'model': knn, 'x_train': x_train, 'x_test': x_test, 'y_train': y_train, 'y_test': y_test, 'y_pred': y_pred}