#include<stdio.h>
int main ()
{
int hrs,min,sec;
printf("enter a seconds=");
scanf("%d",&sec);
hrs=sec/3600;
sec=sec%3600;
min=sec/60;
sec=sec%60;
printf("hours =%d:min =%d:sec =%d",hrs,min,sec);
}