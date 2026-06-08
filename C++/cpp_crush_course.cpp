// Introduction to C++
// This is a crush course that go through the basic componenet of c++
// C++ can be used for High-performance applications / Video games / Device drivers...
// C++ is one of the **fastest** and **most efficient** language

// C++ standard library: data structure, algorithm...

// Basic IO file in stand library, input - output - stream
#include <iostream>
#include <cmath>
using namespace std;

int c_math_usage() {
    double result = pow(2, 3);
    return result;
    return 0;
}

int operator_priority() {
    double x = 1 + 2 * 3;
    cout << x;
    return 0;
}

int mathematical_expression() {
    int x = 10;
    int y = 3;
    // All mathematical operations include { + - * / %}
    int z = x + y;
    // Increment a variable
    x += 2;
    cout << z << endl;
    cout << x << endl;
    return 0;
}

int var() {
    // Variable in C++
    int var_a = 5, var_b = 10;  // Define different vaiable in a same line
    int temp = var_a;
    var_a = var_b;
    var_b = temp;

    // Define unchanged constant
    const double pi = 3.14;

    double sales = 9.99;
    cout << var_a << endl << endl;

    return 0;
}

// "main" is the core program of executing your program, 
// all the function will be call / manipulate at this chunk
int main() {  // the "int" indicate its successful execution.
    // var();
    // "std" stands for standard library
    // "cout" stands for character out 
    cout << "Function Output: " << c_math_usage() << endl;
    cout << "Hello, World" << endl;

    // Input value in C++
    // cout << "Input your farenheit value: ";
    // int fahrenheit;
    // cin >> fahrenheit;
    // double celsius = (fahrenheit - 32) / 1.8;
    // cout << celsius;
    // return 0;
}

