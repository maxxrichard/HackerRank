# Enter your code here. Read input from STDIN. Print output to STDOUT

#importing libraries
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

#initializing empty lists
X_train = list()
y_train = list()
X_test = list()

#input training data
features, train_rows = map(int,input().split()) 
for _ in range(train_rows):
    a = list(map(float,input().split()))
    X_train.append(a[0:features])
    y_train.append(a[features])
    #print(a[features])

#input testing data
test_rows = int(input())
for _ in range(test_rows):
    a = list(map(float,input().split()))
    X_test.append(a)

#fit polynomial model
poly = PolynomialFeatures(degree=3)
poly_features_train = poly.fit_transform(X_train)
poly_features_test = poly.fit_transform(X_test)

#fit linear regression model
model = LinearRegression().fit(poly_features_train, y_train)
y_pred = model.predict(poly_features_test)

#print the predictions
for i in y_pred:
    print(round(i,2))