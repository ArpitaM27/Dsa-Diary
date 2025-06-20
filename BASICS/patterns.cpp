#include<iostream>
using namespace std;
int main(){
int n;
cout<< "state ur no";
cin>>n;
for (int i = 0; i < n; i++)
{
   
   for (int j = 0; j <=i; j++)
   {
    cout<< "*";
   }
   cout<<endl;
}

return 0;
}

#include<iostream>
using namespace std;
int main(){
int n;
cout<< "state ur no";
cin>>n;
for (int i = 1; i <= n; i++)
{
   
   for (int j = i; j >0; j--)
   {
    cout<< j<< "";
   }
   cout<<endl;
}

return 0;
}

#include<iostream>
using namespace std;
int main(){
int n;
cout<< "state ur no";
cin>>n;
for (int i = 1; i <= n; i++)
{
   
   for (int j = 1; j <i; j++)
   {
    cout<< " ";
   }
  

for (int j = i; j <=n; j++)
{
   cout << j<< "";
}
 cout<<endl;
}
return 0;
}


#include<iostream>
using namespace std;
int main(){
int n;
cout<< "state ur no";
cin>>n;
for (int i = 1; i <= n; i++)
{
   
   for (int j = 1; j <i; j++)
   {
    cout<< "";
   }
  

for (int j = i; j <n; j++)
{
   cout << j<< "";
}
 cout<<endl;
}
return 0;
}