from sklearn import model_selection
from transformer import get_rawX_y, Transformer
from feature_engine import encoding, imputation
from sklearn import pipeline
from sklearn.preprocessing import StandardScaler

def do_pipeline():
    ## Create a pipeline
    kag_pl = pipeline.Pipeline(
        [('clean', Transformer()),
        # ('preprocess_num', StandardScaler(), ['numeric_col_1', 'numeric_col_2']),  # Preprocess non-categorical columns

        ('cat', encoding.OneHotEncoder(top_categories = 5,
                                    drop_last = True,
                                    variables=['Q1', 'Q3', 'major']
                                    )),
        ('num_inputs', imputation.MeanMedianImputer(imputation_method = 'median', variables = ['education', 'years_exp']))]
        )

    return kag_pl

def split_data (raw, ycol): 
    set_X, set_y = get_rawX_y(df=raw, y_col=ycol)
    kag_pl = do_pipeline()
    set_train_X, set_test_X, set_train_y, set_test_y = model_selection.train_test_split(
        set_X,
        set_y,
        test_size=0.3,
        random_state=42,
        stratify=set_y)

    X_train = kag_pl.fit_transform(set_train_X, set_train_y)
    X_test = kag_pl.transform(set_test_X)

    return X_train
