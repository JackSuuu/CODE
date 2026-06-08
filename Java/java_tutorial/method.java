public class method {
    static Boolean myMethod() {
        // System.out.println("I just got executed");
        return true;
    }

    public static void main(String[] args) {
        System.err.println(myMethod());
        myMethod();
        myMethod();
    }
}
