//fib
#include<iostream>
using namespace std;
int fib(int a){
    if(a==0)
    return 0;
    else if(a==1)
    return 1;
    else{
    return fib(a-2)+fib(a-1);}

}
int main(){
    int n;
    cout<< "enter how many terms";
    cin>> n;
    for (int i = 0; i < n; i++)
    {
        cout<< fib(i) << " ";
    }
    
return 0;
}

// add digits
