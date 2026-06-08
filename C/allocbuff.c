#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ALLOCSIZE 10000 // size of avilable space

static char allocbuf[ALLOCSIZE];
static char *allocp = allocbuf; // next free position

char *alloc(int n) {
    if (allocbuf + ALLOCSIZE - allocp >= n) {
        allocp += n;
        return allocp - n;
    } else {
        return 0;
    }
}

void afree(char *p) {
    if (p >= allocbuf && p < allocbuf + ALLOCSIZE) {
        allocp = p;
    }
}

