#include <iostream>
using namespace std;
double bal=0;
class bank{
public:
void showBalance(){
cout<<"Balance is "<<bal<<endl;

}
void deposite(){
double dep;
cout<<"Enter amount to deposite: ";
cin>>dep;
cout<<dep<<" has been successfully deposited"<<endl;
bal+=dep;
}
void withdraw(){
double w;
cout<<"Enter amount to withdraw: ";
cin>>w;
if(w>bal) 
cout<<"Insufficent balance"<<endl;
else{
bal-=w;
cout<<"Available balance is "<<bal<<endl;}

}
void disp(){
    int n;
    bool work=true;
    while(work){
    cout<<"Banking program\n"<<"---------------"<<endl;
    cout<<"1.Show Balance"<<endl;
    cout<<"2.Deposite"<<endl;
    cout<<"3.Withdraw"<<endl;
    cout<<"4.Exit"<<endl;
    cout<<"Enter your choice: ";
    cin>>n;
    switch(n){
        case 1:{showBalance();break;}
        case 2:{deposite();break;}
        case 3:{withdraw();break;}
        case 4:{work=false;break;}
    } 
}
} 
};

int main(){
bank b;
b.disp();
return 0;
    
}
