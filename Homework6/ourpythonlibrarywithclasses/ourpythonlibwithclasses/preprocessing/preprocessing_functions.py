# Dependencies
import pandas as pd
import sklearn

from abc import ABC, abstractmethod
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures


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