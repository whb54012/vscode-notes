#include<iostream>
using namespace std;
int MAX(int max,int sum){
    if(max<sum) return sum;
    else return max;
}
int max(int l,int r,int m,int arr[]){
    int suml=0,sumr=0,maxl=arr[m],maxr=arr[m+1];
    for(int i=m;i>=l;i--){
        suml+=arr[i];
        maxl=MAX(maxl,suml);
    }
    for(int i=m+1;i<=r;i++){
        sumr+=arr[i];
        maxr=MAX(maxr,sumr);
    }
    return maxr+maxl;
}
int summax(int arr[],int l,int r){
    if(l==r) return arr[l];
    int m=(l+r)/2;
    int L=summax(arr,l,m);
    int R=summax(arr,m+1,r);
    int LR=max(l,r,m,arr);
    return MAX(LR,MAX(L,R));
}
int main(){
    int arr[]={1,-3,2,3,4,-1,-3,6,8,10};
    int l=0,r=9;
    int max=summax(arr,l,r);
    cout<<max<<endl;
}