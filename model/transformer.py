from sklearn import base

from cleaning import clean

class Transformer(base.BaseEstimator, base.TransformerMixin):
    """ 
    Represents the transformer for Kaggle Survey Data
    This transformer takes a Pandas DataFrame containing Kaggle\
    survey data as input and returns a new version of the Dataframe.\
    The modifications include extracting and transforming certain columns,\
    renaming columns, and selecting a subset of columns

    Args:
        ycol(str, optional): The name of the column to be used as the target\
        variable. If not specified the target variable will not be specified
    """
    def __init__(self, ycol=None):
        self.ycol = ycol

    def transform(self, X):
        return clean(X)

    def fit(self, X, y=None):
        return self


def get_rawX_y(df, y_col):
    """ 
    Obtain the set used for the objective variable and set will all independent variables

    Args:
        df (pandas DataFrame): DataFrame with the data
        y_col (str): String that indicates which is the target variable 
    """
    # Raise error if DataFrame does not contains the columns Q3 and Q6
    if 'Q3' not in df.columns or 'Q6' not in df.columns:
        raise ValueError("The DataFrame does not contain the necessary columns (Q3 and Q6).")
    
    raw = df[(df['Q3'].isin(["United States of America", "China", "India"])) &
             (df['Q6'].isin(["Data Scientist", "Software Engineer"]))]
    
    return raw.drop(columns=[y_col]), raw[y_col]

        