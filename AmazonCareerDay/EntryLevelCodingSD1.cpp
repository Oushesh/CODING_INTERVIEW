//EntryLevelCodingSD1.cpp

/*
Ref: https://www.youtube.com/watch?v=595NTKwQbwY
*/

#include <iostream>
#include <vector>
#include <experimental/algorithm>
#include <string>
#include <boost/algorithm/string.h>

using namespace std;

class StringChecker
{
public:
	//Constructor here
	StringChecker(vector <string> rev, vector <string> rep, vector <string> string query)
	{
		this->rev = rev;
		this->rep = rep ;
		this->query = query;
	}

	//Function to set all characters to lower alphabets
	vector <string> ThreeKeySug(vector <string> rev, vector <string> rep, vector <string> query)
	{
		vector <string> outputs;
		//sort the vector
		vector <string> lower_rep = sort(rep.begin(),rep.end());
		//put all characters to lower case
		std::for_each(lower_rep.begin(),lower_rep.end(),[] (char & c))
		{
			c = ::tolower(c);
		};


		for (int i=1;i<query.size();i++)
		{
			vector <string> subQuery = query[0:i+1];
			std::for_each(subQuery.begin(), subQuery.end(),[] (char & c))
			{
				c = ::tolower(c);

			};
			vector <string> matched_words;
			for (auto word:lower_rep)
			{
				if (word.rfind(subQuery,0)==0)
				{
					matched_words.push_back(word);
				}
				//bool b = boost::algorithm::contains(word,lower_rep);
				if (matched_words.size()==3)
				{
					break;
				}
				if (matched_words.size>0)
				{
					outputs.push_back(matched_words);

				}
			}

		}
		return outputs;
	}
}

int main()
{
	//instantiate the class here

	StringChecker current_string;
	cout << "The output for the match is the following:" << current_string.
	return 0;
}

//TODO: to check and debug the code to see how it works
