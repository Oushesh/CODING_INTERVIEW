import numpy as np


'''
Function:
returns mse: mean squared error
'''
def Compare(predicted,expected):
    '''
    predicted: list
    expected: list
    '''
    #edge case: test len(predcited) same as expected
    assert(len(predicted)==len(expected))
    total=sum([(i-j)**2 for i in predicted for j in expected])
    mse = total/len(predicted)
    return mse

#Input: 2D points
#linear model: y= mx+b
#points:
# ()

def fit(points,candidates):
    #1. Plug x from points into y=mx+b
    #2. For each one get the y ouput.
    #list:erros --> plug this as input into
    #compare
    #Define output
    for m,b in candidates:
        for j in points:
            y_expected =m*j[0]+b
            output.append(y_expcted)
    y_expcted =[i[0] for in points]
    mse = Compare(y_predicted,output)
    return mse



###TO Do numberic Computations fast in an interview I will use the map reduce functionality of python.


if __name__ == "__main__":

    points = [[0, 0], [1, 1], [1.9, 2], [3, 3.2], [4, 4.1], [5, 5.11]]
    candidates = [[1, 0], [2, 1], [0.5, 1], [1.01, 0], [1, 0.1]]

    print ('The mse error is:',fit(points,candidates))

#TODO: Kill the intervier: COuld have used: map(function,inputs) formulation
