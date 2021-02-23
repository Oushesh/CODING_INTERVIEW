'''
Ref: https://www.geeksforgeeks.org/google-interview-experience-for-sde-1/?ref=rp

(1h)

One grid is given. It contains characters in each cell.
You have to find out out the smallest hamilton distance:
| row_index_x – row_index_y | + | column_index_x – column_index_y |

(row_index_x – row_index_y) + (column_index_x – column_index_y)
[ x, 0, 0, 0 ]
[ 0, y, 0, y ]
[ x, x, 0, 0 ]
[ 0, y, 0, 0 ]

keep curr_x, curr_y
best_x, best_y
x(0,0)->(1,1)y
x(0,0)->(1,3)y

curr_x
x(2,0)
curr_x
x(2,1)
curr_y(3,1)

1. Loop through the x,y:  if x: curr_x (save it)
perform the count until I find curr_y


There is a problem with the question here:
We need to walk through the array twice here:
because of the modulus.

if array_size is nxm:
Time Complexity: O(2(nxm))

'''

def Hamlton_dis(maze):
    curr_x = 0
    curr_y = 0
    best_x = 0
    best_y = 0

    #Forward check
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y]=='x':
                if curr_x < best_x:
                    best_x = curr_x
                curr_x = x
            if maze[x][y]=='y':
                if curr_y < best_y:
                    best_y = curr_y
                curr_y = y
