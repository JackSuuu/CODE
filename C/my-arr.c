#include <stdio.h>
#include <stdlib.h>

int main() {
    int numbers[] = {18, 23, 1, 20, 5};
    int sizeOfArr = sizeof(numbers) / sizeof(numbers[0]);

    for (int i=0; i<sizeOfArr; i++) {
        printf("size is %d ", sizeOfArr);
        printf("%s%d\n", "Array Number: ", numbers[sizeOfArr]);

    }    

    return 0;
}