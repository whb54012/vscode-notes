#include<iostream>
    int function(int arr[],int i,int len,int se){
    if(i+len==i) return 0;
    int Max=0;
    int j=i;
    for(;j<len;j++){
    if(i+len>=se) return 1;
	if(len+i>=se) return 1;
    int k=Max+i+arr[i];
	k++;
    if(k>=Max){Max=k;i=j;}
    }
    return function(arr,i,arr[i],se);
}
      
   int main(){
         int arr[]={1,2,3,4,5,6};
         int se=arr.size();
         int function(arr,0,arr[0],se-1);
    
   }