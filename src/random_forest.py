"""Uses Random Forest Classifier to classify data as AF vs Non-AF"""
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

def random_forest(X,y):
    """Uses Random Forest Classifier to classify data as AF vs Non-AF"""
    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)
    # Use Random Forest Classifier to predict the outcome
    print("Training Random Forest Classifier...\n")
    rf = RandomForestClassifier(n_estimators=100, random_state=101)
    rf.fit(x_train, y_train)
    y_pred = rf.predict(x_test)
    print("Random Forest Classifier Results\n" + "-" * 50 + "\n")
    print('Accuracy of Random Forest Classifier: {:.4F} \n'.format(metrics.accuracy_score(y_test, y_pred) * 100))
    print('Confusion Matrix (Random Forest Classifier): \n', metrics.confusion_matrix(y_test, y_pred))
    print('Area under curve (Random Forest Classifier): {:.4F} \n'.format(metrics.roc_auc_score(y_test, y_pred)))
    print(metrics.classification_report(y_test, y_pred))
    print("-" * 50 + "\n")
    return {'model': rf, 'x_train': x_train, 'x_test': x_test, 'y_train': y_train, 'y_test': y_test, 'y_pred': y_pred}