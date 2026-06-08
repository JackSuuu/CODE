#include <stdio.h>

void swap(int *a, int *b) {
    int t = *a;
    *a = *b, *b = t;
}

int main() {
    // function call 
    int x = 5;
    int y = 10;

    swap(&x, &y);
    printf("after swap - x: %d, y: %d\n", x, y);

    return 0;
}
