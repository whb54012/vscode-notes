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
    int tmp=arr[j];
    arr[j]=arr[i];
    arr[i]=tmp;
    quicksort(arr,l,i-1);
    quicksort(arr,i+1,r);
}
int main(){
    int arr[]={5,3,4,1,2};
    int k;
    quicksort(arr,0,sizeof(arr)/sizeof(int)-1);
    for(int m=0;m<=4;m++){
        cout<<arr[m];
    }
}