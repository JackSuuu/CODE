public class java_lab_w1 {
    public static void main(String[] args) {
        String first_num;
        String second_num; 

        first_num = args[0];
        second_num = args[1];

        System.out.print("The Output of two numbers multiple together is: ");
        System.out.println(Integer.parseInt(first_num) * Integer.parseInt(second_num));
    }
}
