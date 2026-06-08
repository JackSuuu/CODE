#include <stdio.h>

int main() {
    long a[2];
    a[0] = 3;
    a[1] = 5;
    long *p = &a[1];
    // Pointer subtraction in C computes the difference
    // in terms of the number of elements, not bytes
    // Since `p` points to a[1] and &a[0] points to a[0],
    // The difference is 1
    long i = p - &a[0];
    long j = *p - a[0];

    printf("i = %ld, j = %ld\n", i, j);

    return 0;
}