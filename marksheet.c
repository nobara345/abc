#include<stdio.h>
int main()
{
 int marks[20][6] = {
 {88,86,76,56,87,75},
 {87,98,48,39,76,57},
 {98,67,86,47,65,83},
 {88,67,87,56,67,47},
 {56,77,98,45,78,68},
 {90,78,56,78,38,67},
 {87,87,56,48,94,55},
 {67,85,48,76,55,30},
 {66,77,98,56,48,98},
 {78,86,48,76,67,59},
 {87,67,57,98,46,29},
 {77,56,98,48,59,38},
 {68,47,56,39,65,87},
 {55,87,65,86,94,57},
 {57,87,56,98,47,58},
 {76,89,45,87,36,76},
 {67,88,68,96,58,46},
 {66,87,38,58,45,67},
 {67,86,57,66,48,38},
 {55,67,85,39,56,67}
 };
  int choice,roll,sub;
  printf("Press 1 : marks\n");    
  printf("Press 2 : result\n");
  printf("Press 3 : whole result\n");
  printf("Enter your choice = ");
  scanf("%d",&choice);
   switch(choice)
    {
     case 1:
     printf("Enter roll number = ");
     scanf("%d",&roll);
     printf("Press 0 : English\n");
     printf("Press 1 : Maths\n");
     printf("Press 2 : Biology\n");
     printf("Press 3 : Chemistry\n");
     printf("Press 4 : Physics\n");
     printf("Press 5 : Hindi\n");
     printf("Enter subject code = ");
     scanf("%d",&sub);
     printf("Marks = %d\n",marks[roll][sub]);
     break;
     
      case 2:
      printf("Enter a roll number = ");
      scanf("%d",&roll);
      printf("English = %d\n",marks[roll][0]);
      printf("Maths = %d\n",marks[roll][1]);
      printf("Biology= %d\n",marks[roll][2]);
      printf("Chemistry = %d\n",marks[roll][3]);
      printf("Physics= %d\n",marks[roll][4]);
      printf("Hindi= %d\n",marks[roll][5]);
      break;
            
       case 3:
       printf("\t\tEng\tMaths\tBio\tChem\tPhy\tHindi\n");
       for(int i=0; i<20; i++)
        {
         printf("Roll No. %d\t",i);
          for(int j=0; j<6; j++)
           {
            printf("%d\t",marks[i][j]);
           }
         printf("\n");
        }

    }
}