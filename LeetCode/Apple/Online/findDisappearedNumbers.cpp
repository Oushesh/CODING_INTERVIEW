/*
'''
Apple online interview:
448. Find all nummbers Disapperared in an Array.
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the
returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
class Solution_Set
{
public:
  bool compare (int i,int j) { return (i<j); }
  vector <int> findDisappearedNumbers(vector <int> & nums)
  {
    vector <int> output;
    auto sorted_num = nums;
    sort(sorted_num.begin(),sorted_num.end());
    for (int i=1;i<nums.size();i++)
    {
      if (find(sorted_num.begin(),sorted_num.end(),i)==sorted_num.end())
      {
        output.push_back(i);
      }
    }
    return output;
  }
};

int main()
{
  vector <int> nums = {4,3,2,7,8,2,3,1};
  Solution_Set S1;
  vector <int> output=S1.findDisappearedNumbers(nums);

  /* You need to build an iterator to print the outptut*/
  for (auto elements: output)
  {cout << elements << endl;}
  return 0;
}
