#include<stdio.h>
#include<string.h>
int main(){
    char number[101],num1[101];
    int len,sum=0;
    scanf("%d",&len);
    getchar();
    gets(number);
    for(int i=0;i<len;i++){
        if(number[i]=='V'&&number[i+1]=='K') {sum++;
                                             number[i]='\0';
                                            if(number[i+2]!='\0')
                                             strcat(number,&number[i+2]);i=i-1;
                                            len=len-2;}
    }
    for (int i = 0; i<len; i++)
    { if(number[i]=='V'&&number[i+1]!='\0') {sum++;break;;}; }   
    printf("%d",sum);
} 