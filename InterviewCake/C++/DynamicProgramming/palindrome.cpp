/*
Author: Oushesh
palindrome check in CPP

*/
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

class Words
{
public:
	bool palindrome(vector <char> & string)
	{
		//This function checks whether a string is a plaindrome or not.
		for (int i=0; i<string.size();i++)
		{
			//This part checks whether the string is
			//palindrome or not.
			if (string[i]!=string[string.size()-i])
				return false;
			else
				continue;
		}
		return true;
	}

  //Special Function to slice 
  vector  <char> slice(vector <char> string, int left, int right)
  {
    auto first = string.cbegin() + left;
    auto last = string.cbegin() + right+1;
    vector <char> subvec(first,last);
    return subvec;
  }

	vector <char> check (vector <char> & string)
	{

		vector <vector <char>> output;
		int left = 0;
		int right = string.size();
    
    //access subvector using 
    //Ref: https://www.techiedelight.com/get-slice-sub-vector-from-vector-cpp/    
    while (right>left)
		{
      //how to extract subarray from here:
      
			if (true==palindrome(slice(string,left,right)))
			{
				output.push_back(slice(string,left,right));
				left+=1;
				right-=1;
			}
			if (true !=palindrome(slice(string,left,right)))
				left+=1;
			if (true!=palindrome(slice(string,left,right)))
				right-=1;
		}
		return output;
	}
};
int main()
{
	vector <char> string = {'a','n','n','a'};
	Words given_words;
	for (auto palindrome: given_words.check(string))
		cout <<"The palindromes from this string are: " << palindrome << endl;
	return 0;
}

// TODO: finish debugging this and test