import java.util.Scanner;

public class redirection {
    public static void main(String[] args) {
        // Create a Scanner to read from standard input
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter some input
        System.out.println("Enter some text:");

        // Read input from standard input
        String input = scanner.nextLine();
        while (input != null) {
            System.out.println(input);
            input = scanner.nextLine();
        }



        // Close the Scanner after reading from standard input
        scanner.close();
    }
}
