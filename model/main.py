"""This is the main module of this exercise"""
from load_data import extract_zip
from utils import split_data
from decision_tree import save_tree_plot, decision_tree_train, evaluation
from xgboost_model import XGBoostModel
from dummy_model import DummyClassifier



url = 'https://github.com/mattharrison/datasets/raw/master/data/kaggle-survey-2018.zip'
filename = 'kaggle-survey-2018.zip'
member_name = 'multipleChoiceResponses.csv'

def main():
    """
    This is the main function
    """
    raw = extract_zip(url, filename, member_name)
    X_train, y_train, X_test, y_test = split_data(raw = raw, ycol = 'Q6')
    model = decision_tree_train(X_train=X_train, y_train=y_train)
    tree_plot = save_tree_plot(X_train = X_train, model = model)
    score_decision_tree = evaluation(X_test=X_test, y_test=y_test, model=model)

    dummy_model = DummyClassifier.train(X_train=X_train, y_train=y_train)
    score = DummyClassifier.evaluation(X_test=X_test, y_test=y_test, model=dummy_model)
    xgboost_model = XGBoostModel.train(X_train=X_train, y_train=y_train)
    score_xgboost = XGBoostModel.evaluation(X_test=X_test, y_test=y_test, model=xgboost_model)

    print(tree_plot)
    print(score_decision_tree)
    print(score)
    print(score_xgboost)

if __name__ == '__main__':
    main()
