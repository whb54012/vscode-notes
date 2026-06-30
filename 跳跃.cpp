#include<iostream>
    int function(int arr,int i,int len,int se){
    if(i+len==i) return 1;
    int Max=0;
    int j=i;
    for(;j<len;j++){
	if(len+i>=se) return 1;
    int j=Max+i+arr[i];
	Max=max(Max,j);
                  }
    return function(int arr,int len,int i);
}
      
   int main(){
         int arr[]={1,2,3,4,5,6};
         int se=arr.size();
         int function(arr,0,arr[0],se-1);
    
   }