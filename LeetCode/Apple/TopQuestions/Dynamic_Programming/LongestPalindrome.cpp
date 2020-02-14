//
//Dynamic Programming Solution in C++
#include <iostream>
#include <map>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;
class Solution{
public:
  string longestPalindrome(string & s)
  {
    int left = 0;
    int right = 2;
    vector <int> indices={};
    for (int i=1;i<s.length()-1;i++)
    {
      while (left>=0 && right < s.length())
      {
        if (s[left]==s[right])
        {
          indices.push_back(left);
          left -=1;
          right +=1;
        }
      }
      indices.push_back(right);
    }
    return s.substr(indices[0],indices[-1]);
  }
};

int main()
{
  string s = "ababa";
  Solution palindrome;
  cout << palindrome.longestPalindrome(s) << endl;
  return 0;
}
