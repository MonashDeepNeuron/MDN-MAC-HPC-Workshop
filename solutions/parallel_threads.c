#include <stdio.h>
#include <time.h>
#include <pthread.h>

#define NUM_HELLOS 2000000

void thread1(){
    for(int i = 0; i <= NUM_HELLOS/2; i++){
        printf("Hello World x %d \r", i);
        fflush(stdout);
    }
}

void thread2(){
    for(int i = 0; i <= NUM_HELLOS/2; i++){
        printf("Hello World x %d \r", i);
        fflush(stdout);
    }
}

void parallel_hello(){
    pthread_t thread1_id, thread2_id;
    pthread_create(&thread1_id, NULL, thread1, NULL);
    pthread_create(&thread2_id, NULL, thread2, NULL);
    pthread_join(thread1_id, NULL);
    pthread_join(thread2_id, NULL);
}

int main(){
    float startTime = (float) clock()/CLOCKS_PER_SEC;
    parallel_hello();
    float endTime = (float) clock()/CLOCKS_PER_SEC;
    printf("Total Execution Time: %f", endTime-startTime);
    return 0;
}