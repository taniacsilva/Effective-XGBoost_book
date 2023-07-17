from load_data import extract_zip
from cleaning import tweak_kag, topn

url = 'https://github.com/mattharrison/datasets/raw/master/data/kaggle-survey-2018.zip'
filename = 'kaggle-survey-2018.zip'
member_name = 'multipleChoiceResponses.csv'

def main():

    raw = extract_zip(url, filename, member_name)
    print(raw.info())
    
    cleaned_data = tweak_kag(df_ = raw)
    print(cleaned_data)    
    
    top_n = topn(ser = cleaned_data)

    print(top_n)
if __name__ == '__main__':
    main()