#Reference: https://interviewing.io/recordings/Java-Google-16/


'''
Max Heap:
The number on the top is the highest.
     5
   2      1
0    1


Given 2 heap structures:
   5            3
2    1       1     1

Resulting Heap structure:

     5
   2   3
1
'''


'''
Let's try a general version of Max Heap Program:
Input List: [1,3,5,4,6,13,10,9,8,15,17]

Corresponding Binary Tree:
           1
         /   \
        3     5
      /  \   /  \
     4   6  13   10
   /  \ /  \
  9  8  15  17

 The task is to build a Max-Heap from above array.

 Total Nodes = 11
 Last Non-leaf node index = (11/2) -1 = 4

 To build the heap, heapify the nodes:
 [1,3,5,4,6] in reverse order.

swap(6,17)
swap(4,9)
swap(13,5)
swap(3,17), swap(3,15)
swap(1,17), swap(1,15), swap(1,6)
'''

'''
How to build the binaryTree:
'''

class MaxHeap:
    def sort(self,list):
        return sorted(list)

    def list2BinaryTree(self,list):
        '''
        Canonical Datastructure for Tree:
        {1:[children],2:[children],3:[multiple children]}
        '''
        tree = {}

        return binaryTree


if __name__ == "__main__":
    list = [1,3,5,4,6,13,10,9,8,15,17]
    currentHeap = MaxHeap()
    sortedlist = currentHeap.sort(list)
    print ('sorted list',sortedlist)

    print ('corresponding Tree',)
