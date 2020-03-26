#include <vector>
#include <iostream>
#include <string>

using namespace std;

class Solution
{
public:
  vector <string> splitter(string s1)
  {
    vector <string> characters;
    string substring;
    for (int i=0; i<s1.size();i++)
    {
      if (s1[i] !='|')
      {
        substring.push_back(s1[i]);
        characters.push_back(substring);
      }
    }
    return characters;
  }
  string join(string splits,string reversed,int left,int right)
  {
    return splits[left]+reversed+splits[right];
  }

  //Custom made C++ swap function;
  string reverse_substring(string & target, int f, int b)
  {
    //f: front
    //b: back
    //write a swap function here: 3 variables to swap 2. one is temp
    char tmp;
    while (f<b)
    {
      //swap elementwise
      tmp     = target[f];
      target[f]      =  target[b];
      target[b]      =  tmp;
      b--;
      f++;
    }
    return splits;
  }
  vector <string> reverse(string & splits)
  {
    int mid_index = int(splits.size()/2);
    int start_index = 0;
    int end_index   = splits.size()-1;

    int left = mid_index;
    int right = mid_index;
    string target = splits[mid_index];

    while (left !=start_index && right !=end_index)
    {
      string reversed=reverse_substring(target);
      left -=1;
      right +=1;
      target = join(splits,reversed,left,right);
    }
    return target;
  }
};

int main()
{
  string s1 =  "cat|dog|cow";
  /*
  I expect to see this: {{cat},{dog},{cow}}
  */
  Solution current;
  vector<string> splits = current.splitter(s1);
  cout << splits.size() << endl;
  for (auto alphabets: s1)
  {
    if (alphabets !='|')
    {
      cout << alphabets << endl;
    }
  }
  vector <string> output = current.reverse(splits);
  cout << "reversed already occurred" << endl;
  for (auto characters_reversed: output)
  {
    cout << characters_reversed << endl;
  }
  return 0;
}
