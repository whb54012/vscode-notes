#include<iostream>
using namespace std;
int start,End,MIN;
int MAX(int max,int sum){
    if(max<sum) return sum;
    else return max;
}
void max(int l,int r,int m,int arr[]){
    int suml=0,sumr=0,maxl=arr[m],maxr=arr[m+1];
    int tmpl=m,tmpr=m+1;
    for(int i=m;i>=l;i--){
        suml+=arr[i];
        if(maxl<suml){
            tmpl=i;
            maxl=suml;
        }
    }
    for(int i=m+1;i<=r;i++){
        sumr+=arr[i];
        if(maxr<sumr){
            tmpr=i;
            maxr=sumr;
        }
    }
    if((maxr+maxl)>MIN){
        start=tmpl;
        End=tmpr;
        MIN=maxr+maxl;
    }
}
void summax(int arr[],int l,int r){
    if(l==r)//{
        if(arr[l]>MIN){
            MIN=arr[l];
            start=l;
            End=r;}
        // return arr[l];}
    int m=(l+r)/2;
    summax(arr,l,m);
    summax(arr,m+1,r);
    max(l,r,m,arr);
    // return MAX(LR,MAX(L,R));
}
int main(){
    int arr[]={1,-3,2,3,4,-1,-3,6,8,10};
    int l=0,right=9;
    MIN=-1000000;
    int total=0;
    summax(arr,l,right);
    // int max=
    for(int i=start;i<=End;i++){
        total+=arr[i];
    }
    cout<<start<<endl;
    cout<<End<<endl;
    cout<<total<<endl;
}