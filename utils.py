import pandas as pd
from numpy.typing import NDArray
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def get_metrics(y_pred : NDArray, y_test: pd.core.series.Series) -> pd.DataFrame:
    accuracy = accuracy_score(y_test,y_pred)
    recall = recall_score(y_test,y_pred, average='weighted')
    precision = precision_score(y_test,y_pred, average='weighted')
    f1_score_w = f1_score(y_test,y_pred, average='weighted')
    return [accuracy, recall, precision, f1_score_w]


