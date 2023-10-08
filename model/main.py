"""This is the main module of this exercise"""
from load_data import extract_zip
from utils import split_data
from decision_tree import save_tree_plot

url = 'https://github.com/mattharrison/datasets/raw/master/data/kaggle-survey-2018.zip'
filename = 'kaggle-survey-2018.zip'
member_name = 'multipleChoiceResponses.csv'

def main():
    """
    This is the main function
    """
    raw = extract_zip(url, filename, member_name)
    X_train, y_train = split_data(raw = raw, ycol = 'Q6')
    tree_plot = save_tree_plot(X_train=X_train, y_train=y_train)
    print(tree_plot)


if __name__ == '__main__':
    main()
