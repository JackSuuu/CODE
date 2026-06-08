#include <iostream>

/*
Address Fetching: The address of a variable (&value) is fetched just the same, 
regardless of whether you cast it or not. 
The reinterpret_cast does not affect the performance of address fetching, 
as it merely changes how the pointer is interpreted.
Memory Interpretation:

By using reinterpret_cast<char *>, you’re saying, 
"I want to treat the memory of value as a raw byte stream."
This is particularly useful for operations like binary data manipulation 
or network communication, where you need to work with raw memory in a specific way.

Clarity for the Programmer:
The cast makes it clear that the programmer intends to treat the memory of value as a sequence of bytes 
(char* is often used for raw memory operations).
Without the cast, you would have a pointer to the original type (&value), 
which wouldn’t allow you to manipulate the memory as bytes.
*/

int main() {
    int value = 0x12345678; // 4-byte integer
    char *source = reinterpret_cast<char *>(&value);

    // Print individual bytes
    for (size_t i = 0; i < sizeof(value); i++) {
        printf("Byte %zu: 0x%02X\n", i, static_cast<unsigned char>(source[i]));
    }

    return 0;
}
