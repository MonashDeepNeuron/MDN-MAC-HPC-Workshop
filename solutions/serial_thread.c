#include <stdio.h>
#include <time.h>

#define NUM_HELLOS 200000

int main(){
    float startTime = (float) clock()/CLOCKS_PER_SEC;
    for(int i = 0; i <= NUM_HELLOS; i++){
        printf("Hello World x %d \r", i);
        fflush(stdout);
    }
    float endTime = (float) clock()/CLOCKS_PER_SEC;
    printf("Total Execution Time: %f", endTime-startTime);
}