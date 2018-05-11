import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import (CountVectorizer, TfidfTransformer)
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import (confusion_matrix, classification_report, accuracy_score)
from sklearn.calibration import (calibration_curve, CalibratedClassifierCV)

filename = "D:\\Stanford\\TA\\new_dataset.xlsx"

df = (pd.ExcelFile(filename)).parse(sheet_name='Sheet1')

y = df.Label
X = df.drop('Label', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True)

print(X_train.head())
print(X_train.shape)

print(X_test.head())
print(X_test.shape)






