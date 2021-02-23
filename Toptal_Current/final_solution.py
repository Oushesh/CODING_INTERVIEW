#final_solution

'''
MSE = 1/n*SUM(Pi-Ei)**2

First approach is with numpy
Second approach without: let's
use map reduce criteria from
Python. list(map(function,input))
'''

import numpy as np

#Approach 1:
def function(input):
  Pi=input[0]
  Ei=input[1]
  return (Pi-Ei)**2
#function works on individual parts,
#points is a vector --> list
points = [[0,0],[1,1],[1.9,2],[3,3.2],[4,4.1],[5,5.1]]

mse=sum(list(map(function,points)))/len(points)

print (mse)
#First part is done:

#The second is canadiates.
#y = mx + c
#m,c  in candidates

#Feed in the X values
# y = mx +c, y=x --> Feed (x)-> get (y)
#Compute the error
#list of true_y
#list of predicted_
#Numerical Programming at Toptal always. And the question is what he asked in the first part.

candidates = [[1,0],[2,1],[0.5,1],[1.01,0],[1,0.1]]
def function_mse(combined_y):
  Given_Y=combined_y[0]
  True_Y=combined_y[1]

  return (Given_Y-True_Y)**2


def fit_line(points,candiate):
  Xs = [point[0] for point in points]
  #Calculate the
  True_Ys = [(lambda x:candiate[0]*x+candiate[1])(x) for x in Xs]

  #True Ys
  #Given Ys
  Given_Ys = [point[1] for point in points]
  #Combine Given_Ys and True_Ys
  combined_ys = [(Given_Y,True_Y) for Given_Y,True_Y in zip(Given_Ys,True_Ys)]


  #caluclate error.
  error = sum(list(map(function_mse,combined_ys)))/len(combined_ys)
  return error

candidate = [2,1]
error = print(fit_line(points,candidate))

#Build an error list
errors = [(lambda candidate: fit_line(points,candidate))(candidate) for candidate in candidates]

print (errors)

print (min(errors))

#Get index of the where the minimum occurs
index = 0
for i in range(len(errors)):
  if errors[i] == min(errors):
    index=i

print (index)

print ('The best function is:',candidates[index])
#https://stackoverflow.com/questions/6076270/lambda-function-in-list-comprehensions


