
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>

using namespace std;
class Solution{
public:
  vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
      if (nums1.size() > nums2.size()) {
          return intersect(nums2, nums1);
      }
      unordered_map<int, int> m;
      for (auto n : nums1)
      {
          ++m[n];
      }
      int k = 0;
      for (auto n : nums2) {
          auto it = m.find(n);
          if (it != end(m) && --it->second >= 0) {
              nums1[k++] = n;
          }
      }
      return vector(begin(nums1), begin(nums1) + k);
  }
};


class Solution_old
{
public:
  vector <int> intersect(vector<int> & nums1,vector<int>& nums2)
  {
    vector <int> common;
    map <int,int> dictionary;
    if (nums1.size()>nums2.size())
    {
      dictionary = hashmap(vector <int> & nums1);
      if ()

      dictionary[i]-=1;
    }
    else
    {
      dictionary = hashmap(vector <int> & nums2);
      dictionary[i]-=1;
    }
  return common;
  }
};


int main()
{
  vector <int> nums1 = {4,9,5};
  vector  <int> nums2 = {9,4,9,8,4};
  Solution S1;
  cout << S1.intersect(nums1,nums2) << endl;

  Solution_old S2;
  cout << "The intersection elements according to my implementation are:",S2.intersect(nums1,nums2)<<endl;
  return 0;
}
