# Dependencies
import numpy as np
import pandas as pd
import sklearn

from sklearn import model_selection
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# a) Load dataset
def load_dataset(path_file):
    df = pd.read_csv(path_file)
    return df

# b) Split dataset
def split(df):
    train, test = model_selection.train_test_split(df)
    return train, test


# c) Drop NA rows in 3 features
def clean_rows(df, rows: list):
   df_dropped = df.dropna(axis = 0, subset = rows)
   return df_dropped
    
    
# d) Fill NA with mean in 2 cols
def fill_na_mean(df, cols : list):
    df_filled = df[cols].fillna(df.mean())
    df = df.drop(cols, axis = 1)
    df = pd.concat([df_filled, df], axis = 1)
    return df
    

# e) Dummies for etchnicity
def one_hot(df, prfx, col):
    df = pd.get_dummies(df, prefix = prfx, columns = col)
    return df


# g & h) Train model
def fit_predict(df, target, features: list):
    x = df[features]
    y = df[target]
    y_hat = LogisticRegression().fit(x, y).predict_proba(x)
    y_hat = y_hat[:,1]
    df['predictions'] = y_hat
    return df    


# i) Metric scores
def asses(y_true, y_predict):
    print(roc_auc_score(y_true, y_predict))
