public class Tutorial_2 {
    private static int ageToInt(String age) {
        int parsed = Integer.parseInt(age);
        return parsed;
    }

    public static void main(String[] args) {
        System.out.println("My age is " + ageToInt(args[0]));
    }
}
