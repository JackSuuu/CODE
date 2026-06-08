#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// clear function using poionter
void clear2(int *array, int size) {
    int *p;
    for (p = &array[0]; p < &array[size]; p++) {
        *p = 0;
    }
}

int main() {
    int x = 10;
    char *pmessage;
    int *ptr = &x;

    pmessage = "now is this the time";

    printf("%d", *ptr);

    return 0;
}