#include <iostream>
using namespace std;

void fun(string parameter) {
    cout << "Hi funtion" + parameter << endl;
}


int main() {
    // Hello World
    cout << "Hello World!";
    return 0;

    // Data types
    int age = 25;
    double pi = 3.14159;
    char grade = 'A';
    bool isStudent = true;

    // Operator
    int x = 10;
    int y = 5;
    int sum = x + y;
    int product = x * y;
    int remainder = x % y;

    // if-else statement
    int number = 7;

    if (number > 10) {
        cout << "The number is greater than 10." << std::endl;
    } else {
        cout << "The number is less than or equal to 10." << std::endl;
    }

    // loop
    for (int i = 0; i < 5; i++) {
        cout << "Iteration: " << i << std::endl;
    }

}








