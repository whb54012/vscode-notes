#include<iostream>
using namespace std;
    int function(int arr[],int i,int len,int se){
    if(i+len==i) return 0;
    int Max=0,m=1;
    int j=i;
    for(;j<len;j++){
    if(i+len>=se) return 1;
    int k=Max+arr[j]+m;
    m++;
    if(k>=Max){Max=k;i=j;}
    }
    return function(arr,i,arr[i]+i,se);
}      
   int main(){
        int arr[]={1,2,3,4,5,6};
        int se = sizeof(arr) / sizeof(arr[0]);
        int result = function(arr, 0, arr[0], se - 1);
        if(result==1) cout<<"ture"<<endl;
        else cout<<"False";
        return 0;
   }