#include<stdio.h>
#include<string.h>
int main(){
int x;
char a[101],b[101];
scanf("%d",&x);
getchar();
gets(a);
    for(int i=0;i<x;i++){
        int num;
        scanf("%d",&num);
        if(num==1) {scanf("%s",b);
                 strcat(a,b);
                 printf("%s\n",a);}
        else if(num==2) {int t,y;
                      scanf("%d",&t);
                      scanf("%d",&y);
                    strcpy(b,&a[t]);
                b[y]='\0';strcpy(a,b);
            printf("%s\n",a);} 
        else if(num==3) {int t,y=0;
                      scanf("%d",&t);
                      scanf("%s",b);
                    strcat(b,&a[t]);a[t]='\0';
                strcat(a,b);printf("%s\n",a);}
        else {char b[100];
        scanf("%s",b);
        char*p=strstr(a,b);
        printf("%d\n", p != NULL ? (int)(p - a) : -1);}        
    }
   return 0;
}