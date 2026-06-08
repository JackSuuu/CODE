public class Luly {

    public static void main(String[] args) {

        // Primitive Data Type
        int age = 20, height = 180;
        char n = 'L';
        String name = "Luly";
        double pi = 3.14;
        boolean is_hungry = false;

        int round_pi = (int) pi;

        round_pi ++;
        round_pi += 1;

        if (is_hungry) {
            System.out.println("一点都不饿呢");
        } else {
            System.out.println("快要饿死了");
        }

        switch (name) {
            case "Jack":
                System.out.println("1");
                break;
            case "Leo":
                System.out.println("2");
                break;
            case "Luly":
                System.out.println("Ohh it's correct");
                break;
            default:
                System.out.println("Not fit at all cases");
        }

        for (int i=0; i<=10; i++) {
            System.out.print(i);
            System.out.print(", ");
        }

        System.out.println("\n");
        System.out.println("=================我是一条分割线=================");

        int i = 0;
        while (i<=10) {
            System.out.println(i);
            i++;
        }

        System.out.println("=================我是一条分割线=================");

        int j = 0;
        do {
            System.out.println(j);
            j++;
        } while (j<=10);
        
        System.out.println(name + " --> Height is: " + String.valueOf(height) + ", age is: " + String.valueOf(age));
    }
}
