import pandas as pd

def tweak_kag(df_: pd.DataFrame) -> pd.DataFrame:
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
    return (df_.assign(age = df_.Q2.str.slice(0, 2).astype(int), 
                       education = df_.Q4.replace({'Master´s degree': 18,
                                                  'Bachelor´s Degree': 16,
                                                  'Some college/university study without earning a bachelor´s degree': 20,
                                                  'Professional Degree': 19,
                                                  'I prefer not to answer': None, 
                                                  'No formal education past high school': 12}), 
                                                  major = (df_.Q5.pipe(topn, n=3)
                                                  .replace({'Computer science (software engineering, etc,)': 'cs',
                                                            'Engineering (non-computer focused)': 'eng', 
                                                            'Mathematics or statistics': 'stat'})
                                                  ),
                                                  year_exp = (df_.Q8.str.replace('+', '', regex = False)
                                                                .str.split('-', expand=True)
                                                                .iloc[:,0]
                                                                .astype(float)), 
                                                  compensation = (df_.Q9.str.replace('+', '', regex= False)
                                                                  .str.replace(',', '', regex=False)
                                                                  .str.replace('500000', '500', regex = False)
                                                                  .str.replace('I do not wish to disclose my approximate yearly compensation', '0', regex = False)
                                                                  .str.split('-', expand = True)
                                                                  .iloc[:,0]
                                                                  .fillna(0)
                                                                  .astype(int)
                                                                  .null(1_000)
                                                  ),
                                                  python =  df_.Q16_Part_1.fillna(0).replace('Python', 1),
                                                  r = df_.Q16_Part_2.fillna(0).replace('R', 1),
                                                  sql = df_.Q16_Part_3.fillna(0).replace('SQL', 1)
    ) #assign
    .rename(columns=lambda col:col.replace(' ', '_'))
    .loc[:, 'Q1,Q3,age,education,major,years_exp,compensation'
         'python,r,sql'.split(',')]~
         )