import numpy as np
#from sklearn.linear_model import LinearRegression
#Quizzes a bit quicker in this part

def linear_func_prediction(theta1, theta0, x_values):
    predictions = []
    for x in x_values:
        predictions.append(theta1*x+theta0)
    return predictions

def cost_function(real, predicted):
    m = len(real)
    if m != len(predicted):
       err= SystemError("Faulty sizes")
       print( err)
       return
    sum_cost = 0
    for i in range(0,m):
        sum_cost += (real[i] - predicted[i])**2
    real_cost = (1/(2*m))*sum_cost
    return real_cost

#print(cost_function([1,1,1.5],[0.5,2,3]))

