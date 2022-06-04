from dis import pretty_flags
# from itertools import Predicate
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import math

# for equation y = mx + b 
# the cost function use in this function is from the coursera course
def gradient_descent(x,y,iterations):
    m_curr = b_curr = 0
    learning_rate = 0.0002
    m = len(x)
    for a in range(iterations):
        y_predicted = m_curr*x + b_curr
        cost_function = (1/(2*m))*sum([val**2 for val in y-y_predicted])
        # print(cost_function)
        bd = -(1/m)*sum(y-y_predicted)
        md = -(1/m)*sum(x*(y-y_predicted))
        b_curr = b_curr - learning_rate * bd
        m_curr = m_curr - learning_rate * md
        print(f" m {m_curr} , b {b_curr} , iterations {iterations} , cost {cost_function}")

# for equation y = mx + b 
# the cost function use in this function is from the ml course by codebasics from yt
def gradient_descent_2(x,y,iterations):
    # here the equation is y=mx+b *[b is like theta0]
    m_curr = b_curr = 0 
    n = len(x)
    learning_rate = 0.0002
    cost_previous = 0
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n)*sum([value**2 for value in y-y_predicted])
        print(cost)
        # md is derivative of the cost function
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous = cost
        print(f" m {m_curr} , b {b_curr} , iterations {iterations} , cost {cost}")
df = pd.read_csv("test_scores.csv")
# print(df)

# REMINDER !!!!
x = np.array(df["math"])
y = np.array(df["cs"])
# don't use np.array([df["math"]]) cause it will create something else and the ans will also be different

# gradient_descent_2(x,y,100)
gradient_descent(x,y,1000)
print(x,y)