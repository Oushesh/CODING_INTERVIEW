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

Example:
Lets use Dynamic Programming without sorting:
[2,3,4,10,7,5], Havehours --> 9

Dynamic Sorting and Summing:

if len(meetings)==odd:
    center = len(meetings)+1/2
else:
    center= len(meetings)/2

left_pointer = 0
right_pointer = len(meetings)
output = []
while (center <=right):
    if (number_right+number_left)<haveHours:
        left -=1
        right+=1

'''
class Solution_Dynamic():
    def sortmeetings_Dynamic(self,meetings):
        if len(number)%2==1:
            mid = int(len(meetings)/2)
        else:
            mid= int(len(meetings)+1/2)

        left    = 0
        right   = len(meetings)-1
        current = 1
        sum     = 0
        while (current<=right):
            if meetings[current]['hours'] < meetings[left]['hours']:
                meetings[left]['hours'],meetings[current]['hours']= meetings[current]['hours'], meetings[left]['hours']
                left +=1
            elif meetings[right]['hours'] < meetings[current]['hours']:
                meetings[current]['hours'],meetings[right]['hours'] = meetings[right]['hours'],meetings[current]['hours']
                right -=1
            else:
                current +=1
        return meetings

    def optimize_meetings(self,sorted_meetings,haveHours):
        '''
        Since we have a dynamic sorted meeting dict already: lets start from the
        right: if right < havehours else right=right-1; check(right +right-1) < Havehours:

        '''
        index = []
        sum = 0
        dict = {}
        for i  in range(len(sorted_meetings)):
            sum+=sorted_meetings[i]['hours']
            if sum <= haveHours:
                dict[sorted_meetings[i]['hours']] = haveHours-sorted_meetings[i]['hours']
                index.append(i)
        return index


if __name__ == "__main__":
    meetings = [{'name':'Meeting1','hours':2},{'name':'Meeting2','hours':3},{'name':'Meeting3','hours':1}]
    haveHours = 3
    print ('name',meetings[0]['name'])

    object = Solution()
    print (object.optimizeMeetings(meetings,haveHours))
    object_Dynamic = Solution_Dynamic()
    print (object_Dynamic.optimize_meetings(meetings,haveHours))
