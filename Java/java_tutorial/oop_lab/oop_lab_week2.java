package OOP_Lab;

public class oop_lab_week2 {
    public String[] quadratic_solver(double a, double b, double c) {
        boolean is_neg = false;

        double det_inner = Math.pow(b, 2) - 4 * a * c;

        if (det_inner < 0) {
            is_neg = true;
        } else {
            is_neg = false;
        }

        double det = Math.sqrt(Math.abs(det_inner));

        double x_1;
        double x_2;
        String fin_1;
        String fin_2;

        // (-b - det) / 2*a

        if (! is_neg) {
            x_1 = (-b - det) / 2*a;
            x_2 = (-b + det) / 2*a;
            fin_1 = String.valueOf(x_1);
            fin_2 = String.valueOf(x_2);
        } else {
            double fir = -b / 2*a;
            double sec = det / 2*a;
            fin_1 = String.valueOf(fir) + " + " + String.valueOf(sec) + "i";
            fin_2 = String.valueOf(fir) + " - " + String.valueOf(sec) + "i";
        }

        return new String[]{fin_1, fin_2};
    }

    public static void main(String[] args) {
        // Q1 - Integer Distance
        int A = 10; //Integer.parseInt(args[0]);
        int B = 8; ///Integer.parseInt(args[1]);

        int sum = Math.max(A, B) - Math.min(A, B);
        System.out.println(sum);

//        System.out.println("=======================");

        // Q12 - Quadratic Solver with Imaginary Parts
        // - compute the discriminnt
        // - return the real or imaginary part
        double a = 1.0;
        double b = -2.0;
        double c = 2.0;

    }
}
