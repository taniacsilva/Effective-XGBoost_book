import xgboost as xgb
import pandas as pd
from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()

class XGBoostModel:

    def __init__(self) -> None:
        pass

    
    def train(X_train: pd.DataFrame, y_train: pd.DataFrame) -> xgb.XGBClassifier:
        """
        This function fits the model

        Args:
            X_train: DataFrame that contains train data (does not include label column)
            y_train: DataFrame that contains the objective variable in train data

        Returns:
            xgboost_model: XGBClassifier
        """

        y_train = label_encoder.fit_transform(y_train)

        xgboost_model = xgb.XGBClassifier(n_estimators=1, max_depth=1)
        xgboost_model.fit(X_train, y_train)

        return xgboost_model
    
    def evaluation(X_test: pd.DataFrame, y_test: pd.DataFrame, model: xgb.XGBClassifier):    
        """
        This function evaluates the model using unseen data

        Args:
            X_test: DataFrame that contains test data (does not include label column)
            Y_test: DataFrame that contains the objective variable in test data
            model: XGBoost model

        Returns:
            acc_score: Integer that represents the accuracy of the model
        """
        y_test = label_encoder.transform(y_test)

        score = model.score(X_test, y_test)

        return score