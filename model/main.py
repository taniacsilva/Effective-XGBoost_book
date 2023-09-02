"""This is the main module of this exercise"""
from load_data import extract_zip
from utils import split_data

url = 'https://github.com/mattharrison/datasets/raw/master/data/kaggle-survey-2018.zip'
filename = 'kaggle-survey-2018.zip'
member_name = 'multipleChoiceResponses.csv'
csv_name = 'x_train_data.csv'
def main():
    """
    This is the main function
    """
    raw = extract_zip(url, filename, member_name)
    X_train = split_data(raw = raw, ycol = 'Q6')

    X_train.to_csv(csv_name, index=False)

if __name__ == '__main__':
    main()
