"""Visualization module used to visualize the results of various classifiers."""
import os
from sklearn import metrics
import  scikitplot as skplt
import matplotlib.pyplot as plt

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
images_path = os.path.join(parent_dir, 'images')

def svm_feature_importance(coef, names, fig_path, plot_title):
    """Visualize the feature importance of the SVM classifier."""
    imp = coef
    imp,names = zip(*sorted(zip(imp,names)))
    # Plot the feature importance
    plt.barh(range(len(names)), imp, align='center')
    plt.yticks(range(len(names)), names)
    plt.title(f'{plot_title} Feature Importance')
    plt.savefig(os.path.join(fig_path, 'feature_importance.png'))


def visualize_results(results, classifier_name):
    """Visualize ROC Curve, Confusion Matrix, Classification Report and Feature Importance."""
    feature_names = results['x_train'].columns.tolist()
    # Derive plot titles from classifier name. Make first letter uppercase and replace underscores with spaces
    plot_title = classifier_name.title().replace('_', ' ')
    # Join classifier_name with images_path
    fig_path = os.path.join(images_path, classifier_name)
    # Create directory if it doesn't exist
    if not os.path.exists(fig_path):
        os.makedirs(fig_path)
    # Feature Importance
    # If Classifier name has svm, use a different method to visualize feature importance
    if 'linear_svm' == classifier_name:
        svm_feature_importance(results['model'].coef_[0], feature_names, fig_path, plot_title)
    elif 'decision_tree' in classifier_name:
        skplt.estimators.plot_feature_importances(results['model'], feature_names=results['x_train'].columns, figsize=(14,6))
        plt.title(f'{plot_title} Feature Importance')
        plt.savefig(os.path.join(fig_path, 'feature_importance.png'))
    # ROC Curve
    roc_curve = metrics.RocCurveDisplay.from_predictions(results['y_test'], results['y_pred'])
    roc_curve.plot()
    plt.title(f'{plot_title} ROC Curve')
    plt.savefig(os.path.join(fig_path, 'roc_curve.png'))
    # Confusion Matrix
    skplt.metrics.plot_confusion_matrix(results['y_test'], results['y_pred'])
    plt.title(f'{plot_title} Confusion Matrix')
    plt.savefig(os.path.join(fig_path, 'confusion_matrix.png'))
    # Plot Precision-Recall Curve
    precision, recall, _ = metrics.precision_recall_curve(results['y_test'], results['y_pred'])
    precision_recall_display = metrics.PrecisionRecallDisplay(precision, recall)
    precision_recall_display.plot()
    plt.title(f'{plot_title} Precision-Recall Curve')
    plt.savefig(os.path.join(fig_path, 'precision_recall_curve.png'))
