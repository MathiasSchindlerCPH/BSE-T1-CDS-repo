# Dependencies
import pandas as pd
import sklearn

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

class Model:
    def __init__(self, feat_cols: pd.DataFrame, targ_col: pd.Series):
        self.feat_cols = feat_cols
        self.targ_col = targ_col
    
    def train(self, alpha, regularization):
        self.C = alpha
        self.regularization = regularization
        regr = LogisticRegression(C = self.C, penalty=self.regularization)
        self.fitted = regr.fit(self.feat_cols, self.targ_col)
        
    def predict(self, predict_data: pd.DataFrame):
        self.predict_data = predict_data
        self.predict_proba = self.fitted.predict_proba(self.predict_data)
        self.predict_ = self.fitted.predict(self.predict_data)
        return self.predict_proba, self.predict_

# i) Metric scores
def asses(y_true, y_predict):
    print(roc_auc_score(y_true, y_predict))