#include <iostream>
#include <stdexcept>

class Fraction {
private:
    int numerator;
    int denominator;

    // Custom GCD function using Euclidean algorithm
    int gcd(int a, int b) const {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    // Helper function to simplify fractions
    void simplify() {
        int gcdValue = gcd(numerator, denominator);  // Use custom gcd
        numerator /= gcdValue;
        denominator /= gcdValue;
        // Ensure the denominator is positive
        if (denominator < 0) {
            numerator = -numerator;
            denominator = -denominator;
        }
    }

public:
    // Constructor
    Fraction(int num, int denom) {
        if (denom == 0) {
            throw std::invalid_argument("Denominator cannot be zero");
        }
        numerator = num;
        denominator = denom;
        simplify();
    }

    // Addition operator
    Fraction operator+(const Fraction& other) const {
        int num = numerator * other.denominator + denominator * other.numerator;
        int denom = denominator * other.denominator;
        return Fraction(num, denom);
    }

    // Subtraction operator
    Fraction operator-(const Fraction& other) const {
        int num = numerator * other.denominator - denominator * other.numerator;
        int denom = denominator * other.denominator;
        return Fraction(num, denom);
    }

    // Multiplication operator
    Fraction operator*(const Fraction& other) const {
        int num = numerator * other.numerator;
        int denom = denominator * other.denominator;
        return Fraction(num, denom);
    }

    // Division operator
    Fraction operator/(const Fraction& other) const {
        if (other.numerator == 0) {
            throw std::invalid_argument("Cannot divide by zero");
        }
        int num = numerator * other.denominator;
        int denom = denominator * other.numerator;
        return Fraction(num, denom);
    }

    // Output stream operator to print the fraction
    friend std::ostream& operator<<(std::ostream& os, const Fraction& f) {
        os << f.numerator << "/" << f.denominator;
        return os;
    }

    // Getter for numerator and denominator
    int getNumerator() const { return numerator; }
    int getDenominator() const { return denominator; }
};

int main() {
    try {
        Fraction f1(1, 3);
        Fraction f2(2, 3);
        
        // Example usage
        std::cout << "f1: " << f1 << std::endl;
        std::cout << "f2: " << f2 << std::endl;

        // Addition
        std::cout << "f1 + f2: " << f1 + f2 << std::endl;

        // Subtraction
        std::cout << "f1 - f2: " << f1 - f2 << std::endl;

        // Multiplication
        std::cout << "f1 * f2: " << f1 * f2 << std::endl;

        // Division
        std::cout << "f1 / f2: " << f1 / f2 << std::endl;

    } catch (const std::invalid_argument& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }

    return 0;
}
