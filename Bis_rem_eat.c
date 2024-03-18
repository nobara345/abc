#include<stdio.h>
int main ()
{
int a,b,c,d;
printf("enter a number of biscuits =");
scanf("%d",&a);
printf("enter a number of dogs = ");
scanf("%d",&b);
c=a/b;
d=a%b;
printf(" biscuits eaten by one dog =%d\n",c);
printf("remaining biscuits= %d",d);
}