#include<stdio.h>
int main()
{
int num=8,attempt=1,guess;
while(1)
{
  printf("\nenter a number=");
  scanf("%d",&guess);
  if(num==guess)
  {
    printf("your guess is correct");
    break;
  }else if(num>guess)
  {
    printf("the number is smaller");
    attempt++;
  }
  else
  {
    printf("the number is greater");
    attempt++;
  }
}
}