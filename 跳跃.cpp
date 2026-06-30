#include<iostream>
using namespace std;
    int function(int arr[],int i,int len,int se){
    if(arr[i]==0) return 0;
    if(len>=se) return 1;
    int Max=0,m=0;
    int j=i;
    for(;j<=len;j++){
    Max=j+arr[j];
    if(Max>=m){m=Max;i=j;}
    }
    return function(arr,i,arr[i]+i,se);
}      
   int main(){
        int arr[]={2,1,0,4,5,6};
        int se = sizeof(arr) / sizeof(arr[0]);
        int result = function(arr, 0, arr[0], se - 1);
        if(result==1) cout<<"true"<<endl;
        else cout<<"False";
        return 0;
}