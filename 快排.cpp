#include<iostream>
using namespace std;
void quicksort(int arr[],int size,int i){
    int j=i;
    for(;j<size;j++){
        if(arr[j]<arr[size]){
            int tmp=arr[j];
            arr[j]=arr[i];
            arr[i]=tmp;
            i++;}}
    for(int m=j-1;m>=i;m--){
        int tmp=arr[j];
        arr[m]=arr[j];
        arr[j]=tmp;
        j--;
    }
    quicksort(arr,j-1,0);
}
int main(){
    int arr[]={1,9,1,2,1,0,1};
    int k;
    cout<<k<<endl;
    quicksort(arr,sizeof(arr)/4);
}