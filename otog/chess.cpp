#include <iostream>
using namespace std;
int main()
{
    int n,a,b;
    cin >> n >> a >> b;
    char t[n][n];
    for(int i=0;i<n;i++)
    {
        if((i/a)%2==0)
        {
            for(int j=0;j<n;j++)
            {
                if((j/a)%2==0)
                    t[i][j] = '#';
                else
                    t[i][j] = '.';
            }
        }
        else
        {
            for(int j=0;j<n;j++)
            {
                if((j/a)%2==0)
                    t[i][j] = '.';
                else
                    t[i][j] = '#';
            }
        }
    }
    char t2[n][n];
    for(int i=0;i<n;i++)
    {
        if((i/b)%2==0)
        {
            for(int j=0;j<n;j++)
            {
                if((j/b)%2==0)
                    t2[i][j] = '#';
                else
                    t2[i][j] = '.';
            }
        }
        else
        {
            for(int j=0;j<n;j++)
            {
                if((j/b)%2==0)
                    t2[i][j] = '.';
                else
                    t2[i][j] = '#';
            }
        }
    }
    int ans = 0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if (t[i][j] == '#' || t2[i][j] =='#')
                ans ++;
        }
    }
    cout << ans << endl;
}