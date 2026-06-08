
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Person {
    private String name; // private = restricted access
    private int age;

    // Getter
    public String getName() {
        return name;
    }

    // Get age
    public int getAge() {
        return age;
    }

    // Setter
    public void setName(String newName) {
        this.name = newName;
    }
}

public class tutorial {

    public static int fun() {
        return 10;
    }

    public List<Integer> Loop() {
        List<Integer> numbers = new ArrayList<>();
        for (int i = 0; i <= 10; i ++) {
            numbers.add(i);
        }
        return numbers;
    }

    public static void main(String[] args) {
        // Primitive Variable
        int a = 5;
        char b = 'A';
        long c = 400;
        double d = 3.14;

        // Non-primitive data
        String name = "Jack";
        
        // Output and Input
        // Create a Scanner object
        Scanner scanner = new Scanner(System.in);
        String input_name = scanner.nextLine();
        System.out.println(name.length());
        System.out.println(input_name);
        System.out.println(fun());
        scanner.close();

        // code block here;
        System.out.println("Hello World");
    } 
}
