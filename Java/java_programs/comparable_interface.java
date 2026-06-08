import java.util.ArrayList;
import java.util.Collections;

// Define a class representing a fruit
// Comparable is a build in interface in java.util package
class Fruit implements Comparable<Fruit> {
    private String name;
    private int quantity;

    public Fruit(String name, int quantity) {
        this.name = name;
        this.quantity = quantity;
    }

    public String getName() {
        return name;
    }

    public int getQuantity() {
        return quantity;
    }

    @Override
    public int compareTo(Fruit other) {
        // Compare fruits based on their quantity
        return Integer.compare(this.quantity, other.quantity);
    }

    @Override
    public String toString() {
        return "Fruit [name=" + name + ", quantity=" + quantity + "]";
    }
}

public class comparable_interface {
    public static void main(String[] args) {
        // Create some fruit objects
        Fruit apple = new Fruit("Apple", 10);
        Fruit orange = new Fruit("Orange", 5);
        Fruit banana = new Fruit("Banana", 8);

        // Create an ArrayList to store fruits
        ArrayList<Fruit> fruits = new ArrayList<>();
        fruits.add(apple);
        fruits.add(orange);
        fruits.add(banana);

        // Print fruits before sorting
        System.out.println("Fruits before sorting:");
        for (Fruit fruit : fruits) {
            System.out.println(fruit);
        }

        // Sort fruits using Collections.sort() method
        Collections.sort(fruits);

        // Print fruits after sorting
        System.out.println("\nFruits aftet sorting: ");
        for (Fruit fruit : fruits) {
            System.out.println(fruit);
        }
    }
}
