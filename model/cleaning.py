"""This module cleans the data"""
import pandas as pd

def  clean(df_: pd.DataFrame) -> pd.DataFrame:
    """
    Tweak the Kaggle survey data and return a new DataFrame
    This function takes a pandas DataFrame containing Kaggle survey data as input
    and returns a new DataFrame. The modifications include extracting and transforming
    certain columns, renaming columns, and selecting a subset of columns
    
    Args:
        df_ (pd.DataFrame): Input dataframe containing kaggle survey data
    Returns:
        pd.DataFrame : The new data with the modified and selected columns
    """
    return (df_
            .assign(age=df_.Q2.str.slice(0,2).astype(int),
                    education=df_.Q4.replace({'Master’s degree': 18,
                            'Bachelor’s degree': 16,
                            'Doctoral degree': 20,
    'Some college/university study without earning a bachelor’s degree': 13,
                            'Professional degree': 19,
                            'I prefer not to answer': None,
                            'No formal education past high school': 12}),
                    major=(df_.Q5
                                .pipe(topn, n=3)
                                .replace({
                        'Computer science (software engineering, etc.)': 'cs',
                        'Engineering (non-computer focused)': 'eng',
                        'Mathematics or statistics': 'stat'})
                            ),
                    years_exp=(df_.Q8.str.replace('+','', regex=False)
                            .str.split('-', expand=True)
                            .iloc[:,0]
                            .astype(float)),
                    compensation=(df_.Q9.str.replace('+','', regex=False)
                            .str.replace(',','', regex=False)
                            .str.replace('500000', '500', regex=False)
    .str.replace('I do not wish to disclose my approximate yearly compensation',
                '0', regex=False)
                            .str.split('-', expand=True)
                            .iloc[:,0]
                            .fillna(0)
                            .astype(int)
                            .mul(1_000)
                                    ),
                    python=df_.Q16_Part_1.fillna(0).replace('Python', 1),
                    r=df_.Q16_Part_2.fillna(0).replace('R', 1),
                    sql=df_.Q16_Part_3.fillna(0).replace('SQL', 1)
                )#assign
        .rename(columns=lambda col:col.replace(' ', '_'))
        .loc[:, 'Q1,Q3,age,education,major,years_exp,compensation,'
                'python,r,sql'.split(',')]   
        )

def topn(ser, n=5, default='other'):
    """
    Replace all values in a Pandas Series that are not among the top 'n'
    most frequent values with a default value.
    This function takes a Pandas Series and returns a new Series with the
    values replaced as described above. The top 'n' most frequent values
    are determined using the 'value_counts' method of the input Series

    Args:
        ser (pd.Series): The input Series
        n (int): The number of most frequent values to keep. The default
        value is 5
        default (str): The default value to use for values that are not 
        among the top 'n' most frequent values. The default is 'other'.
    
    Returns:
        pd.Series: The modified series with the values replaced
    """
    counts = ser.value_counts()
    return ser.where(ser.isin(counts.index[:n]), default)
