from sklearn import dummy
from utils import do_pipeline
import pandas as pd

class DummyClassifier:

    def __init__(self) -> None:
        pass

    def train(X_train: pd.DataFrame, y_train: pd.DataFrame) -> dummy.DummyClassifier:
        """
        This function fits the model

        Args:
            X_train: DataFrame that contains train data (does not include label column)
            y_train: DataFrame that contains the objective variable in train data

        Returns:
            dummy_model: DummyClassifier
        """
        dummy_model = dummy.DummyClassifier()
        dummy_model.fit(X_train, y_train)

        return dummy_model
    
    def evaluation(X_test: pd.DataFrame, y_test: pd.DataFrame, model: dummy.DummyClassifier):    
        """
        This function evaluates the model using unseen data

        Args:
            X_test: DataFrame that contains test data (does not include label column)
            Y_test: DataFrame that contains the objective variable in test data
            model: Dummy model, that predicts the most common label

        Returns:
            acc_score: Integer that represents the accuracy of the model
        """
        score = model.score(X_test, y_test)

        return score