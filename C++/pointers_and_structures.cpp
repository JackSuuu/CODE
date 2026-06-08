#include <iostream>
using namespace std;

int main() {
    int var = 5;        // A regular integer variable
    int *ptr = &var;    // Pointer ptr stores the address of var

    cout << "Address of var: " << &var << endl;      // Print the address of var
    cout << "Value of ptr (Address of var): " << ptr << endl;  // Print the pointer value (address of var)
    cout << "Value pointed to by ptr: " << *ptr << endl;  // Dereference ptr to get the value at the address

    // Modifying the value using pointer
    *ptr = 10;  // Change the value of var through the pointer

    cout << "New value of var: " << var << endl;  // Print the updated value of var

    return 0;
}
