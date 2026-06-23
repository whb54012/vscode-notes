#include<iostream>
using namespace std;
void quicksort(int arr[],int size,int i){
    int j=i;
    if(j==size){return;}
    for(;j<size;j++){
        if(arr[j]<arr[size-1]){
            int tmp=arr[j];
            arr[j]=arr[i];
            arr[i]=tmp;
            i++;}}
            for(int m=0;m<=6;m++){
        cout<<arr[m]<<endl;
    }
    for(int m=j-1;m>=i;m--){
        int tmp=arr[m];
        arr[m]=arr[j];
        arr[j]=tmp;
        j--;
    }
    for(int m=0;m<=6;m++){
        cout<<arr[m]<<endl;
    }
    // quicksort(arr,j-1,0);
    // quicksort(arr,size,j);
}
int main(){
    int arr[]={1,9,1,2,1,0,1};
    int k;
    quicksort(arr,sizeof(arr)/4,0);
    // for(int m=0;m<=6;m++){
    //     cout<<arr[m]<<endl;
    // }
}