'''
Reference: https://www.youtube.com/watch?v=Q5_2BCej9hg
'''

'''
function (meetings,haveHours)
meeting = {
    name:'Meeting1',
    hours: 2}

return meeting objects that can be attended
'''

'''
What is the time complexity of this algorithm?
1. We loop over meetings list O(n)
2. We sorted the list before --> O(n)logn
3. we append -> time complexity constanst
4. O(n)(n)log(n)--> O(n²)logn
'''

class Solution:
    def optimizeMeetings(self,meetings,haveHours):
        '''
        meetings: each meeting is a dict of dicts
        '''
        output_meetings = []
        sorted_meetings = sorted(meetings,key = lambda a:a['hours'],reverse=True)
        print (sorted_meetings)
        sum = 0
        for meeting in sorted_meetings:
            sum +=meeting['hours']
            if sum <= haveHours:
                output_meetings.append(meeting)
        return output_meetings

'''
Problem 2: min_number of meetings with highest number of hours.
lets say we have 8h
list: 2,3,1,8,9
sort (9,8,1,3,2) --> reverseTrue
//Find sum of hours
Same as leetcode question sum(list) <= a given number

Lets use Dynamic Programming without sorting:


'''

class Solution_Dynamic:
    def optimizemeetings_Dynamic(self,meetings,haveHours):


if __name__ == "__main__":
    meetings = [{'name':'Meeting1','hours':2},{'name':'Meeting2','hours':3},{'name':'Meeting3','hours':1}]
    haveHours = 3
    print ('name',meetings[0]['name'])

    object = Solution()
    print (object.optimizeMeetings(meetings,haveHours))
