
#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

class Solution{
public:
  bool exist(vector <vector<string>> &board, vector <string> word)
  {
    //pass the string to a vector type templated to string:
    if (board.size()==0 || board[0].size()==0)
    {
      return false;
    }
    for (int i=0;i<board.size();i++)
    {
      for (int j=0;j<board[0].size();j++)
      {
        if (check(board,i,j,word,0))
        {
          return true;
        }
      }
    }
  }
  bool check(vector <vector <string>> & board, int i, int j,vector <string> word, int current)
  {
    //build a vector container to hold string word;
    if (current==word.size())
    {
      return true;
    }
    else if (i<0 || i>=board.size() || j<0 || j>=board[0].size() || board[i][j]=="-1")
    {
      return false;
    }
    else
    {
      if (board[i][j]==word[current])
      {
        string temporary;
        temporary = board[i][j];
        board[i][j] = "-1";
        board[i][j]=temporary;
        return check(board,i-1,j,word,current+1) || check(board,i+1,j,word,current+1) || check(board,i,j-1,word,current+1) || check(board,i,j+1,word,current+1);
      }
      else
      {
        return false;
      }
    }
  }
};


int main()
{
  //main Data type is vectors of vectors of int.
  vector <vector <string>> board={
      {"A","B","C","E"},
      {"S","F","C","S"},
      {"A","D","E","E"}
    };
    string target="ABCCEDS";
    vector <string> word;
    word.push_back(target);
    cout << word[3] << endl;
    Solution S1;
    cout <<S1.exist(board,word)<<endl;
    return 0;
}
