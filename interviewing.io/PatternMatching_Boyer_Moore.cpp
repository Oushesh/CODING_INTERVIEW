//
// Created by Oushesh on 04/12/2020.
//
//Reference: https://www.sanfoundry.com/cpp-program-implement-boyer-moore-algorithm-string-matching/
//The preprocessing function for Boyer Moore's Bad
//character heuristic function

#include <unordered_map>
#include <string.h>
#include <iostream>


# define NO_OF_CHARS 256

int max(int a, int b)
{
    return (a>b) ? a:b;
}

void badCharHauristic(char *str, int size, int badchar[NO_OF_CHARS])
{

    //initialize all coccurrences as -1
    for (int i=0; i< NO_OF_CHARS;i++)
        badchar[i] = -1;

    //Fill the actual value of last occurrence of a character
    for (int i=0; i<size;i++)
        badchar[(int) str[i]] = i;
}

void search(char *txt, char*pat)
{
    //Similar to python it starts with 1, indexing starts with 0
    int m = strlen(pat);
    int n = strlen(txt);

    badCharHauristic(pat,m, badchar);

    //shift = 0
    int s = 0;
    while (s<=(n-m))
    {
        int index = m-1;
        while (index>=0 && pat[index]==txt[s+index])
            index--;
        if (index < 0)
        {
            cout << "Pattern occurs at shift" << endl;
            s += (s + m < n) ? m - badchar[txt[s + m]] : 1;
        }
        else
        {
            s+=max(1,index-badChar[txt[s+index]]);
        }

    }
}


/*
 * Driver Program to test the above function*/

int main()
{
    char txt[] = "ABAAABCD";
    char pat[] = "ABC";
    search(txt,pat);
    return 0;
}