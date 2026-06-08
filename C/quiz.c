#include <stdio.h>

int main(int argc, char const *argv[])
{
    int x[10];

    for (int i = 0; i < 10; i++) {
        x[i] = i + 1;
    }

    for (int i = 0; i < 10; i++) {
        printf("%d ", x[i]);
    }

    int *p = &x[0];
    int i;

    for (i = 0; i < 10; i++)  {
        *p = ++(*p);
        *p = (*p)--;
        p++;
    }
    for (i = 0; i < 10; i++) {
        printf("%d ", x[i]);
    }

    printf("\n");
    return 0;
}
