"""Uses Support Vector Machine to classify data as AF vs Non-AF"""
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics

def svm(X, y, kernel='linear'):
    """Uses Support Vector Machine to classify data as AF vs Non-AF"""
    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)
    # Use SVM to predict the outcome
    print(f"Training Support Vector Machine with {kernel}...\n")
    svm = SVC(kernel=kernel, random_state=101)
    svm.fit(x_train, y_train)
    y_pred = svm.predict(x_test)
    print("Support Vector Machine Results\n" + "-" * 50 + "\n")
    print('Accuracy of SVM: {:.4F} \n'.format(metrics.accuracy_score(y_test, y_pred) * 100))
    print('Confusion Matrix (SVM): \n', metrics.confusion_matrix(y_test, y_pred))
    print('Area under curve (SVM): {:.4F} \n'.format(metrics.roc_auc_score(y_test, y_pred)))
    print(metrics.classification_report(y_test, y_pred))
    print("-" * 50 + "\n")
    return {'model': svm, 'x_train': x_train, 'x_test': x_test, 'y_train': y_train, 'y_test': y_test, 'y_pred': y_pred}
