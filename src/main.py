"""Main module that loads the pre-processed data after relevant metadata is extracted from it and
performs classification on the data through various classifiers."""
import load_data
import decision_tree
import visualize
import svm
import random_forest
import knn

af_data = load_data.gen_metadata()
# Split data into X and y
X = af_data.drop(['Control'], axis=1)
y = af_data['Control']

# # Decision Tree Classifier
# dt_results = decision_tree.decision_tree(X, y)
# # Visualize results
# visualize.visualize_results(dt_results, "decision_tree")

# # KNN Classifier
# knn.knn(X, y)
# # Visualize results
# #visualize.visualize_results(knn_results, "knn")

# # Random Forest Classifier
# rf_results = random_forest.random_forest(X, y)
# # Visualize results
# visualize.visualize_results(rf_results, "random_forest")

# nonlinear_svm_results = svm.svm(X, y, kernel='rbf')
# visualize.visualize_results(nonlinear_svm_results, "nonlinear_svm")

# # Support Vector Machine
# svm_results = svm.svm(X, y)
# # Visualize results
# visualize.visualize_results(svm_results, "linear_svm")