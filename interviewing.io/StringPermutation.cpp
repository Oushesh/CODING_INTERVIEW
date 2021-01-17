/*
String permutation.cpp

1. We already wrote in python, now in C++. If we do an elementwise
   to elementwise comparion we have a complexity of O(n²)

2. The other optimisation is to find the words based on a dictionary
   that exsited and reduce the search complexity. Walk the interviwer
   through it and how much optisaion can be done. In best case
   the word shuffling is done such that the words can be directly querried
   from the dictionary. in worst case we have a permutation that lexically
   ununderstandable.

3. Build an ascii map --> sort it out according numbers
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

//Custom build print function to see
//the output results

void printVector(vector<char> )
{

}

bool check(vector<char> s1, vector<char> s2)
{
  //Convert the char elements to ascii numbers for easy sorting.
  vector <int> s1_int;
  vector <int> s2_int;

  //Take care of edge case here, they have to be of the same length
  if (s1.size()!=s2.size())
    return false;
  else
  {
    for (char a: s1)
    {
      s1_int.push_back(int(a));
    }

    for (char b:s2)
    {
      s2_int.push_back(int(b));
    }
    //now both strings s1 and s2 are represented by
    //vectors of int.

    //now lets perform a sorting out: c++ stl sort -->
    sort(s1_int.begin(),s1_int.end());
    sort(s2_int.begin(),s2_int.end());
    if (s1==s2)
      return true;
    else
      return false;
  }
};

int main()
{
  //Lets define it directly as a vector<char> or so and thats easiers.
  vector<char> s1 = {'g','e','e','k','f','o','r','g','e','e','k','s'};
  vector<char> s2 = {'f','o','r','g','e','e','k','g','e','e','k','s'};
  cout << "The 2 strings are permutations of each other" << check(s1,s2);
  return 0;
}


/*
This algorithm has the same complexity as the one implemented in Python:
 O(N log N).

 Space Complexity: O(len(s1)+len(s2))--> O(m+n) or O(2n) if both have
 the same length amounting to the same O(n)
*/

//Use repl.it to fast test code.
