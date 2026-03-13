#include <iostream>
using namespace std;

int main(){
    int n;
   srand(time(NULL));
   int num=(rand()%10)+1;
   bool working=true;
   cout<<"----Random number guessing----"<<endl;
   while(working){
   cout<<"Guess the number btw(1-10): ";
   cin>>n;
   if(num!=n){
    if(n>num){
        cout<<"Too big!"<<endl;
    }
    else{
        cout<<"Too small!"<<endl;
    }
   }
   else{
    cout<<"hidden was "<<num<<endl;
    working=false;

   }
}


}