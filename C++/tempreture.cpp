#include <iostream>
using namespace std;

int main(){
    string t;
    int temp;
    cout<<"Enter tempreture: ";
    cin>>temp;
    cout<<"convert to(f/c): ";
    cin>>t;
    double d=(t=="c")? (temp-32)*5/9: (temp*9/5)+32;
    cout<<d;


    return 0;
}