import java.util.ArrayList;

/**
 * Edinburgh
 */

public class Learn_Java_in_14_mins {

    public static void main(String args[]) {
        // Primitive data type
        int num = 10;
        char ch = 'S';
        long c = 400;
        double pi = 3.14;
        boolean isBreak = true;

        // Advanced data type
        String name = "Jack Su";

        System.out.println(name.toUpperCase());
        System.out.println("=======================================");

        // Call object from another file
        Animal_T a = new Animal_T();
        String dog = a.iAmDog();

        System.out.println("Calling Object: " + dog);
        Animal_T.doStuff();
        System.out.println("=======================================");

        // Java Arrays
        String[] cars = {"Volvo", "Ford", "Mercedes"};

        // Java data structure - ArrayList<Data_Type>
        ArrayList<String> arr = new ArrayList<String>();
        arr.add("Dog");
        arr.add("Lion");

        // Output terminal
        for (int i=0; i < name.length(); i++) {
            char each = name.charAt(i);
            System.out.println(each);
        }
        System.out.println("Hello World");
        addExclamationPoint("Edinburgh");
        char firstOfName = returnFirstChar(name);
        System.out.println(firstOfName);
        System.out.println("=======================================");
    }

    // Methods Construction
    public static void addExclamationPoint(String s) {
        System.out.println(s + "!");
    }

    // Functions Construction: state | status | returnType | functionName
    public static char returnFirstChar(String s) {
        return s.charAt(0);
    }
}
