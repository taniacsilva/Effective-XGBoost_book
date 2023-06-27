from load_data import extract_zip

url = 'https://github.com/mattharrison/datasets/raw/master/data/kaggle-survey-2018.zip'
filename = 'kaggle-survey-2018.zip'
member_name = 'multipleChoiceResponses.csv'

def main():

    raw = extract_zip(url, filename, member_name)
    print(raw.info())

if __name__ == '__main__':
    main()