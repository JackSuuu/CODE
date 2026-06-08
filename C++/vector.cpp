// Include the vector library
#include <vector>
#include <iostream>
using namespace std;

int main() {
    // Create a vector called cars that will store strings
    vector<string> cars;
    cars.push_back("Volvo");
    cars.push_back("BMW");
    cars.push_back("Ford");
    cars.push_back("Mazda");
  
    // Print vector elements
    for (vector<string>::const_iterator it = cars.begin(); it != cars.end(); ++it) {
      cout << *it << "\n";
    }
    return 0;
  }
  
