# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as numpy
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import re


X_train = list()
y_train = list()
X_test = list()
test_user = list()

#Training data
rows, features = map(int,input().split())

for _ in range(rows):
    x = list(map(str,input().split()))
    for i in range(2, len(x)):
        x[i] = float(re.sub(r'[*:]','',x[i]))
    X_train.append(x[2:])
    y_train.append(int(x[1]))


#Testing data
testing_rows = int(input())

for _ in range(testing_rows):
    x = list(map(str,input().split()))
    for i in range(1, len(x)):
        x[i] = float(re.sub(r'[*:]','',x[i]))
    X_test.append(x[1:])
    test_user.append(x[0])


model = RandomForestClassifier().fit(X_train, y_train)
predictions = model.predict(X_test)


for i in range(testing_rows):
    if predictions[i] == 1: a = '+1'
    else: a = '-1'    
    print(test_user[i],a)

