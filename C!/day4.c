#include<stdio.h>
int main(){
    int a = 777;
    printf("|%d|\n", a);
    printf("|%-8d|\n", a);
    printf("|%8d|\n", a);
    printf("|%2d|\n", a);
    
    float b = 150.5;
    printf("|%f|\n", b);
    printf("|%-8.3f|\n", b);
    printf("|%8.2f|\n", b);
    printf("|%4.3f|\n", b);
    printf("S.Holmes:\n51grad 31\'25.48\" N\n0 grad  9\'29.93\" W\n");
    printf("||-----|-----|-----|-----||\n|| act | one | two | res ||\n||=====+=====+=====+=====||\n|| \t+|3\t |4\t |00007||\n|| \t-|\t\t3| \t4|-0001||\n|| \t*| \t3|4\t |00012||\n||\/\t |3\t |\t\t4|0.750||\n===========================\n");
    return 0;
}