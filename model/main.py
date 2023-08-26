"""This is the main module of this exercise"""
from load_data import extract_zip
from cleaning import clean, topn

url = 'https://github.com/mattharrison/datasets/raw/master/data/kaggle-survey-2018.zip'
filename = 'kaggle-survey-2018.zip'
member_name = 'multipleChoiceResponses.csv'

def main():
    """
    This is the main function
    """
    raw = extract_zip(url, filename, member_name)

    cleaned_data = clean(df_ = raw)

    top_n = topn(ser = cleaned_data)
  
if __name__ == '__main__':
    main()
