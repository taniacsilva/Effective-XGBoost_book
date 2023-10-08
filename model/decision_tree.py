import pandas as pd
from sklearn import tree
from utils import do_pipeline
import matplotlib.pyplot as plt

kag_pl = do_pipeline()

def decision_tree_train(X_train: pd.DataFrame, y_train: pd.DataFrame):
    """
    Train the decision tree
    Args:
        X_train: DataFrame that contains train data
        y_train: DataFrame that contains the objective variable for the train set
    """
    stump_dt = tree.DecisionTreeClassifier(max_depth=1)
    stump_dt.fit(X_train, y_train)

    return stump_dt

def evaluation(X_test: pd.DataFrame, y_test: pd.DataFrame, model: tree.DecisionTreeClassifier):
    """
    This function evaluates the model using unseen data

    Args:
        X_test: DataFrame that contains test data (does not include label column)
        Y_test: DataFrame that contains the objective variable in test data
        model: Decision Tree model

    Returns:
        acc_score: Integer that represents the accuracy of the model
    """
    score = model.score(X_test, y_test)

    return score

def save_tree_plot(X_train: pd.DataFrame, model: tree.DecisionTreeClassifier):
    """
    Save the tree plot
    Args:
        X_train: DataFrame that contains train data
        model: Decision Tree model
    """
    fig, ax = plt.subplots(figsize=(8, 4))
    features = list(c for c in X_train.columns)
    plot = tree.plot_tree(model,
                   feature_names=features,
                   filled=True,
                   class_names=model.classes_,
                   ax=ax)
    
    return plot