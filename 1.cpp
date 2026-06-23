#include<iostream>
using namespace std;
int sum(int l,int r,int m){
    for(int i=m,i>=l,i--){

    }
    for(int i=m+1,i<=r,i++){

    }
}
int summax(int arr[],int l,int r){
    if(l==r) return arr[l];
    int m=(l+r)/2;
    int L=summax(arr,l,m);
    int R=summax(arr,m+1,r);
    int LR=max(l,r,m);
}
int main(){
    int arr[]={1,-3,2,3,4,-1,-3,6,8,10};
    int l=0,r=9;
    return summax(arr,l,r);
}