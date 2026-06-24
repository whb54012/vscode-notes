#include<iostream>
using namespace std;
void quicksort(int arr[],int r,int l){
    int j=l,i=l;
    if(l>=r){return;}
    for(;j<=r;j++){
        if(arr[j]<arr[r]){
            int tmp=arr[j];
            arr[j]=arr[i];
            arr[i]=tmp;
            i++;}}
    //         for(int m=0;m<=6;m++){
    //     cout<<arr[m];
    // }
    j--;
    for(int m=j-1;m>=i;m--){
        int tmp=arr[m];
        arr[m]=arr[j];
        arr[j]=tmp;
        j--;
    }
    // cout<<j<<endl;
    // for(int m=0;m<=6;m++){
    //     cout<<arr[m];
    // }
    quicksort(arr,j-1,l);
    quicksort(arr,r,j+1);
}
int main(){
    int arr[]={3,1,2};
    int k;
    quicksort(arr,sizeof(arr)/4-1,0);
    for(int m=0;m<=2;m++){
        cout<<arr[m];
    }
}