#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
class Solution
{
public:
    vector<vector<int>> subsets(vector<int>& nums)
    {
      vector<vector<int>> v;
        vector<int> b;
        v.push_back(b);
        for(int i=0;i<nums.size();i++)
        {
          int t=v.size();
            for(int j=0;j<t;j++)
            {
                b=v[j];
                b.push_back(nums[i]);
                v.push_back(b);
            }
        }
        return v;
    }
};
int main()
{
  vector <int> nums = {1,2,3};
  vector <vector <int>> output;
  Solution S1;
  output=S1.subsets(nums);
  //print the result to see the outcome
  return 0;
}
