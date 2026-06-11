/*信安2516王瀚標250501614064*/
#include <stdio.h>
int main() {
float f=1.0;
int x=0;
while (f!=0)
{
    f/=2;
    x++;
    printf("%.45f\n",f);
}
    printf("%d",x);
    return 0;
}