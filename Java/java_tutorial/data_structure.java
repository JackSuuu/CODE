import java.util.ArrayList;
import java.util.LinkedList;
import java.util.HashMap;

public class data_structure {

    public static void main(String[] args) {
        // Define the array_list
        ArrayList<String> cars = new ArrayList<String>();
        // Add items
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford");
        cars.add("Mazda");
        System.out.println(cars);

        // Access an Item
        System.out.println(cars.get(0));

        // Change an Item
        cars.set(0, "Mercedes");

        // Remove an Item
        cars.remove(0);
        // Clean: cars.clear()

        // ArrayList Size
        cars.size();

        // Loop Through an ArrayList
        for (int i=0; i<cars.size(); i++) {
            System.out.println(cars.get(i));
        }

        System.out.println("=====================");

        // Define the linked list
        LinkedList<String> courses = new LinkedList<String>();
        // Add items
        courses.add("OOP");
        courses.add("Cognitive Science");
        courses.add("CAP");
        System.out.println(courses);

        // In Java Linked List, You can call multiple methods
        // The structure of linked list is like Node_1 -> Node_2
        // addFirst(); -- Adds an item to the beginning of the list.
        // addLast (); -- Add an item to the end of the list
        // removeFirst(); -- Remove an item from the beginning of the list
        // removeLast(); -- Remove an item from the end of the list
        // getFirst(); -- Get the item at the beginning of the list
        // getLast(); -- Get the item at the end of the list

        // Java HashMap
        HashMap<String, String> studentRecord = new HashMap<String, String>();

        studentRecord.put("Jack", "Computer_Science");
        studentRecord.put("Leo", "Math and Business");
        System.out.println(studentRecord);
        System.out.println(studentRecord.get("Jack"));


    }
}
