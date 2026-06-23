#include<iostream>
using namespace std;
void quicksort(int arr[],int size){
    int i=0,j=0;
    for{;j<=size;j++}{
        if(arr[j]<arr[size]){
            int tmp=arr[j];
            arr[j]=arr[i];
            arr[i]=tmp;
            i++;
        }

    }
}
int main(){
    int arr[]={1,9,1,2,1,0,1};
    int k;
    cout<<k<<endl;
    quicksort(arr,sizeof(arr)/4);
}