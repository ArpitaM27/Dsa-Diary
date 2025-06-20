#include<iostream>
using namespace std;
int main(){
    int n;
cout << "enter ur no madame";
cin>> n;
    if (n>=0)
    {
       cout << "no is positive";
    }
    else
    cout<< "no is neg";
    return 0;
}
    
// find lower case upper case
#include<iostream>
using namespace std;
int main(){
    char n;
cout << "enter ur character";
cin>> n;
    if ('a'<= n&& n<='z')
    {
       cout << "lowercase";
    }
    else if('A'<=n && n<='Z'){
    cout<< "uppercase";}
    else
    cout << "invalid input";
    return 0;
}
    
   //sum of nos
   #include<iostream>
using namespace std;
int main(){
   int sum=0,n;
   cout << "state ur no";
   cin>> n;
   for (int i = 0; i <=n; i++)
   {
    sum=sum+i;
    
   }
    cout<< sum<< " ";
    return 0;
}
    
  // sum of odd nos
   #include<iostream>
using namespace std;
int main(){
   int sum=0,n;
   cout << "state ur no";
   cin>> n;
   
   
   for (int i = 0; i <=n; i++)
   {
    if (i%2!=0)
    {
       
    
    sum=sum+i;
    }
   }

    cout<< sum<< " ";
    return 0;
}