#include <stdio.h>
int main(void){
    int age, height, weight;
    double bov_m, bov_f;

    printf("What's your age?\n");
    scanf("%d", &age);

    printf("What's your height?");
    scanf("%d", &height);

    printf("What's your weight?");
    scanf("%d", &weight);

    bov_m = 10*weight + 6.25*height - 5*age + 5;
    bov_f = 10*weight + 6.25*height - 5*age - 161;

    printf("|     BMR        |\n");
    printf("| male | female |\n");
    printf("|%8.2f|%8.2f|\n",bov_m, bov_f);

    return 0;
    }