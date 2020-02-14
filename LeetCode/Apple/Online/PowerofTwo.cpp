#include <iostream>
#include <vector>
#include <map>

using namespace std;
class Solution
{
public:
  bool isPowerOfTwo(int & n)
  {
    if (n==0){return false;}
    while (n%2==0)
    {
      n/=2;
    }
    return (n==1);
  }
};

int main()
{
  int Input = 16; 
  Solution S1;
  cout << S1.isPowerOfTwo(Input) << endl;
  return 0;
}
