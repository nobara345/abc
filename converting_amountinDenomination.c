#include<stdio.h>
int main ()
{
int amount,n2000,n1000,n500,n200,n100,n50,n20,n10,n5,n2,n1;
printf("enter amount =");
scanf("%d",&amount);
n2000=amount/2000;
printf("2000 notes=%d\n",n2000);
amount=amount%2000;
n1000=amount/1000;
printf("1000 notes=%d\n",n1000);
amount=amount%1000;
n500=amount/500;
printf("500 notes=%d\n",n500);
amount=amount%500;
n200=amount/200;
printf("200 notes=%d\n",n200);
amount=amount%200;
n100=amount/100;
printf("100 notes=%d\n",n100);
amount=amount%100;
n50=amount/50;
printf("50 notes=%d\n",n50);
amount=amount%50;
n20=amount/20;
printf("20 notes=%d\n",n20);
amount=amount%20;
n10=amount/10;
printf("10 notes=%d\n",n10);
amount=amount%10;
n5=amount/5;
printf("5 notes=%d\n",n5);
amount=amount%5;
n2=amount/2;
printf("2 notes=%d\n",n2);
amount=amount%2;
n1=amount/1;
printf("1 notes=%d\n",n1);
amount=amount%1;
}