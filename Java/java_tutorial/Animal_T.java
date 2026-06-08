public class Animal_T {

    public String iAmDog() {
        return "I am a dog";
    }

    public static void doStuff() {
        int a = 5;

        // Desicion Block
        if (a > 4) {
            System.out.println(a);
        } else if (a == 4) {
            System.out.println("Just Right");
        } else {
            System.out.println("Ohh, not fitable");
        }

        // For Loop
        for (int i = 1; i <= 9; i ++) {
            for (int j = 1; j <= 9; j++) {
                int res = i * j;
                System.out.println(i + " * " + j + " = " + res);
            }
        }

        // While Loop
        while (a > 0) {
            System.out.println("Still remain loop: " + a);
            a -= 1;
        }

        // Error catching
        try {
            // code block
        } catch(Exception e) {
            // When exception occur, this code will run
        }
    }
}
