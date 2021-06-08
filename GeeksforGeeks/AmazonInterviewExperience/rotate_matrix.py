'''
Rotate Matrix:
Input:
1 2 3
4 5 6
7 8 9

Output:
3 6 9
2 5 8
1 4 7

Idea 1:
Center:
Remains the same.

Up --> Left
Down --> Right
Left --> Down
Right --> Down

INterviewer may ask me:
How do we extend this concept:

1  2   3  4
5  6   7  8
9 10  11 12
13 14 15 16

The above proposed idea would not be extended to what I said:
So instead we use a different approach:

Approach 2:
Take an entire row and rotate it
matrix[x][y]=matrix[y][x]; x=0

--> matrix[0][y]=matrix[y][0] ---> 0,1--> len(matrix)-1,0
    matrix[][]= matrix[][] --->

Now the next problem comes:
When I loop classical I cannot access both the elements:
and because I cannot create a new matrix I need to change the looping
technique.

1 2 3 4 --> [(0,0), (0,1), (0,2), (0,3)]
4       --> [(),
3
2
1    -- >


Really Hard if no new matrix can be created
'''

class Matrix:
    def inverted(self,vector):
        return [vector[len(vector)-1-i] for i in range(len(vector))]

    def anticlockwise(self,matrix):
        # square matrix
        assert (len(matrix)==len(matrix[0])) # square matrix contradiction
        assert (len(matrix)>0) # otherwise matrix does not exist
        assert (len(matrix[0])>1)  # otherwise matrix might be single element

        for i in range(len(matrix)):
            row_1 = matrix[i]
            inverted_1 = self.inverted(row_1)
            column_1 = [matrix[j][i] for j in range(len(matrix))]
            print ('column',column_1)

            for j in range(len(inverted_1)):
                matrix[j][i]=inverted_1[j]

                print ('matrix after inversion',matrix[j][i])

            #Until here its good.
            row_2 = column_1
            temp =  matrix[len(matrix)-1-i]
            print ('temp',temp)
            matrix[len(matrix)-1-i] = row_2
            print ('row_2',matrix[len(matrix)-1-i])

            matrix[len(matrix)-1-i] = column_1
            inverted_2 = self.inverted(row_2)

            column_2 = [matrix[j][len(matrix)-1-i] for j in range(len(matrix))]

            #swap inverted_2 with column_2
            for j in range(len(inverted_2)):
                matrix[j][len(matrix)-1-i] = inverted_2[j]


            matrix[i] = column_2
            matrix[i] = self.inverted(matrix[i])
        return matrix

    def anticlockwise_extra_space(self,matrix):

        return matrix


if __name__ == "__main__":
    #List of lists
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]

    current_matrix = Matrix()
    print ('The rotated matrix is:',current_matrix.anticlockwise(matrix))


#TODebug here:Oushesh TODEbug