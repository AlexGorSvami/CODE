#include <stdio.h>
int main(void){
    for (int i=1; i<=5; i++){
        for (int j=1; j<=5; j++)
            printf("%-5d", i*j);
        printf("\n");
    }
    {
      printf("N\t10*N\t100*N\t1000*N\n\n");  
  for (int i=1;i<=10;i++)
    printf("%d\t%d\t%d\t%d\n",i,10*i,100*i,1000*i);
    }
    return(0);
}