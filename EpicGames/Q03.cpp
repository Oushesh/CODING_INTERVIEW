/*
Write the code for the following function, without using any built-in functions
except malloc or operator new..
char* itoa(int Value, int Base);

where the returned value is allocated on behalf of the caller, value is
the integer to convert, and base is octal, decimal, or hex.
Your implementation is expected to be robust and production ready
*/
#include <iostream>
#include <cassert>

using namespace std;

//reverse
void reverse(char str[], int length)
{
    int start = 0;
    int end = length -1;
    while (start < end)
    {
        swap(*(str+start), *(str+end));
        start++;
        end--;
    }
}

// itoa
char* itoa(int num, int base)
{
    //Buffer to store the results
    char* str = new char[100];
    int i = 0;
    bool isNegative = false;

    /* Handle 0 explicitely, otherwise empty string is printed for 0 */
    if (num == 0)
    {
        str[i++] = '0';
        str[i] = '\0';
        return str;
    }

    if (num < 0)
    {
        isNegative = true;
        num = -num;
    }
    while (num != 0)
    {
        int rem = num % base;
        str[i++] = (rem > 9)? (rem-10) + 'a' : rem + '0';
        num = num/base;
    }
    // if -ve append '-'
    if (isNegative)
        str[i++] = '-';
    str[i] = '\0'; // End of string

    reverse(str, i);
    return str;
}

//Ref: https://www.rapidtables.com/convert/number/decimal-to-hex.html Checked here
int main()
{
  int num = 35631;  //1567;

  cout << "Base:10 " << itoa(num, 10) << endl;
  cout << "Base:2 " << itoa(num, 2) << endl;
  cout << "Base:8 " << itoa(num, 8) << endl;
  cout << "Base:16 " << itoa(num, 16) << endl;

  //Some test cases or unit test here:
  int negNum = -1567;
  cout << "Base:10 " << itoa(negNum, 10) << endl;
  cout << "Base:2 " << itoa(negNum, 2) << endl;
  cout << "Base:8 " << itoa(negNum, 8) << endl;
  cout << "Base:16 " << itoa(negNum, 16) << endl;
  return 0;
}

//Tested with results:
//1567
/*
Base:10 1567
Base:2 11000011111
Base:8 3037
Base:16 61f
*/

//Now -1567
/*
Base:10 1567
Base:2 -11000011111
Base:8 3037
Base:16 -61f
*/
