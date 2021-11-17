# Dependencies
import pandas as pd
import sklearn

from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures


class Load_Split:
    def __init__(self, path_file: str):
        self.df = pd.read_csv(path_file)
        self.train, self.test = model_selection.train_test_split(self.df, test_size=0.5)
        

class PreProcessor:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
    def clean_rows(self, rows: list):
        self.cleaned = self.df.dropna(axis = 0, subset = rows)
    
    def fill_na_mean(self, cols: list):
        self.filled = self.df[cols].fillna(self.df.mean())
        self.except_filledcols = self.df.drop(cols, axis = 1)
        self.filled = pd.concat([self.filled, self.except_filledcols], axis = 1)


class Transform(ABC):
    @abstractmethod
    def feat_standardize(self):
        pass
    
    @abstractmethod
    def feat_poly(self):
        pass
    
    
class Standardize(Transform):
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def feat_standardize(self):
        scl = StandardScaler()
        self.scaled = scl.fit_transform(self.df)
        self.scaled = pd.DataFrame(self.scaled, columns = self.df.columns, index = self.df.index)
    
    def feat_poly(self):
        poly = PolynomialFeatures(2)
        self.polynized = poly.fit_transform(self.df)
        poly_cols = poly.get_feature_names_out(self.df.columns)
        self.polynized = pd.DataFrame(self.polynized, columns = poly_cols, index = self.df.index)
    

class Model:
    def __init__(self, feat_cols: pd.DataFrame, targ_col: pd.Series):
        self.feat_cols = feat_cols
        self.targ_col = targ_col
    
    def train(self):
        regr = LinearRegression()
        self.fitted = regr.fit(self.feat_cols, self.targ_col)
        
    def predict(self):
        self.predict = self.fitted.predict(self.feat_cols)
        print(self.predict)
    

