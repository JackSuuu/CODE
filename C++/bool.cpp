#include <cstdint>
#include <cstdio>
#include <iostream>
using namespace std;

int comp(int a, int b) {
    return true ? a > b : false;
}

 // Definition for a binary tree node.
int main() {
    cout << comp(1, 5) + comp(5, 1) + comp(5, 1) << '\n';
}