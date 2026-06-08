#include <stdio.h>
#include <math.h>
#include <string.h>

int my_array[] = {1,23,17,4,-5,100};
int *ptr;

struct tag {
    char lname[20];
    char fname[20];
    int age;
    float rate;
};

int main(void) {
    int i = 0;
    double d = cos(1.2);
    ptr = &my_array[0];

    printf("%d\n", i);

    for (i = 0; i < 6; i++) {
        printf("my_array[%d] = %d ", i, my_array[i]); /*<-- A */
        printf("ptr + %d = %d\n", i, *(ptr + i));     /*<-- B */
    }

    // declare my structure
    struct tag my_struct;
    strcpy(my_struct.lname,"Jensen");
    printf("%s ", my_struct.fname);

    return 0;
}

#define LOOPS 100 /* constant */
#define MAX(A, B) (A < B ? B : A) /* macro */
#define DEBUG2
