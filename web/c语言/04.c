#include<stdio.h>
#include<string.h>
int main(){
    char number[256];
    int a=0,b=0;
    gets(number);
    int len=strlen(number);
    for(int i=0;number[i]!='\0';i++){
        if(number[i]=='b'&&number[i+1]=='o'&&number[i+2]=='y')
        {a++;number[i]='\0';strcat(number,&number[i+2]);printf("%s\n",number);}
        else if(number[i]=='o'&&number[i+1]=='y'||number[i]=='b'&&number[i+1]=='o')
        {a++;number[i]='\0';strcat(number,&number[i+1]);printf("%sb\n",number);}
        else if(number[i]=='b'||number[i]=='o'||number[i]=='y')
        {a++;printf("%sc\n",number);}
        else if(number[i]=='g'&&number[i+1]=='i'&&number[i+2]=='r'&&number[i+3]=='l')
        {b++;number[i]='\0';strcat(number,&number[i+3]);}
        else if(number[i]=='i'&&number[i+1]=='r'&&number[i+2]=='l')
        {b++;number[i]='\0';strcat(number,&number[i+2]);}
        else if(number[i]=='r'&&number[i+1]=='l')
        {b++;number[i]='\0';strcat(number,&number[i+1]);}
        else if(number[i]=='l')
        {b++;}
       }
    printf("%d\n%d",a,b);
    return 0;
}
