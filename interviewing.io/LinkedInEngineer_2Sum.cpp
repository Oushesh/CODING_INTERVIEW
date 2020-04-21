/*
Reference for the interview: https://www.youtube.com/watch?v=JtIYZKsxswA
*/


/*
There are 2 different approaches
Since we are mentionning about 2 sum:
If we brute force the problem
we have complexity of O(n²).
*/
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;
class Numbers
{
public:
  pair <int, int> two_sum(vector <int> numbers,int target)
  {
      /*Build a container for the output of the number, complement[number]*/
      pair <int,int> output;
      unordered_map<int,int> complement;
      for (auto number:numbers)
      {
        if (number < target)
        {
          complement.insert(make_pair(number,target-number));
          if (complement.find(number)==complement.end())
          //if (find(numbers.begin(),numbers.end(),complement.at(number)))
          {
            output=make_pair(number,complement.at(number));
            return output;
          }
        }
      }

  }
};

int main()
{
  vector <int> numbers = {3,6,9,12,15,4,2,1,30};
  int target = 15;
  Numbers current_Numbers;
  pair<int, int> output = current_Numbers.two_sum(numbers,target);
  //Get the iterator
  cout << "The answer is"<< output.first << output.second << endl;
}
