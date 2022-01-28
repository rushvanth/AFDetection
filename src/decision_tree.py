"""Uses Desision Tree classifier to predict AF vs Non-AF"""
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

def decision_tree(X, y):
    """Uses Desision Tree classifier to predict AF vs Non-AF"""
    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)
    # Use Decision Tree Classifier to predict the outcome
    print("Training Decision Tree Classifier...\n")
    dt = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=101)
    dt.fit(x_train, y_train)
    y_pred = dt.predict(x_test)
    print("Decision Tree Classifier Results\n" + "-" * 50 + "\n")
    print('Accuracy of Decision Tree Classifier: {:.4F} \n'.format(metrics.accuracy_score(y_test, y_pred) * 100))
    print('Confusion Matrix (Decision Tree): \n', metrics.confusion_matrix(y_test, y_pred))
    print('Area under curve (Decision Tree): {:.4F} \n'.format(metrics.roc_auc_score(y_test, y_pred)))
    print(metrics.classification_report(y_test, y_pred))
    print("-" * 50 + "\n")
    return {'model': dt, 'x_train': x_train, 'x_test': x_test, 'y_train': y_train, 'y_test': y_test, 'y_pred': y_pred}
