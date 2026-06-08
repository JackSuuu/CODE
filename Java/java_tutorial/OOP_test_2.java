import java.util.Scanner;

public class OOP_test_2 {
    public static void fizzbuzz(int from, int to, int fizz, int buzz) {
        int number = from;
        
        System.out.printf("going from %d to %d, fizzing on %d and buzzing on %d%n",
                                from, to, fizz, buzz);
        while (number <= to) {
            boolean printNumber = true;
            if (number % fizz == 0) {
                System.out.print("fizz");
                printNumber = false;
            }
            if (number % buzz == 0) {
                System.out.print("buzz");
                printNumber = false;
            }
            if (printNumber) {
                System.out.print(number);
            }
            number ++;
            System.out.println();
        }
    }

    public static void printDirection(String abbreviation) {
        String[] abbreviations = abbreviation
                                    .toUpperCase()
                                    .split("");

        for (int index = 0; index < abbreviations.length; index++) {
            switch (abbreviations[index]) {
                case "N":
                    abbreviations[index] = "North";
                    break;
                case "S":
                    abbreviations[index] = "South";
                    break;
                case "E":
                    abbreviations[index] = "East";
                    break;
                case "W":
                    abbreviations[index] = "West";
            }
        }
        System.out.println(String.join("-", abbreviations));
    }

    public static int getFactorial(int number) {
        int factorial = 1;
        for (int i=1; i <= number; i++) {
            factorial *= i;
        }
        return factorial;
    }

    private static void moveTower(int disc, String source, String dest, String spare) {
        if (disc <= 1) {
            System.out.printf("Move disc %s: %s -> %s%n", disc, source, dest);
        } else {
            moveTower(disc-1, source, spare, dest);
            System.out.printf("Move disc %s: %s -> %s%n", disc, source, dest);
            moveTower(disc-1, spare, dest, source);
        }
    }

    public static void main(String[] args) {
        // fizzbuzz(8, 16, 3, 5);
        // printDirection("NW");
        // for (int i=0; i <= 10; i++) {
        //     System.out.printf("Factorial of %d is %d%n", i, getFactorial(i));
        // }
        Scanner scanner = new Scanner(System.in);
        int discs = scanner.nextInt(); // read number of discs from user input
        scanner.close();
        moveTower(discs, "Left", "Middle", "Right");
    }
}
