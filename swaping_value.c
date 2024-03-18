#include<stdio.h>
int main ()
{
int a,b,c;
printf("enter a number =");
scanf("%d%d",&a,&b);
printf("before=\n%d\n%d\n",a,b);
c = a;
a = b;
b = c;
printf("after=\n%d\n%d\n",a,b);
}