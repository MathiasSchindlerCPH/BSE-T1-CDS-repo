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
    def transform(self):
        return NotImplementedError

class ReScaling(Transform):
    def __init__(self, kind: str):
        self.kind = kind
    
    def transform(self, df):
        self.df = df
        if self.kind == 'min_max':
            for feature in (self.df.columns):
                self.df[feature] = (self.df[feature] - self.df[feature].min()) / (self.df[feature].max() - self.df[feature].min())
            return self.df
        elif self.kind == 'standarization':
            for feature in (self.df.columns):
                self.df[feature] = (self.df[feature] - self.df[feature].mean()) / self.df[feature].std()
            return self.df


class PolyFeatures(Transform):
    def __init__(self, n_poly_f: int):
        self.n_poly_f = n_poly_f
        
    def transform(self, df, columns:list):
        self.df = df
        self.columns = columns
        for feature in self.columns:
            for i_poly in range(2,self.n_poly_f+1):
                self.df[feature+'_poly'+str(i_poly)] = self.df[feature] ** i_poly
        return self.df