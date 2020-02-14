#Given a collection of intervals, merge all overlappign intervals
#Example 1:
#Input: [[1,3],[2,6],[8,10].[15,18]]
#Output: [[1,6],[8,10],[15,18]]

#Explanation: SInce intervals [1,3] and [2,6] overlap
#merge[1,6]


#Build pairs for comparison,
#Each pair is a List continaing  2 lists
#sort them

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        print (intervals)
        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged



#Graph SOlution:
#Connected Components:
#Build a graph between the vectors of
#int condition for merging
#Use Graph to build the solution:
#Build Grpah
class Connected_COmponent:
    def merge(self,intervals):
        return None

if __name__ == "__main__":
    #Datatype is a list of lists
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    output = Solution()
    print ('The new merged interval is:',output.merge(intervals))
