import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report , accuracy_score
from sklearn.model_selection import train_test_split

df=pd.read_csv("E:/MLOPS Assignment 1/Dataset/data.csv")

# split dataframe into X and y
X = df.drop('price_range', axis=1)
y = df['price_range']

# split dataframe into train and test
X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.15, random_state=42)

# train a Random Forest

RF_model = RandomForestClassifier(n_estimators= 150)
RF_model.fit(X_train , y_train)

RF_pred = RF_model.predict(X_test)
print('acurracy : ' , accuracy_score(y_test , RF_pred))

print(classification_report(y_test , RF_pred))