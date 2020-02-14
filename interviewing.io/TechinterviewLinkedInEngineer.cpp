#include <iostream>
#include <vector>
#include <string>

//The aim is to actually reverse the string.
/*
Input String =['p','e','r','f','e','c','t',' ','m','a','k','e','s',' ','p','r','a','c','t','i','c','e']
Output String = ['p','r','a','c','t','i','c','e',' ','m','a','k','e','s',' ','p','e','r','f','e','c','t']
*/

using namespace std;
class Solution
{
public:
  vector <string> reverseWholeString(vector <string> inputArray)
  {
    reverseWholeString(inputArray,0,inputArray.size());
    return inputArray;
  }
  void reverseWholeString(vector <string> inputArray, int f, int b)
  {
    //f: front
    //b: back
    //write a swap function here: 3 variables to swap 2. one is temp
    while (f<b)
    {
      //swap elementwise
      string tmp = inputArray[f];
      inputArray[f]      =  inputArray[b];
      inputArray[b]      =  tmp;
      b--;
      f++;
    }
  }

public:
  void reverseTheWordsInPlace(vector <string> inputArray)
  {
    //First do reverse the string,
    //Then reverse the words in the string
    //separated by comma
    reverseWholeString(inputArray);
    reverseTheWords(inputArray);
  }
public:
  void reverseTheWords(vector <string> inputArray)
    {
      int wf;
      int wb;
      int current = 0;
      while (current <inputArray.size())
      {
        //perform swapping here:
        wf = current;
        wb = indexOf(inputArray," ",wf);
        if (-1==wb)
        {
          reverseWholeString(inputArray,wf,inputArray.size()-1);
          current = inputArray.size();
        }
        else
        {
          reverseWholeString(inputArray,wf,wb-1);
          current = wb+ 1;
        }
      }
    }
public:
  int indexOf(vector <string> inputArray, string sentinal,int start)
  {
    for (int i=0;i<inputArray.size();i++)
    {
      if (sentinal == inputArray[i])
      {
        return  i; //successfull output
      }
      return -1;
    }
  }
};

int main()
{
  vector <string> inputArray = {"p","e","r","f","e","c","t"," " ,"m","a","k","e","s"," ","p","r","a","c","t","i","c","e"};
  Solution S1;
  vector <string> output = S1.reverseWholeString(inputArray);
  for (auto y: output)
  {
    cout << y << endl;
  }
  return 0;
};
