// Define a class called "Car"
class Car {
    private String brand;
    private String color;
    private int year;

    // Constructor
    public Car(String brand, String color, int year) {
        this.brand = brand;
        this.color = color;
        this.year = year;
    }

    // Getter methods
    public String getBrand() {
        return this.brand;
    }

    public String getColor() {
        return this.color;
    }

    public int getYear() {
        return this.year;
    }

    // Method to display car information
    public void displayInfo() {
        System.out.println("Brand: " + this.brand);
        System.out.println("Color: " + this.color);
        System.out.println("Year: " + this.year);
    }
}


public class OOP {
    public static void main(String[] args) {
        Car myCar = new Car("Toyota", "Red", 2022);
        myCar.displayInfo();
        
    }
}
