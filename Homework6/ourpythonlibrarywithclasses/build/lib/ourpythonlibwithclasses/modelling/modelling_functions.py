# Dependencies
import pandas as pd
import sklearn

from sklearn.linear_model import LinearRegression


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