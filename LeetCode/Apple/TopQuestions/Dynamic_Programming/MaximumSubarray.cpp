#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
  int maxSubArray(vector <int> & nums)
  {
    int i = 0;
    int max_sum;
    int n = nums.size();
    int curr_sum;
    curr_sum = nums[0];
    max_sum = nums[0];
    for (int i=0; i< n;i++)
    {
      curr_sum = max(nums[i],nums[i]+curr_sum);
      max_sum  = max(curr_sum,max_sum);
    }
    return max_sum;
  }
};


//Divide and Conquer Approach;
//Graph Algorithm Approach
class Solution_DC
{
public:
  int cross_sum(vector <int> & nums, int & left, int & right, int & p)
  {
    if (left==right)
    {
      return nums[left];
    }
    int left_subsum = numeric_limits<int>::infinity();
    left_subsum = -left_subsum;
    int curr_sum    = 0;
    for (int i =0; i<left-1;i--)
    {
      curr_sum +=nums[i];
      left_subsum = max(left_subsum,curr_sum);
    }

    int right_subsum = numeric_limits<int>::infinity();
    right_subsum     = -right_subsum;
    for (int i=0; i<right+1; i++)
    {
      curr_sum+=nums[i];
      right_subsum = max(right_subsum,curr_sum);
    }
    return right_subsum+left_subsum;
  }

  int helper(vector <int> & nums,int & left,int & right)
  {
    if (left == right)
    {
      return nums[left];
    }
    int p = (left+right)/2;
    int left_sum  = Solution_DC::helper(nums,0,nums.size()-1);
    int right_sum = Solution_DC::helper(nums,p+1,right);
    int cross_sum = Solution_DC::helper(nums,left,right,p);

    int max_1 = max(left_sum,right_sum);
    int max_2 = max(left_sum,cross_sum);
    int max_3 = max(right_sum,cross_sum);
    return max(max(max_1,max_2),max(max_2,max_3));
  }

  int maxSubArray_DC{vector <int> & nums)
  {
    return Solution_DC::helper(nums,0,nums.size()-1);
  }
  }
};


int main()
{
  vector <int> nums = {-2,1,-3,4,-1,2,1,-5,4};
  Solution output;
  cout << output.maxSubArray(nums) << endl;
  return 0;
}
