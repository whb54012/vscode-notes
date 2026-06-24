#include<iostream>
using namespace std;
void quicksort(int arr[],int l,int r){
    int j=l,i=l;
    if(l>=r){return;}
    for(;j<r;j++){
        if(arr[j]<arr[r]){
            int tmp=arr[j];
            arr[j]=arr[i];
            arr[i]=tmp;
            i++;}}
    //         for(int m=0;m<=6;m++){
    //     cout<<arr[m];
    // }
    int tmp=arr[j];
    arr[j]=arr[i];
    arr[i]=tmp;
    // cout<<j<<endl;
    // for(int m=0;m<=6;m++){
    //     cout<<arr[m];
    // }
    quicksort(arr,l,i-1);
    quicksort(arr,i+1,r);
}
int main(){
    int arr[]={5,3,4,1,2};
    int k;
    quicksort(arr,0,sizeof(arr)/4-1);
    for(int m=0;m<=4;m++){
        cout<<arr[m];
    }
}