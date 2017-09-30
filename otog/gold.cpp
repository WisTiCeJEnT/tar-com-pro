#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    pair(int,int) a[n];
    for(int i=0;i<n;i++){
        int ta,tb;
        cin >> ta >> tb;
        a[i] = make_pair(ta,tb);
    }
}
