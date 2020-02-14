#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
class Solution_2pointers
{
public:
  int threeSumSmaller(vector <int> & nums, int & target)
  {
    int sum = 0;
    //sort algorithm here
    vector  <int> sorted_nums;
    sort(nums.begin(),nums.end());
    for (int i=0;i<nums.size();i++)
    {
      sum +=twoSumSumaller(nums,i+1,target-nums[i]);
    }
    return sum;
  }

  int twoSumSumaller(vector <int> & nums, int startindex, int target)
  {
    int sum = 0;
    int left;
    left = startindex;
    int right;
    right = nums.size()-1;
    while (left < right)
    {
      if ((nums[left]+nums[right])<target)
      {
        sum+=right-left;
        left+=1;
      }
      else
      {
        right -=1;
      }
    }
    return sum;
  }
};


int main()
{
  vector <int> nums = {3,5,2,8,1};
  int target = 9;
  Solution_2pointers S1;
  cout << S1.threeSumSmaller(nums,target) << endl;
  return 0;
}
