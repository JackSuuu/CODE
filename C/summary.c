#include <stdio.h>  // Standard input/output library
#include <stdlib.h> // Standard library for memory management, process control, etc.
#include <string.h> // String handling library

// Macro definition (preprocessor directive)
#define PI 3.14159

// Global variable declaration
int global_var = 10;

// Function declaration (prototypes)
int add(int a, int b);
void pointerExample(int *ptr);
void structExample();
void fileExample();
void dynamicMemoryExample();

// Structure definition
struct Person {
    char name[50];
    int age;
};

// Enum definition
enum Weekday { Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday };

int main() {
    // Basic variable types
    int a = 5;
    float f = 5.75;
    double d = 12.3456789;
    char c = 'A';
    char str[20] = "Hello, C";

    // Constants
    const int CONST_VALUE = 100;

    // Printing variables
    printf("int: %d, float: %.2f, double: %.8f, char: %c\n", a, f, d, c);
    printf("String: %s\n", str);

    // If-else condition
    if (a > 3) {
        printf("a is greater than 3\n");
    } else {
        printf("a is less than or equal to 3\n");
    }

    // Loops: for, while, do-while
    for (int i = 0; i < 5; i++) {
        printf("for loop iteration: %d\n", i);
    }

    int i = 0;
    while (i < 3) {
        printf("while loop iteration: %d\n", i);
        i++;
    }

    i = 0;
    do {
        printf("do-while loop iteration: %d\n", i);
        i++;
    } while (i < 3);

    // Switch-case
    enum Weekday today = Monday;
    switch (today) {
        case Sunday:
            printf("It's Sunday\n");
            break;
        case Monday:
            printf("It's Monday\n");
            break;
        default:
            printf("Another day of the week\n");
    }

    // Functions and return values
    int sum = add(3, 4);
    printf("Sum: %d\n", sum);

    // Pointers
    int b = 20;
    int *p = &b;  // Pointer to an integer
    printf("Address of b: %p, Value of b: %d\n", (void *)p, *p);
    pointerExample(p);

    // Arrays
    int numbers[] = {1, 2, 3, 4, 5};
    for (i = 0; i < 5; i++) {
        printf("Array element at index %d: %d\n", i, numbers[i]);
    }

    // Structs
    structExample();

    // Dynamic memory allocation
    dynamicMemoryExample();

    // File handling
    fileExample();

    // Exiting the program
    return 0;
}

// Function definitions
int add(int a, int b) {
    return a + b;
}

void pointerExample(int *ptr) {
    *ptr = 30;  // Changing the value of the variable that the pointer points to
    printf("Pointer-modified value: %d\n", *ptr);
}

// Struct example function
void structExample() {
    struct Person person1;
    strcpy(person1.name, "Alice");
    person1.age = 25;
    
    printf("Person's name: %s, age: %d\n", person1.name, person1.age);
}

// File handling example
void fileExample() {
    FILE *file = fopen("example.txt", "w");
    if (file == NULL) {
        printf("File couldn't be opened\n");
        return;
    }

    fprintf(file, "Hello, File IO in C!\n");
    fclose(file);

    // Reading file content
    file = fopen("example.txt", "r");
    char line[100];
    while (fgets(line, sizeof(line), file)) {
        printf("File content: %s", line);
    }
    fclose(file);
}

// Dynamic memory allocation example
void dynamicMemoryExample() {
    int *arr;
    int size = 5;
    arr = (int *)malloc(size * sizeof(int));  // Allocating memory dynamically
    if (arr == NULL) {
        printf("Memory allocation failed\n");
        return;
    }

    // Assigning and printing dynamic array values
    for (int i = 0; i < size; i++) {
        arr[i] = i + 1;
        printf("Dynamic array element at index %d: %d\n", i, arr[i]);
    }

    free(arr);  // Freeing dynamically allocated memory
}
