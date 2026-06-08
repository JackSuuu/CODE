#include <iostream>
#include <vector>

int main() {
    // Create an empty vector
    std::vector<int> arr;

    // Add initial elements to the vector
    arr.push_back(1);
    arr.push_back(2);
    arr.push_back(3);
    arr.push_back(4);
    arr.push_back(5);

    // Print the original array
    for (int i = 0; i < arr.size(); i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    // Add more elements to the vector
    arr.push_back(6);
    arr.push_back(7);

    // Print the modified array
    for (int i = 0; i < arr.size(); i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
