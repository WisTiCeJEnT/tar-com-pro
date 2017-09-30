#include <iostream>
using namespace std;
int main()
{
    int n,a,b;
    cin >> n >> a >> b;
    int ans = 0;
    char t[n][n];
    for(int i=0;i<n;i++)
    {
        int add = 0;
        for(int j=0;j<n;j++)
        {
            if(((j/a)%2==0 and (i/a)%2==0) or ((j/a)%2!=0 and (i/a)%2!=0))
                add = 1;
            if(((j/b)%2==0 and (i/b)%2==0) or ((j/b)%2!=0 and (i/b)%2!=0))
                add = 1;
            ans += add;
            if(add)
                t[i][j] = '#';
            else
                t[i][j] = '.';
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cout << t[i][j];
        }
        cout << endl;
    } 
    cout << ans << endl;
}