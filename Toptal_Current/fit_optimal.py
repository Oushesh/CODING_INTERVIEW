#fit
'''
mse =1/n*sum/(Pi-Ei)**2

Part 1:
'''

import numpy as np

candidates = [[1,0],[2,1],[0.5,1],[1.01,0],[1,0.1]]
points = [[0,0],[1,1],[1.9,2],[3,3.2],[4,4.1],[5,5.1]]

def square_err(points):
  Pi=points[0]
  Ei=points[1]
  return (Pi-Ei)**2

def mse(points):
	return sum(list(map(square_err,points)))/len(points)

print ('The mean square error is:',mse(points))


'''
Part 2:
Find the best fit canadiates for the points given.

1. Each candidate in candidates is a line.
2. For each candidate find the mse
3. Collect a list of MSEs then get the index at the minimum
4. Use the index to query the right candidate
'''

#How to use the mse function
#y=mx+c
def mse_line(points,candidate):
	estimated_y = [(lambda point : point*candidate[0]+candidate[1])(point) for point in points]
	#errors = [(lambda candidate: fit_line(points,candidate))(candidate) for candidate in candidates]

	predicted_y = [point[1] for point in points]

	#Find the minimum index where the minimum error occurs:
	return mse(zip(predicted_y,estimated_y))

def best_line(points,candidates):
	min_err = float('inf')
	min_idx = 0
	for i in range(len(candidates)):
		current_err=mse_line(points,candidates[i])
		if current_err<min_err:
			min_err = current_err
			min_idx=i
	return candidates[min_idx]

print ('The best line is:',best_line(points,candidates))


