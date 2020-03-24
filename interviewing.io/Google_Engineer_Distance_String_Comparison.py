#Reference: https://www.youtube.com/watch?v=wyu6VRmtCmE&t=170s

'''
function takes in 2strings and says whether they are equal
'''


'''
Time and Space Complexity: Space: O(n) space complexity, O(n) time
'''

'''
Most of the time s1 not equal to s2. So lets compare elementwise.
Its the same.
'''

'''
Return true if they are the same and upto max of edit distance is
1.
We need to define what is the edit distance. --> Each time they are different
we can update the distance by 1 up. dist+=1
'''

'''
Edit Distance toleration to more than 1:
Build a distance matrix between the characters
   a b c d
a  0 1 1 1
y  1 1 1 1
c  1 1 0 1
d  1 1 1 0

Examaple 2:
  a b c d
a 0 1 1 1
b 1 0 1 1

sum total = 0  (if all are the same)
Distance 1
'''

'''
Idea 4: Let's try Levenstein Distance
'''

class Solution():
    def compare(self,s1,s2):
        if s1.lower() == s2.lower():
            return True
        return False

    def compare_diff_length(self,s1,s2):
        if not len(s1)==len(s2):
            return False
        '''
        Loop over all both of them and perform elementwise comparison
        '''
        for i in range(len(s1)):
            if not s1[i].lower()==s2[i].lower():
                return False
            return True

    def compare_by_distance(self,s1,s2,threshold=1):
        if not len(s1)==len(s2):
            return False
        else:
            for i in range(len(s1)):
                if not s1[i]==s2[i]:
                    dist+=1
                if dist >threshold:
                    return False
            return True

    def compare_by_distance_set(self,s1,s2,threshold=1):
        if not len(s1)==len(s2):
            return False
        else:
            '''
            use set technique
            '''
            #print (set(s1).intersection(set(s2)))
            if len(list(set(s1).intersection(set(s2))))>threshold:
                return False
        return True

    def distance_matrix(self,s1,s2):
        distance = [[]]
        count_zeors = 0
        for i in range(len(s1)):
            for j in range(len(s2)):
                if not s1[i]==s2[i]:
                    distance[i][j] = 1
                else:
                    distance[i][j] = 0
                    count_zeors +=1
        return distance,count_zeors

    def compare_by_distance_any_threshold(self,s1,s2,threshold):
        '''
        Call distance Matrix and count the number of zeors
        '''
        distance, count_zeros = self.distance_matrix(s1,s2)
        if max(len(s1),len(s2)) - count_zeros > thresold:
            return False
        return True



if __name__ == "__main__":
    s1 = 'abc'
    s2 = 'ABc'
    output = Solution()
    print (output.compare(s1,s2))

    #insertion and delteion, distance 1
    s3 = 'abcd'
    s4 = 'abd'  #return False
    s5 =  'abc'

    print (output.compare_by_distance_set(s4,s5))
