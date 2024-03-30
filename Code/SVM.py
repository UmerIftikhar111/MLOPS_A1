import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.metrics import confusion_matrix, classification_report , accuracy_score
from sklearn.model_selection import train_test_split
import joblib


df=pd.read_csv("E:/MLOPS Assignment 1/Dataset/data.csv")

# split dataframe into X and y
X = df.drop('price_range', axis=1)
y = df['price_range']

# split dataframe into train and test
X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.15, random_state=42)

svc = svm.SVC(kernel='linear')
svc.fit(X_train, y_train)

svc_pred = svc.predict(X_test)
print('accuracy: ', accuracy_score(y_test , svc_pred))

print(classification_report(y_test , svc_pred))

# save the trained model to a file
joblib.dump(svc, 'E:/MLOPS Assignment 1/svm_model.joblib')

