#include <iostream>
#include<string.h>
#include <cassert>

using namespace std;

inline int getElement(int* Matrix, int row, int column, int stride)
{
    return Matrix[row * stride + column];
}

inline char* append(char* p, int n, bool& first)
{
    if (first)
        sprintf(p, "%d", n);
    else
        sprintf(p, ", %d", n);
    first = false;
    return p + strlen(p);
}

void BuildStringFromMatrixRec(int* Matrix, int Rows, int Columns, char* OutBuffer, int stride, bool& first)
{
    if (Rows < 1 || Columns < 1)
        return;
    char* p = OutBuffer;
    for (int i = 0; i < Columns; i++)
        p = append(p, getElement(Matrix, 0, i, stride), first);
    for (int i = 1; i < Rows; i++)
        p = append(p, getElement(Matrix, i, Columns - 1, stride), first);
    for (int i = Columns - 2; i >= 1; i--)
        p = append(p, getElement(Matrix, Rows - 1, i, stride), first);
    if (Columns > 1)
        for (int i = Rows - 1; i >= 1; i--)
            p = append(p, getElement(Matrix, i, 0, stride), first);
    int* Matrix2 = &Matrix[1 * stride + 1];
    BuildStringFromMatrixRec(Matrix2, Rows - 2, Columns - 2, p, stride, first);
}

void BuildStringFromMatrix(int* Matrix, int NumRows, int NumColumns, char* OutBuffer)
{
    bool first = true;
    BuildStringFromMatrixRec(Matrix, NumRows, NumColumns, OutBuffer, NumColumns, first);
}

/*

For testing I used the 2 cases:
Input:

(3x4) Matrix
2, 3, 4, 8,
5, 7, 9, 12,
1, 0, 6, 10

Output: 2, 3, 4, 8, 5, 7, 9, 12, 1, 0, 6, 10

Input:
(4x4) Matrix

2, 3, 4, 8,
5, 7, 9, 12,
1, 0, 6, 10,
15, 16, 17, 18

Output: 2, 3, 4, 8, 12, 10, 18, 17, 16, 15, 1, 5, 7, 9, 6, 0
*/

int main()
{
  //Performing Unit Tests here
  char buf[1024];
  //int size = sizeof(buf)/sizeof(*buf);
  //cout << size << endl;

  int m[] = {2, 3, 4, 8, 5, 7, 9, 12, 1, 0, 6, 10};
  int rows = 3;
  int columns = 4;
  //Check for positiveness of the rows, columns
  assert(rows>0);
  assert(columns>0);
  BuildStringFromMatrix(m, rows, columns, buf);

  cout << buf << endl;

  assert(!strcmp(buf, "2, 3, 4, 8, 12, 10, 6, 0, 1, 5, 7, 9"));
  cout << "The code gives the desired output" << endl;

  int rows_x = 4;
  int columns_x = 4;
  int x[] = {2, 3, 4, 8, 5, 7, 9, 12, 1, 0, 6, 10, 15, 16, 17, 18};
  BuildStringFromMatrix(x, rows_x, columns_x, buf);
  cout << buf << endl;

  assert(!strcmp(buf, "2, 3, 4, 8, 12, 10, 18, 17, 16, 15, 1, 5, 7, 9, 6, 0"));
  cout << "The code gives the desired output" << endl;

  return 0;
}
