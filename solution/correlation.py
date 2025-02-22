# Enter your code here. Read input from STDIN. Print output to STDOUT

#import libraries
import math

#define sum function
def summation(x):
    a = 0
    for i in x: a += i
    return a

#define multiply function
def multiply(x,y):
    mul = list()
    for i in range(len(x)): mul.append(x[i]*y[i])
    return mul

#define coefficient function
def coeff(x, y, n):
    xy_sum = summation(multiply(x,y))
    x_sum = summation(x)
    y_sum = summation(y)
    x2_sum = summation(multiply(x,x))
    y2_sum = summation(multiply(y,y))
    
    r = (n*xy_sum - x_sum*y_sum)/(math.sqrt(n*x2_sum - x_sum*x_sum)*math.sqrt(n*y2_sum - y_sum*y_sum))
    return r

#define empty lists & input the size
m = list()
p = list()
c = list()
n = int(input().strip())

#input the data
for i in range(n):
    a = list(map(int,input().split()))
    m.append(a[0])
    p.append(a[1])
    c.append(a[2])
    
#print the coefficients
print(round(coeff(m,p,n),2))
print(round(coeff(p,c,n),2))
print(round(coeff(c,m,n),2))
