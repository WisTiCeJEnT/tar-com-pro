#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    for(int i=0;i<n;i++)
    {
        int find = 0;
        char t[3][3];
        for(int j=0;j<3;j++)
        {
            for(int k=0;k<3;k++)
            {
                cin >> t[j][k];
            }    
        }
        for(int j=0;j<3;j++)
        {
            if (t[j][0] == 'O')
            {
                if(t[j][1] == 'O' and t[j][2]=='.')
                {
                    cout <<j+1<< " 3"<<endl;
                    find = 1;
                    break;
                }
                else if(t[j][1] == '.' and t[j][2]=='O')
                {
                    cout <<j+1<< " 2"<<endl;
                    find = 1;
                    break;
                }
            }
            else if(t[j][1]=='O' and t[j][2]=='O')
            {
                cout <<j+1<< " 1"<<endl;
                find = 1;
                break;
            }    
        }
        for(int j=0;j<3;j++)
        { 
            if (t[0][j] == 'O')
            {
                if(t[1][j] == 'O' and t[2][j]=='.')
                {
                    cout << "3 "<<j+1<<endl;
                    find = 1;
                    break;
                }
                else if(t[1][j] == '.' and t[2][j]=='O')
                {
                    cout << "2 "<<j+1<<endl;
                    find = 1;
                    break;
                }
            }
            else if(t[1][j]=='O' and t[2][j]=='O')
            {
                cout << "1 "<<j+1<<endl;
                find = 1;
                break;
            }    
        }
        if (t[0][0] == 'O' and t[1][1] == 'O' and t[2][2] == '.')
        {
            cout << "3 3" << endl;
            find = 1;
            break;
        }
        else if (t[0][0] == 'O' and t[1][1] == '.' and t[2][2] == 'O')
        {
            cout << "2 2" << endl;
            find = 1;
            break;
        }
        else if (t[0][0] == '.' and t[1][1] == 'O' and t[2][2] == 'O')
        {
            cout << "1 1" << endl;
            find = 1;
            break;
        }
        if (t[0][2] == 'O' and t[1][1] == 'O' and t[2][0] == '.')
        {
            cout << "3 1" << endl;
            find = 1;
            break;
        }
        else if (t[0][2] == 'O' and t[1][1] == '.' and t[2][0] == 'O')
        {
            cout << "2 2" << endl;
            find = 1;
            break;
        }
        else if (t[0][2] == '.' and t[1][1] == 'O' and t[2][0] == 'O')
        {
            cout << "1 3" << endl;
            find = 1;
            break;
        }
        //X
        if (find)
            break;
        for(int j=0;j<3;j++)
        {
            if (t[j][0] == 'X')
            {
                if(t[j][1] == 'X' and t[j][2]=='.')
                {
                    cout <<j+1<< " 3"<<endl;
                    break;
                }
                else if(t[j][1] == '.' and t[j][2]=='X')
                {
                    cout <<j+1<< " 2"<<endl;
                    break;
                }
            }
            else if(t[j][1]=='X' and t[j][2]=='X')
            {
                cout <<j+1<< " 1"<<endl;
                break;
            }    
        }
        for(int j=0;j<3;j++)
        { 
            if (t[0][j] == 'X')
            {
                if(t[1][j] == 'X' and t[2][j]=='.')
                {
                    cout << "3 "<<j+1<<endl;
                    break;
                }
                else if(t[1][j] == '.' and t[2][j]=='X')
                {
                    cout << "2 "<<j+1<<endl;
                    break;
                }
            }
            else if(t[1][j]=='X' and t[2][j]=='X')
            {
                cout << "1 "<<j+1<<endl;
                break;
            }    
        }
        if (t[0][0] == 'X' and t[1][1] == 'X' and t[2][2] == '.')
        {
            cout << "3 3" << endl;
            break;
        }
        else if (t[0][0] == 'X' and t[1][1] == '.' and t[2][2] == 'X')
        {
            cout << "2 2" << endl;
            break;
        }
        else if (t[0][0] == '.' and t[1][1] == 'X' and t[2][2] == 'X')
        {
            cout << "1 1" << endl;
            break;
        }
        if (t[0][2] == 'X' and t[1][1] == 'X' and t[2][0] == '.')
        {
            cout << "3 1" << endl;
            break;
        }
        else if (t[0][2] == 'X' and t[1][1] == '.' and t[2][0] == 'X')
        {
            cout << "2 2" << endl;
            break;
        }
        else if (t[0][2] == '.' and t[1][1] == 'X' and t[2][0] == 'X')
        {
            cout << "1 3" << endl;
            break;
        }
    }

}
