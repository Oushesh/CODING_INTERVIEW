#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

//check if map contains key
using namepsace std;

class Solution
{
public:
  vector <string> hash_table(vector<string>&words, int K)
  {
    int counter;
    map <string,int> dict;
    for (int i=0;i<words.size();i++)
    {
      it = dict.find(words[i]);
      if (it!=dict.end())
      {
        counter = 1;
        dict.push_back(words[i]);
      else if (it==dict.end())
      {
        dict.push_back(words[i]);
      }
      }
    }
    return dict;
  }

topKFrequent(vector <string>& words, int K)
{
  map <string,int> hash;
  hash = hash_table(words);
  sort(hash)
}


};


int main()
{
  vector <string> words  =  {}"the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"};
  int K = 2;
  Solution S1;
  cout << S1.topKFrequent(words,K) << endl;
}
