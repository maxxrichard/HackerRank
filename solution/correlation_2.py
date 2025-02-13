# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


#Defining empty lists
X_train = list()
y_train = list()
X_test = list()

#Training data
features, rows = map(int,input().split())

for i in range(rows):
  x = list(map(float,input().split()))
  X_train.append(x[0:-1])
  y_train.append(x[-1])

# Testing data
rows = list(map(int,input().split()))
for i in range (rows[0]):
  x = list(map(float,input().split()))
  X_test.append(x)

#Model training & evaluation
model = LinearRegression().fit(X_train, y_train)
predictions = model.predict(X_test)

# Printing results
for i in range(len(predictions)):
  print(predictions[i])
