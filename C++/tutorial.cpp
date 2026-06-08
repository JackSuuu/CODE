# include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

class MyClass {
    public:
        string myString;

        MyClass() : myString("Jack") {} // default constructor

        void myMethod() {
            cout << "Hello This is a method";
        }
};

int main(int argc, char const *argv[])
{
    MyClass myobj;
    myobj.myMethod();
    return 0;
}
