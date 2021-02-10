/*
Author: Oushesh

palindrome check in Cpp
*/
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

class Words
{
public:
	//Constructor here
	bool palindrome(vector <char> & string)
	{
		//This function checks whether a string is a plaindrome or not.
		for (int i=0; i<string.size();i++)
		{
			if (string[i]!=string[string.size()-i])
				return false;
			else
				continue;
		}
		return true;
	}

	vector <char> check (vector <char> & string)
	{
		vector <char> output;
		int left = 0;
		int right = string.size();
		while (right>left)
		{
			if (true==palindrome(string[left:right])
			{
				output.push_back(string[left:right]);
				left+=1;
				right-=1;
			}
			if (true !=palindrome(string[left:right]))
				left+=1:
			if (true!=palindrome(string[left:right]))
				right-=1;
		}
		return output;
	}
};
int main()
{
	vector <char> string = {"a","n","n","a"};
	Words given_words;
	for (auto palindrome: given_words.check(string))
		cout <<"The palindromes from this string are: " << palindrome << endl;
	return 0;
}

// TODO: todebug and test