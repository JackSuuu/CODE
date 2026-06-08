# include <iostream>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);

    // Because C++ array has fixed size, so it can not add
    // Rest of the code...
    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    arr[size] = 6;
    arr[size + 1] = 7;
    size += 2;

    return 0;
}