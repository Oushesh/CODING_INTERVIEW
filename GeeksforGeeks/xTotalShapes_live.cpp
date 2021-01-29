#include <iostream>
#include <vector>
#include <deque>
using namespace std;


void neighbour(vector<vector<char>> grid, int i, int j, int m, int n)
{
    if (i>0 || j>0 || i<=m || j<=n || grid[i][j]=='X')
      return;

    grid[i][j]='X'

    //recusrive call here frr all the neighbours
    neighbour(grid,i+1,j,m,n);
    neighbour(grid,i-1,j,m,n);
    neighbour(grid,i,j+1,m,n);
    neighbour(grid,i,j-1,m,n);
}

int xShape(vector<vector<char>> grid)
{
    // Code here
    int m = grid.size();
    int n = grid[0].size();
    int count = 0;

    for (int i=0;i<m;i++)
    {
        for (int j=0;j<n;j++)
        {
            //Call the search function recursively only if the grid[i][j]=='X'
            if (grid[i][j]=='X')
            {
                neighour(grid,i,j,m,n);
                count +=1;
            }
        }
    }
    return count;
}


// Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, m;
		cin >> n >> m;
		vector<vector<char>>grid(n, vector<char>(m, '#'));
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				cin >> grid[i][j];
			}
		}
		int ans = xShape(grid);
		cout << ans <<'\n';
	}
	return 0;
}  // } Driver Code Ends
