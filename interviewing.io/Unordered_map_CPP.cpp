/*Dictionary or unordered dict translation of
 * the code from Python to C++
 * The best way to implement a dict in
 * C++ is via a an unordered_map
*/

#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

void solve()
{
    unordered_map <string,string> spnumbers;
    spnumbers = {{"one","uno"},{"two","dos"},{"three","tres"},{"four","cuatro"},{"five","cinco"}};

    for (auto i=spnumbers.begin();i!=spnumbers.end();i++)
    {
        //auto is used to automacally detect the data type
        //when a variable is declared. Use this ONLY when declaring
        //complex variables.

        cout << i->first << ":";
        cout << i->second << endl;
    }
}

int main()
{
    //another data alternative would be vectors of vectors of strings
    unordered_map<string, string> spnumbers;
    spnumbers = {{"one","uno"},{"two","dos"}};
    spnumbers["three"] ="tres";
    spnumbers["four"] = "cuatro";
    cout << "one is ";
    cout << spnumbers["one"] << endl;

    cout <<"Calling solve now:"<< endl;
    solve();
    return 0;
}