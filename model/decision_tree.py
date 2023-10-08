import pandas as pd
from sklearn import tree
from utils import do_pipeline
import matplotlib.pyplot as plt

def decision_tree_train(X_train: pd.DataFrame, y_train: pd.DataFrame):
    """
    Train the decision tree
    Args:
        X_train: DataFrame that contains train data
        y_train: DataFrame that contains the objective variable for the train set
    """
    stump_dt = tree.DecisionTreeClassifier(max_depth=1)
    kag_pl = do_pipeline()
    X_train = kag_pl.fit_transform(X_train)
    stump_dt.fit(X_train, y_train)

    return stump_dt

def save_tree_plot(X_train: pd.DataFrame, y_train: pd.DataFrame):
    """
    Save the tree plot
    Args:
        X_train: DataFrame that contains train data
        y_train: DataFrame that contains the objective variable for the train set
    """
    fig, ax = plt.subplots(figsize=(8, 4))
    features = list(c for c in X_train.columns)
    stump_dt = decision_tree_train(X_train=X_train, y_train=y_train)
    plot = tree.plot_tree(stump_dt,
                   feature_names=features,
                   filled=True,
                   class_names=stump_dt.classes_,
                   ax=ax)
    return plot