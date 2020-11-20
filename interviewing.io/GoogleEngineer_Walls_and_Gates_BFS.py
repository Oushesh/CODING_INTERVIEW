class Solution():
    def wallsAndGates(self, rooms):
        """
        input: List[int][int]
        rtype: List[int][int]
        """
        if len(rooms) == 0:
            return rooms

        #add all gates to a queue
        queue = []
        for i in range( len(rooms) ):
            for j in range( len(rooms[0]) ):
                if rooms[i][j] == 0:
                	queue.append((i,j))
        while queue:
            row, col = queue.pop()
            if row > 0 and rooms[row-1][col] == float("Inf"):
                rooms[row-1][col] = rooms[row][col] + 1
                queue = [(row-1, col)] + queue
            if row < len(rooms)-1 and rooms[row+1][col] == float("Inf"):
                rooms[row+1][col] = rooms[row][col] + 1
                queue = [(row+1, col)] + queue
            if col > 0 and rooms[row][col-1] == float("Inf"):
                rooms[row][col-1] = rooms[row][col] + 1
                queue = [(row, col-1)] + queue
            if col < len(rooms[0])-1 and rooms[row][col+1] == float("Inf"):
                rooms[row][col+1] = rooms[row][col] + 1
                queue = [(row, col+1)] + queue

rooms = [
         [float("Inf"),  -1 , 0 , float("Inf")],
		 [float("Inf"), float("Inf") ,float("Inf"),  -1],
		 [float("Inf"),  -1 ,float("Inf"),  -1],
  		 [0,  -1, float("Inf"), float("Inf")]
         ]

test = Solution()
test.wallsAndGates(rooms)
print (rooms)
