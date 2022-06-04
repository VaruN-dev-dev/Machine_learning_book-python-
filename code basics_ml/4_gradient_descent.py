import numpy as np
def gradient_descent(x,y):
    # here the equation is y=mx+b *[b is like theta0]
    m_curr = b_curr = 0 
    itertations = 100
    n = len(x)
    learning_rate = 0.001
    for i in range(itertations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n)*sum([value**2 for value in y-y_predicted])
        print(cost)
        # md is derivative of the cost function
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print(f" m {m_curr} , b {b_curr} , iterations {itertations} , cost {cost}")
        

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
print(x,y)
gradient_descent(x,y)